package missionaries_cannibals;

import aima.core.search.framework.problem.GoalTest;

public class GoalTestMC implements GoalTest {
    @Override
    public boolean isGoalState(Object state) {
        int [] s = (int[])state;
        return (s[0]==0 && s[1]==0 && s[2]==1 );
    }
}
