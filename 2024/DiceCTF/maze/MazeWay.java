package maze;

import java.util.*;

public class MazeWay implements Cloneable{
    private final Maze maze;
    private final List<Action> actions=new ArrayList<>();
    private Position nowPosition;
    private int renzokuValue;
    private int renzoku;
    private final Set<Position> beenPositions=new HashSet<>();
    private final Set<Integer> solved=new HashSet<>();
    private final Position startPosition;
    public MazeWay(Maze maze,Position startPosition){
        this.maze=maze;
        this.nowPosition=startPosition;
        this.beenPositions.add(this.nowPosition);
        this.renzokuValue=this.maze.byPosition(this.nowPosition);
        this.renzoku=1;
        this.startPosition=startPosition;
    }

    public Position startPosition() {
        return startPosition;
    }

    public List<Action> actions() {
        return Collections.unmodifiableList(this.actions);
    }

    public Maze maze(){
        return this.maze;
    }
    public Set<Position> beenPositions(){
        return Collections.unmodifiableSet(this.beenPositions);
    }
    public int remaining(int num){
        return (int) (this.maze.count(num)-beenPositions.stream().filter(value->this.maze.byPosition(value)==num).count());
    }
    public void act(Action action){
        if(!ableToGo(action)) throw new IllegalArgumentException("Invalid Action");
        Position newPosition=this.nowPosition.apply(action);
        this.beenPositions.add(newPosition);
        this.nowPosition=newPosition;
        this.actions.add(action);
        int value=this.maze.byPosition(this.nowPosition);
        if(value==renzokuValue){
            renzoku++;
            if(renzoku==Maze.RENZOKU_MAX){
                this.solved.add(this.renzokuValue);
            }
        }
        else{
            this.renzoku=1;
            this.renzokuValue=value;
        }
    }
    public int filledPosition(){
        return walkCount()+1;
    }
    public int walkCount(){
        return this.beenPositions.size()-1;
    }
    public int nowValue(){
        return this.maze.byPosition(this.nowPosition);
    }
    public int renzoku(){
        return this.renzoku;
    }
    public Position now(){
        return this.nowPosition;
    }
    public boolean been(Position position){
        return beenPositions.contains(position);
    }
    public boolean solved(int num){
        return this.solved.contains(num);
    }
    public boolean ableToGo(Action action){
        try{
            Position pos=this.nowPosition.apply(action);
            if(been(pos)) return false;
            if(this.maze.byPosition(pos)==renzokuValue&&Maze.RENZOKU_MAX<(renzoku+1)&&renzokuValue!=-1) return false;
            return true;
        }catch (Exception e){
            return false;
        }
    }

    @Override
    public MazeWay clone() {
        MazeWay clone=new MazeWay(this.maze,startPosition);
        clone.beenPositions.addAll(this.beenPositions);
        clone.actions.addAll(this.actions);
        clone.nowPosition=this.nowPosition;
        clone.solved.addAll(this.solved);
        clone.renzoku=this.renzoku;
        clone.renzokuValue=this.renzokuValue;
        return clone;
    }

    public enum Action{
        RIGHT(1,0),LEFT(-1,0),UP(0,-1),DOWN(0,1);
        public final int x;
        public final int y;
        Action(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}
