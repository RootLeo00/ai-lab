/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package main;

import aima.core.search.framework.SearchAgent;
import aima.core.search.framework.problem.*;
import aima.core.search.framework.qsearch.GraphSearch;
import aima.core.search.framework.qsearch.TreeSearch;
import aima.core.search.uninformed.BreadthFirstSearch;
import aima.core.search.uninformed.DepthFirstSearch;
import missionaries_cannibals.ActionFunctionMC;
import missionaries_cannibals.GoalTestMC;
import missionaries_cannibals.ResultFunctionMC;
import missionaries_cannibals.StepCostFunctionMC;

public class App {
 

    public static void main(String[] args) {
        // start problem solution
        int[] initial_state= new int[3];
        initial_state[0]=3;
        initial_state[1]=3;
        initial_state[2]=0;

        Problem problem = new Problem(initial_state, new ActionFunctionMC(), new ResultFunctionMC(), new GoalTestMC(), new StepCostFunctionMC());
        try {
            SearchAgent agent =new SearchAgent(problem,new BreadthFirstSearch(new GraphSearch()));
            // run search agent
            //System.out.println(a.getName());
            System.out.println(agent.getActions()); //getActions() ti da l'array delle azioni che ti porta alla soluzione
            System.out.println(agent.isDone()); //#TODO cos'è isDone()
            
            SearchAgent agent1 =new SearchAgent(problem,new BreadthFirstSearch(new TreeSearch()));
            // run search agent
            //System.out.println(a.getName());
            System.out.println(agent1.getActions());
            System.out.println(agent1.isDone());

            SearchAgent agent2 =new SearchAgent(problem,new DepthFirstSearch(new TreeSearch()));
            // run search agent
            //System.out.println(a.getName());
            System.out.println(agent2.getActions());
            System.out.println(agent2.isDone());
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
