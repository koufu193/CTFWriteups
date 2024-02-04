package challenge;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Challenge {
    static final int[] DAT_00404020 = {0x04, 0x07, 0x0b, 0x00, 0x20, 0x09, 0x0d, 0x1c, 0x06, 0x15, 0x0d, 0x0d, 0x05, 0x1f, 0x16, 0x14, 0x03, 0x21, 0x07, 0x22, 0x0e, 0x05, 0x1f, 0x07, 0x17, 0x12, 0x0f, 0x0b, 0x10, 0x09, 0x16, 0x07};
    static final int[] KEY_1 = {-1, 0, 1, 0};
    static final int[] KEY_2 = {0, 1, 0, -1};
    static final int[] CHAR_KEY_MAP_2 = {1, 2, 3, 2, 3, 3};
    static final int[] CHAR_KEY_MAP_1 = {0, 0, 0, 1, 1, 2};
    static final char[] map = new char[36];
    static final Map<Character, Integer> unmap = new HashMap<>();

    static {
        int counter = 0;
        for (char alphabet = 'a'; alphabet <= 'z'; alphabet++) {
            map[counter] = alphabet;
            counter++;
        }
        for (char digit = '0'; digit <= '9'; digit++) {
            map[counter] = digit;
            counter++;
        }
        for (int i = 0; i < map.length; i++) {
            unmap.put(map[i], i);
        }
    }

    public static void main(String[] args) {
        printMaze();
    }
    public static void printMaze(){
        for(int i=0;i<8;i++){
            for(int j=0;j<8;j++){
                System.out.printf("%2d,",FUN_004012b0(i,j));
            }
            System.out.println();
        }
        System.out.println();
    }

    public static boolean validInput(char[] flag, int[] convertedFlag) {
        if (!new String(flag).matches(
                "^[0-9a-z]{32}$"
        )) {
            return false;
        }
        for (int i = 0; i < 0x20; i++) {
            int iVar2 = (unmap.get(flag[i]) + DAT_00404020[i]) % 0x24;
            convertedFlag[i * 2] = iVar2 / 6;
            convertedFlag[i * 2 + 1] = iVar2 % 6;
        }
        return true;
    }

    public static boolean checkFlag(int[] flag) {
        int iVar1;
        int iVar2;
        int uVar3;
        int uVar4;
        int iVar5;
        int uVar7;
        int iVar8;
        int iVar9;
        int iVar10;
        int uVar11;
        int local_84;
        int[] local_78 = new int[14];

        uVar11 = 0;
        uVar7 = 0;
        uVar3 = FUN_004012b0(0, 0);
        iVar9 = 1;
        local_84 = 0;
        iVar5 = -1;
        iVar10 = 0;
        do {
            System.out.println("checking " + flag[uVar11 + uVar7 * 8] + " " + (uVar11 + uVar7 * 8));
            iVar1 = local_84;
            iVar8 = KEY_1[CHAR_KEY_MAP_2[flag[uVar11 + uVar7 * 8]]];
            iVar2 = KEY_2[CHAR_KEY_MAP_2[flag[uVar11 + uVar7 * 8]]];
            if (
                    (iVar5 + KEY_1[CHAR_KEY_MAP_1[flag[uVar11 + uVar7 * 8]]] != 0) ||
                            (iVar10 + KEY_2[CHAR_KEY_MAP_1[flag[uVar11 + uVar7 * 8]]] != 0)
            ) {
                iVar8 = KEY_1[CHAR_KEY_MAP_1[flag[uVar11 + uVar7 * 8]]];
                iVar2 = KEY_2[CHAR_KEY_MAP_1[flag[uVar11 + uVar7 * 8]]];
                if (
                        (KEY_1[CHAR_KEY_MAP_2[flag[uVar11 + uVar7 * 8]]] + iVar5 != 0) ||
                                (KEY_2[CHAR_KEY_MAP_2[flag[uVar11 + uVar7 * 8]]] + iVar10 != 0)
                ) {
                    return false;
                }
            }
            iVar10 = iVar2;
            iVar5 = iVar8;
            uVar4 = FUN_004012b0(uVar7, uVar11);
            if ((uVar4 & uVar3) != -1) {
                if (uVar4 == uVar3) {
                    local_84++;
                    if (3 < local_84) return false;
                } else {
                    local_84 = 1;
                    if(uVar3!=-1) {
                        iVar8 = local_78[uVar3];
                        if (local_78[uVar3] < iVar1) {
                            iVar8 = iVar1;
                        }
                        local_78[uVar3] = iVar8;
                    }
                }
            }
            uVar7 = uVar7 + iVar5;
            uVar11 = uVar11 + iVar10;
            if (iVar9 - 1 < 0x3f) {
                if ((uVar7 | uVar11) == 0) return false;
            } else if (iVar9 == 0x80) {
                if (equalsAll(local_78, 3)) {
                    return true;
                }
                return false;
            }
            if (7 < (uVar7 | uVar11)) return false;
            iVar9 = iVar9 + 1;
            uVar3 = uVar4;
        } while (true);
    }

    static int FUN_004012b0(int param_1, int param_2) {
        long uVar1;

        uVar1 = 1L << ((param_2 + param_1 * 8L) & 0x3fL);
        if ((uVar1 & 0xfL) != 0) {
            return 0;
        }
        if ((uVar1 & 0x101030L) != 0) {
            return 1;
        }
        if ((uVar1 & 0xe0c0L) != 0) {
            return 2;
        }
        if ((uVar1 & 0x2060200L) != 0) {
            return 3;
        }
        if ((uVar1 & 0x1c080c00L) != 0) {
            return 4;
        }
        if ((uVar1 & 0xe0e00000L) != 0) {
            return 5;
        }
        if ((uVar1 & 0x2020700000000L) != 0) {
            return 6;
        }
        if ((uVar1 & 0x7800000000L) == 0) {
            if ((uVar1 & 0x301010000000000L) != 0) {
                return 8;
            }
            if ((uVar1 & 0xc040c0000000000L) != 0) {
                return 9;
            }
            if ((uVar1 & 0xf00000000000L) != 0) {
                return 10;
            }
            if ((uVar1 & 0x1038000000000000L) == 0) {
                return -((uVar1 & 0xe080000000000000L) == 0 ? 1 : 0) | 0xc;
            }
            return 0xb;
        }
        return 7;
    }

    private static boolean equalsAll(int[] arr, int value) {
        for (int v : arr) {
            if (v != value) return false;
        }
        return true;
    }
}
