package org.example;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.IllegalFormatCodePointException;
import java.util.Map;

public class Solver {

    public static void main(String[] args) {
        byte[] bytes;
        try (BufferedInputStream input = new BufferedInputStream(new FileInputStream("program_path"))) {
            bytes = input.readAllBytes();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        Map<Integer,Character> data=new HashMap<>();
        Map<Integer, Action> actions = generateActions();
        for(int n=21;n<0x7f;n++) {
            if('A'<=n&&n<='Z') continue;
            int offset = 1;
            int[] stack = new int[0x1000];
            stack[0]=n;
            try {
                for (int i = 0; i < bytes.length; i++) {
                    int d = Byte.toUnsignedInt(bytes[i]);
                    if (d == 16) {
                        i += 1;
                        log("shuffle");
                        int k = Byte.toUnsignedInt(bytes[i]);
                        for (int j = 0; j < (k >> 1); j++) {
                            int o = stack[offset + (j - k)];
                            stack[offset + (j - k)] = stack[offset + ~j];
                            stack[offset + ~j] = o;
                        }
                    } else if (d == 10 || d == 0xb || d == 0xc || d == 0xd) {
                        if (d == 10) {
                            //log("put "+((char)bytes[i+1]));
                            stack[offset] = bytes[i + 1];
                            offset++;
                            i++;
                        } else {
                            //System.out.println("jump "+(d==0xd?"no rule":(d==0xb?"not zero":"zero"))+" "+((bytes[i + 1] << 8) | bytes[i + 2])+" "+(bytes[i + 1] << 8)+" "+Byte.toUnsignedInt(bytes[i+2]));
                            boolean flag = false;
                            if (stack[offset - 1] != 0 && d == 0xb) {
                                flag = true;
                            } else if (stack[offset - 1] == 0 && d == 0xc) {
                                flag = true;
                            } else if (d == 0xd) flag = true;
                            //System.out.println(flag);
                            if (flag) i += ((bytes[i + 1] << 8) | Byte.toUnsignedInt(bytes[i + 2]));
                            i += 2;
                        }
                    } else {
                        if (actions.get(d) == null) {
                            System.out.println(d + " " + Integer.toHexString(i));
                        }
                        offset += actions.get(d).act(stack, offset);
                    }
                }
            } catch (IllegalFormatCodePointException e) {
                data.put(stack[0]&0xff,(char)n);
            }
        }
        char[] dataa={0xc6, 0x8b, 0xd9, 0xcf, 0x63, 0x60, 0xd8, 0x7b, 0xd8, 0x60, 0xf6, 0xd3, 0x7b, 0xf6, 0xd8, 0xc1, 0xcf, 0xd0, 0xf6, 0x72, 0x63, 0x75, 0xbe, 0xf6, 0x7f, 0xd8, 0x63, 0xe7, 0x6d, 0xf6, 0x63, 0xcf, 0xf6, 0xd8, 0xf6, 0xd8, 0x63, 0xe7, 0x6d, 0xb4, 0x88, 0x72, 0x70, 0x75, 0xb8, 0x75};
        for(int i=dataa.length-1;0<=i;i--){
            System.out.print(data.get((int)dataa[i]));
        }
    }

    private static void log(String str) {
        //System.out.println(str);
    }

    private static Map<Integer, Action> generateActions() {
        Map<Integer, Action> actions = new HashMap<>();
        actions.put(0, (a, b) -> {
            throw new IllegalFormatCodePointException(1);
        });
        actions.put(1, (a, b) -> {
            log("add " + a[b - 2] + " " + a[b - 1] + " " + (a[b - 2] + a[b - 1]));
            a[b - 2] += a[b - 1];
            return -1;
        });
        actions.put(2, (a, b) -> {
            log("sub " + a[b - 2] + " " + a[b - 1] + " " + (a[b - 2] - a[b - 1]));
            a[b - 2] = a[b - 2] - a[b - 1];
            return -1;
        });
        actions.put(3, (a, b) -> {
            log("and " + a[b - 2] + " " + a[b - 1] + " " + (a[b - 2] & a[b - 1]));
            a[b - 2] = a[b - 2] & a[b - 1];
            return -1;
        });
        actions.put(4, (a, b) -> {
            log("or " + a[b - 2] + " " + a[b - 1] + " " + (a[b - 2] | a[b - 1]));
            a[b - 2] = a[b - 2] | a[b - 1];
            return -1;
        });
        actions.put(5, (a, b) -> {
            log("xor " + a[b - 2] + " " + a[b - 1] + " " + (a[b - 2] ^ a[b - 1]));
            a[b - 2] = a[b - 2] ^ a[b - 1];
            return -1;
        });
        actions.put(6, (a, b) -> {
            log("shift " + a[b - 2] + " " + (a[b - 1] & 0x1f) + " " + (a[b - 2] << (a[b - 1] & 0x1f)));
            a[b - 2] = a[b - 2] << (a[b - 1] & 0x1f);
            return 0;
        });
        actions.put(7, (a, b) -> {
            log("unshift " + a[b - 2] + " " + (a[b - 1] & 0x1f) + " " + (a[b - 2] >> (a[b - 1] & 0x1f)));
            a[b - 2] = a[b - 2] >> (a[b - 1] & 0x1f);
            return -1;
        });
        actions.put(8, (a, b) -> {
            a[b] = read();
            log("read a char " + (char) a[b] + " " + a[b]);
            return 1;
        });
        actions.put(9, (a, b) -> {
            log("print a char");
            //System.out.print((char)a[b-1]);
            return -1;
        });
        actions.put(0xf, (a, b) -> {
            log("copy " + a[b - 1]);
            a[b] = a[b - 1];
            return 1;
        });
        actions.put(0xe, (a, b) -> {
            log("back3");
            return -1;
        });
        actions.put(0x11, (a, b) -> {
            log("shuffle2");
            int local_30 = a[b - 1];
            for (int i = 0; i < 8; i++) {
                a[b - 1 + i] = local_30 & 1;
                local_30 = local_30 >> 1;
            }
            return 7;
        });
        actions.put(0x12, (a, b) -> {
            log("shuffle1");
            int local_2f = 0;
            for (int i = 7; -1 < i; i--) {
                local_2f = local_2f << 1 | a[b - 8 + i] & 1;
            }
            a[b - 8] = local_2f;
            return -7;
        });
        return actions;
    }

    public interface Action {
        int act(int[] stack, int off);
    }

    private static int read() {
        try{
            return System.in.read();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
