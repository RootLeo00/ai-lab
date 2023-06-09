from aima import search
from mc_problem import MCProblem
import time

def run():
    problem = MCProblem()
    start_time=time.time()
    soln= search.breadth_first_graph_search(problem)
    print("Time taken: ", time.time()-start_time, "seconds")
    return soln

def pretty_print(soln):
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



#main
if __name__ == "__main__":
    soln=run()
    pretty_print(soln)