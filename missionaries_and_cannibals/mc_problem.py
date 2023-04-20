import sys
sys.path.insert(1, "../aima-python")
# import search4e
from search import Problem


class MCProblem(Problem):
    def __init__(self,
                initial=tuple([3,3,True]),
                goal=tuple([0,0,False])):
        Problem.__init__(self,initial,goal)
    
    def actions(self, state):
        print("[action()] state =", state)
        state=list(state)
        if len(state)==0: 
            print ("DEAD END")
            return ()
        result=[]
        if state[2] : #barca a sx -> prelevo 
            if state[0] >= 1: #se ci sono almeno 1 missionario
                result.append("M")
            if state[1] >= 1: #se ci sono almeno 1 cannibale
                result.append("C")
            if state[0] >= 2: #se ci sono almeno 2 missionari
                result.append("MM")
            if state[1] >= 2: #se ci sono almeno 2 cannibali
                result.append("CC")
            if state[0] >= 1 and state[1] >= 1:
                result.append("MC")
        else: #barca a dx -> faccio scendere
            if 3-state[0] >= 1: #se ci sono almeno 1 missionario
                result.append("M")
            if 3-state[1] >= 1: #se ci sono almeno 1 cannibale
                result.append("C")
            if 3-state[0] >= 2: #se ci sono almeno 2 missionari
                result.append("MM")
            if 3-state[1] >= 2: #se ci sono almeno 2 cannibali
                result.append("CC")
            if 3-state[0] >= 1 and 3-state[1] >= 1:
                result.append("MC")
        print("actions ", result)
        return tuple(result)
    
    def result(self, state, action):
        print("[result()] action=", action)
        state=list(state)
        result = state[:]
        if state[2] : #barca a sx -> prelevo
            print("barca a sinistra")
            if action =="M":
                result[0] -= 1
            elif action == "C":
                result[1] -= 1
            elif action == "MM":
                result[0] -= 2
            elif action == "CC":
                result[1] -= 2
            elif action == "MC":
                result[0] -= 1
                result[1] -= 1
        else: #barca a dx -> faccio scendere
            print("barca a destra")
            if action == "M":
                result[0] += 1
            elif action == "C":
                result[1] += 1
            elif action == "MM":
                result[0] += 2
            elif action == "CC":
                result[1] += 2
            elif action == "MC":
                result[0] += 1
                result[1] += 1
        result[2] = not result[2]
        if result[0] < result[1] and result[0] != 0:
            return ()
        if 3-result[0] < 3-result[1] and 3-result[0] != 0:
            return ()
        print("result ", result)
        return tuple(result)
    
