package challenge;

import java.util.*;

import static challenge.Solver.Action.*;

public class Solver {
    static final int[] DAT_00404020 = {0x04, 0x07, 0x0b, 0x00, 0x20, 0x09, 0x0d, 0x1c, 0x06, 0x15, 0x0d, 0x0d, 0x05, 0x1f, 0x16, 0x14, 0x03, 0x21, 0x07, 0x22, 0x0e, 0x05, 0x1f, 0x07, 0x17, 0x12, 0x0f, 0x0b, 0x10, 0x09, 0x16, 0x07};
    static final int[] KEY_1 = {-1, 0, 1, 0};
    static final int[] KEY_2 = {0, 1, 0, -1};
    static final Action[] actionKey={UP,RIGHT,DOWN,LEFT};
    static final int[] CHAR_KEY_MAP_2 = {1, 2, 3, 2, 3, 3};
    static final int[] CHAR_KEY_MAP_1 = {0, 0, 0, 1, 1, 2};
    static final int FLAG_LENGTH=0x20;
    static final char[] map = new char[36];
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
    }
    public static void main(String[] args) {
        int[] values=new int[FLAG_LENGTH*2];
        Arrays.fill(values,-1);
        Action[] actions=new Action[]{RIGHT, RIGHT, DOWN, LEFT, DOWN, RIGHT, RIGHT, UP, UP, RIGHT, DOWN, DOWN, RIGHT, RIGHT, UP, LEFT, UP, RIGHT, RIGHT, DOWN, DOWN, DOWN, LEFT, DOWN, RIGHT, DOWN, DOWN, DOWN, LEFT, UP, UP, LEFT, LEFT, LEFT, LEFT, DOWN, RIGHT, RIGHT, RIGHT, DOWN, LEFT, LEFT, LEFT, LEFT, LEFT, UP, RIGHT, UP, LEFT, UP, RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, UP, LEFT, LEFT, LEFT, LEFT,LEFT, UP, UP,UP};
        int x=0;
        int y=0;
        int rel_x=0;
        int rel_y=0;
        int prev_rel_x=0;
        int prev_rel_y=-1;
        for (Action action : actions) {
            int number = findNumber(action);
            rel_x = action.x;
            rel_y = action.y;
            System.out.println(calc(x, y));
            values[calc(x, y)] = getNumber(prev_rel_x, prev_rel_y, number);
            x += rel_x;
            y += rel_y;
            prev_rel_x = rel_x;
            prev_rel_y = rel_y;
        }
        System.out.printf("dice{%s}",String.valueOf(toChars(compact(values))));
    }
    private static char[] toChars(int[] arr){
        char[] chars=new char[FLAG_LENGTH];
        for(int i=0;i<FLAG_LENGTH;i++){
            chars[i]=map[arr[i]];
        }
        return chars;
    }
    private static int[] compact(int[] arr){
        int[] result=new int[FLAG_LENGTH];
        for(int i=0;i<FLAG_LENGTH;i++){
            result[i]=arr[i*2]*6+arr[i*2+1];
        }
        for(int i=0;i<FLAG_LENGTH;i++){
            result[i]-=DAT_00404020[i];
            if(result[i]<0){
                result[i]+=0x24;
            }
        }
        return result;
    }
    private static int getNumber(int prev_rel_x,int prev_rel_y,int actionNumber){
        for(int a:findNumbers(actionNumber,CHAR_KEY_MAP_2)){
            if(prev_rel_y+KEY_1[CHAR_KEY_MAP_1[a]]==0&&prev_rel_x+KEY_2[CHAR_KEY_MAP_1[a]]==0) return a;
        }
        for(int a:findNumbers(actionNumber,CHAR_KEY_MAP_1)){
            if(prev_rel_y+KEY_1[CHAR_KEY_MAP_2[a]]==0&&prev_rel_x+KEY_2[CHAR_KEY_MAP_2[a]]==0) return a;
        }
        throw new IllegalArgumentException("Not Found");
    }
    private static int[] findNumbers(int number,int[] keyMap){
        List<Integer> result=new ArrayList<>();
        for(int i=0;i<keyMap.length;i++){
            if(keyMap[i]==number) result.add(i);
        }
        int[] arr=new int[result.size()];
        for(int i=0;i<arr.length;i++){
            arr[i]=result.get(i);
        }
        return arr;
    }
    private static int findNumber(Action action){
        for(int i=0;i< actionKey.length;i++){
            if(actionKey[i]==action) return i;
        }
        throw new IllegalArgumentException("Undefined action:"+action);
    }
    private static int calc(int x,int y){
        return x+y*8;
    }
    enum Action{
        RIGHT(1,0),LEFT(-1,0),UP(0,-1),DOWN(0,1);
        public final int x;
        public final int y;
        Action(int x,int y){
            this.x=x;
            this.y=y;
        }
    }
}
