package maze;

public record Position(int x,int y){
    public Position{
        if(x<0||Maze.MAZE_LENGTH<=x) throw new IllegalArgumentException(String.format("x must be between %d and %d",0,Maze.MAZE_LENGTH));
        if(y<0||Maze.MAZE_LENGTH<=y) throw new IllegalArgumentException(String.format("y must be between %d and %d",0,Maze.MAZE_LENGTH));
    }
    public Position apply(MazeWay.Action action){
        return new Position(this.x+action.x,this.y+action.y);
    }
}
