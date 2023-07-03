import java.io.*;
import java.util.*;

public class Reader {
    public static void main(String[] args) {
        byte[] bytes;
        try (BufferedInputStream input = new BufferedInputStream(new FileInputStream("program_path"))) {
            bytes = input.readAllBytes();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        try(BufferedWriter writer=new BufferedWriter(new FileWriter("result.txt"))){
            Map<Integer,String> map=new TreeMap<>();
            Set<Integer> labels=new HashSet<>();
            for(int i=0;i<bytes.length;i++){
                int l=Byte.toUnsignedInt(bytes[i]);
                String str=String.format("%02X",l);
                int k=0;
                if(l==10|0x10==l) k=1;
                else if(0x0b<=l&&l<=0xd) k=2;
                if(0<k){
                    str=str+" ";
                    if(0x0b<=l&&l<=0xd){
                        int o=(bytes[i+1]<<8)|Byte.toUnsignedInt(bytes[i+2])+2;
                        int adr=(i + o + 1);
                        labels.add(adr);
                        str+="label_"+(adr);
                    }else {
                        str+=String.format("%02X", Byte.toUnsignedInt(bytes[i + 1]));
                    }
                }
                System.out.println(i);
                map.put(i,str+"\n");
                i +=k;
            }
            map.forEach((a,b)-> {
                try {
                    if(labels.contains(a)) b="label_"+a+":"+b;
                    writer.write(b);
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            });
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
