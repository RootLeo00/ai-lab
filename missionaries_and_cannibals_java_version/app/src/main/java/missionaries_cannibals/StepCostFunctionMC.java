package missionaries_cannibals;

import aima.core.agent.Action;
import aima.core.search.framework.problem.StepCostFunction;

public class StepCostFunctionMC implements StepCostFunction{

    @Override
    public double c(Object s, Action a, Object sDelta) {
        return 1;
    }
    
}
