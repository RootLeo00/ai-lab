package missionaries_cannibals;

import aima.core.agent.Action;
import aima.core.search.framework.problem.ActionsFunction;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

public class ActionFunctionMC implements ActionsFunction{

    @Override
    public Set<Action> actions(Object s) {
        Set<Action> result = new HashSet<>();
        int [] state = (int[])s;
        System.out.println("expanding state: "+state[0]+":"+state[1]+":"+state[2]);

        if (state[2]==0){ //boat on the left side
            if(state[0]>=1){
                result.add(new ActionMC("M") );
            }
            if(state[1]>=1){
                result.add(new ActionMC("C") );
            }
            if(state[0]>=2){
                result.add(new ActionMC("MM") );
            }
            if(state[1]>=2){
                result.add(new ActionMC("CC") );
            }
            if(state[0]>=1 && state[1]>=1){
                result.add(new ActionMC("MC") );
            }
        }else{ //boat on the right side
            if(3-state[0]>=1 && state[0]<3){ 
                result.add(new ActionMC("M") );
            }
            if(3-state[1]>=1&& state[1]<3){
                result.add(new ActionMC("C") );
            }
            if(3-state[0]>=2&& state[0]<=1){
                result.add(new ActionMC("MM") );
            }
            if(3-state[1]>=2 && state[1]<=1){
                result.add(new ActionMC("CC") );
            }
            if(3-state[0]>=1 && 3-state[1]>=1&& state[0]<3&& state[1]<3){
                result.add(new ActionMC("MC") );
            }
        }
        Iterator i =result.iterator();
        while(i.hasNext()){
            ActionMC a=(ActionMC)i.next();
            System.out.println(a.getName());
        }
        return result;
    }

    
}