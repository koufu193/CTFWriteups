package maze;

import java.util.Arrays;
//遅いSolver
public class MazeSolver {
    public static void main(String[] args) {
        int[][] map=new int[][]
                {{0, 0, 0, 0, 1, 1, 2, 2},
                {-1, 3, 4, 4, 1, 2, 2, 2},
                {-1, 3, 3, 4, 1, 5, 5, 5},
                {-1, 3, 4, 4, 4, 5, 5, 5},
                {6, 6, 6, 7, 7, 7, 7,-1},
                {8, 6, 9, 9,10,10,10,10},
                {8, 6, 9,11,11,11,-1,12},
                {8, 8, 9, 9,11,12,12,12}};
        Maze maze=new Maze(map);
        MazeWay def=new MazeWay(maze,Maze.START_POSITION.apply(MazeWay.Action.DOWN));
        def.act(MazeWay.Action.UP);
        def.act(MazeWay.Action.RIGHT);
        def.act(MazeWay.Action.RIGHT);
        start(def);
    }
    private static void start(MazeWay defaultWay){
        int nowValue=defaultWay.nowValue();
        if(64<=defaultWay.filledPosition()){
            System.out.println(defaultWay.actions());
            printMap(defaultWay);
        }
        for(MazeWay.Action action:MazeWay.Action.values()){
            if(!defaultWay.ableToGo(action)) continue;
            if(nowValue!=-1&&defaultWay.remaining(nowValue)<Maze.RENZOKU_MAX&&
                    !defaultWay.solved(nowValue)&&
                    defaultWay.maze().byPosition(defaultWay.now().apply(action))!=nowValue) continue;
            MazeWay newMaze=defaultWay.clone();
            newMaze.act(action);
            start(newMaze);
        }
    }
    private static void printMap(MazeWay maze){
        char[][] z=new char[8][8];
        for(char[] o:z){
            Arrays.fill(o,'□');
        }
        Position now=maze.startPosition();
        for(MazeWay.Action a:maze.actions()){
            z[now.y()][now.x()]=kigo(a);
            now=now.apply(a);
        }
        for (char[] o:z){
            System.out.println(o);
        }
        System.out.println();
    }
    private static char kigo(MazeWay.Action action){
        return switch (action){
            case RIGHT -> '→';
            case DOWN -> '↓';
            case LEFT -> '←';
            case UP->'↑';
        };
    }
}
