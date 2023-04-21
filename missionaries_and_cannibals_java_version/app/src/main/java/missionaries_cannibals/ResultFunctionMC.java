package missionaries_cannibals;

import aima.core.agent.Action;
import aima.core.search.framework.problem.ResultFunction;

public class ResultFunctionMC implements ResultFunction {
    @Override
    public Object result(Object s, Action a) {
        int [] state = (int[])s;
        int [] result = new int[3];
        result[0]=state[0];
        result[1]=state[1];
        result[2]=state[2];
         ActionMC action =(ActionMC)a;
         System.out.println("from state: "+state[0]+":"+state[1]+":"+state[2]+" action: "+action.getName());
        
    if(state[2]==0) {
        switch (action.getName()) {
            case "M":
                result[0]-=1;

            break;
            case "C":
                result[1]-=1;

                break;
            case "MM":
                result[0]-=2;

                break;
            case "CC":
                result[1]-=2;

                break;
            case "MC":
                result[0]-=1;
                result[1]-=1;

                break;
        }
    }else{
        switch (action.getName()) {
            case "M":
                result[0]+=1;

            break;
            case "C":
                result[1]+=1;

                break;
            case "MM":
                result[0]+=2;

                break;
            case "CC":
                result[1]+=2;

                break;
            case "MC":
                result[0]+=1;
                result[1]+=1;

                break;
        }
        
        }
        if(state[2]==1){
            result[2]=0;

        }else{
            result[2]=1;
        }

    return result;


    }
}
