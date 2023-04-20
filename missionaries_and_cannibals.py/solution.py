import sys
from aima import search
from mc_problem import MCProblem

problem = MCProblem()
soln= search.breadth_first_graph_search(problem)
print("solution ", soln)



