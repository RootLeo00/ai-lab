package missionaries_cannibals;

import aima.core.agent.Action;

public class ActionMC implements Action{
    private String name;
    public ActionMC(String name){
        this.name=name;
    }
    public String getName(){
        return this.name;
    }
    @Override
    public boolean isNoOp() {
        return false;
    }
}