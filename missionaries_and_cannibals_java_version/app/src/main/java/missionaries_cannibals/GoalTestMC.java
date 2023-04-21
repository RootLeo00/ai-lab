package missionaries_cannibals;

import aima.core.search.framework.problem.GoalTest;

public class GoalTestMC implements GoalTest {
    @Override
    public boolean isGoalState(Object state) {
        int [] s = (int[])state;
        //System.out.println("testing state: "+s[0]+":"+s[1]+":"+s[2]);
        if(s[0]==0 && s[1]==0 && s[2]==1)
        return true;
        else
        return false;
    }
}
