import sys
from aima import search
# sys.path.insert(1, '../aima-python')
# import search4e
# from search import breadth_first_tree_search, path
from mc_problem import MCProblem

problem = MCProblem()
soln= search.breadth_first_tree_search(problem)
print(soln)
# print("Cost: ", soln.path_cost)
# path = search.path_states(soln)
# print(path)


