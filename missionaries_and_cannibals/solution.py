import sys
from aima import search
from mc_problem import MCProblem

problem = MCProblem()
soln= search.breadth_first_graph_search(problem)
print("solution ", soln)
print("ROUND\tLEFT SIDE STATE")
for s in enumerate(soln.path()):
    missionaires_left=""
    cannibals_left=""
    missionaires_right=""
    cannibals_right=""
    for _ in range(s[1].state[1]):
        cannibals_left+="🐺"
    for _ in range(s[1].state[0]):
        missionaires_left+="🐑"
    for _ in range(3-s[1].state[1]):
        cannibals_right+="🐺"
    for _ in range(3-s[1].state[0]):
        missionaires_right+="🐑"
    if s[1].state[2]:
        boat="⛵️⬅️⬅️⬅️"
    else:
        boat="➡️➡️➡️⛵️"
    print(s[0], "\t", missionaires_left,"\t",cannibals_left,"\t",boat,"\t", missionaires_right,"\t",cannibals_right)



