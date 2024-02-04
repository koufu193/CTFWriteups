package maze;

import java.util.Arrays;
//MazeじゃないかもしれないけどMazeということで...
public class Maze {
    public final int[][] map;
    public static final int MAZE_LENGTH=8;
    public static final Position START_POSITION=new Position(0,0);
    public static final int RENZOKU_MAX=3;

    public Maze(int[][] map){
        if(map.length!=MAZE_LENGTH) throw new IllegalArgumentException(String.format("Maze length must be %d",MAZE_LENGTH));
        this.map=map;
    }
    public int byPosition(Position position){
        return map[position.y()][position.x()];
    }
    public int count(int num){
        int count=0;
        for(int[] m:this.map){
            for(int n:m){
                if(n==num) count++;
            }
        }
        return count;
    }
}
