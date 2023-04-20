import sys
from aima import search
from mc_problem import MCProblem

problem = MCProblem()
soln= search.breadth_first_graph_search(problem)
print("solution ", soln)
print("ROUND\t\tRIVER")
river=[]
for s in enumerate(soln.path()):
    missionaires_left=""
    cannibals_left=""
    missionaires_right=""
    cannibals_right=""

    #left side
    for _ in range(s[1].state[1]):
        cannibals_left+="🐺"
    #add space to align with missionaires
    for _ in range(3-s[1].state[1]):
        cannibals_left+="  "
    for _ in range(s[1].state[0]):
        missionaires_left+="🐑"
    #add space to align with missionaires
    for _ in range(3-s[1].state[0]):
        missionaires_left+="  "

    #right side
    for _ in range(3-s[1].state[1]):
        cannibals_right+="🐺"
    #add space to align with missionaires
    for _ in range(s[1].state[1]):
        cannibals_right+="  "
    for _ in range(3-s[1].state[0]):
        missionaires_right+="🐑"
    #add space to align with missionaires
    for _ in range(s[1].state[0]):
        missionaires_right+="  "
    if s[1].state[2]:
        boat="🌊⛵️<~~~~~~~"
    else:
        boat="~~~~~~~>⛵️🌊"
    
    river.append([s[0],missionaires_left, cannibals_left, boat, missionaires_right, cannibals_right])

for row in river:
    print('| {:^2} | {:^} | {:^} | {:^} | {:^} | {:^} |'.format(*row))
    # print(s[0], "\t", missionaires_left+cannibals_left,"\t\t",boat,"\t\t", missionaires_right+cannibals_right)



