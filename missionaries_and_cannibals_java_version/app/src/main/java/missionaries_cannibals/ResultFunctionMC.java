package missionaries_cannibals;

import aima.core.agent.Action;
import aima.core.search.framework.problem.ResultFunction;

public class ResultFunctionMC implements ResultFunction {
    @Override
    public Object result(Object s, Action a) {
        int [] state = (int[])s;
         ActionMC action =(ActionMC)a;
    if(state[2]==1) {
        switch (action.getName()) {
            case "M":
                state[0]=-1;

            break;
            case "C":
                state[1]=-1;

                break;
            case "MM":
                state[0]=-2;

                break;
            case "CC":
                state[1]=-2;

                break;
            case "MC":
                state[0]=-1;
                state[1]=-1;

                break;
        }
        state[2]=0;
    }else{
        switch (action.getName()) {
            case "M":
                state[0]=+1;

            break;
            case "C":
                state[1]=+1;

                break;
            case "MM":
                state[0]=+2;

                break;
            case "CC":
                state[1]=+2;

                break;
            case "MC":
                state[0]=+1;
                state[1]=+1;

                break;
        }
        state[2]=1;
        }

    return state;


    }
}
