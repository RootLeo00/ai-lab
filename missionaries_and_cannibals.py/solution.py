import sys
from aima import search
from mc_problem import MCProblem

problem = MCProblem()
soln= search.breadth_first_graph_search(problem)
print("solution ", soln)
for s in enumerate(soln.path()):
    print(s)


