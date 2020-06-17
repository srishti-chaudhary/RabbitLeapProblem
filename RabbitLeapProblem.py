
import time
import random

class State():
    def __init__(self, state):
        self.state = state
        self.parent = None

    def is_goal(self):
        if self.state == [2,2,2,0,1,1,1]:
            return True
        else:
            return False


def swap(state,x,y):
    newState = []
    for i in state:
        newState.append(i)
    newState[x] = newState[y]
    newState[y] = 0
    return newState

def next_states(curr_state):
    states = []
    index = curr_state.state.index(0)

    possible_index_1 = [index-1, index-2]
    possible_index_2 = [index+1, index+2]

    for i in possible_index_1:
        new_state = State([])
        if i >= 0 and i <= 6 and curr_state.state[i] == 1:
            new_state.state = swap(curr_state.state, index, i)
            states.append(new_state)
            new_state.parent = curr_state
    
    for i in possible_index_2:
        new_state = State([])
        if i >= 0 and i <= 6 and curr_state.state[i] == 2:
            new_state.state = swap(curr_state.state, index, i)
            states.append(new_state)
            new_state.parent = curr_state
    
    random.shuffle(states) 
    return states

def bfs():
    init_state = State([1,1,1,0,2,2,2])

    if init_state.is_goal():
        return init_state
    
    frontier = list()
    explored = set()

    frontier.append(init_state)
    while frontier:
        curr_state = frontier.pop(0)
        if curr_state.is_goal():
            return curr_state

        explored.add(curr_state)
        nodes = []
        nodes = next_states(curr_state)
        for n in nodes:
            if (n not in explored) or (n not in frontier):
                frontier.append(n)


    return None

def dfs():
    init_state = State([1,1,1,0,2,2,2])

    if init_state.is_goal():
        return init_state
    
    frontier = list()
    explored = set()

    frontier.append(init_state)
    while frontier:
        curr_state = frontier.pop()
        if curr_state.is_goal():
            return curr_state

        explored.add(curr_state)
        nodes = []
        nodes = next_states(curr_state)
        for n in nodes:
            if (n not in explored) or (n not in frontier):
                frontier.append(n)


    return None

def print_path(solution):

    path=[]
    path.append(solution)
    Parent = solution.parent
    while Parent:
        path.append(Parent)
        Parent = Parent.parent

    for n in range(len(path)):
        s = path[len(path)-n-1]
        print (s.state)


times = 20

time_bfs = 0
time_dfs = 0

for i in range(times):
    start = 0
    end = 0
    start = time.time()
    s1 = bfs()
    end = time.time()
    time_bfs = time_bfs + (end - start)


print ('USING BFS')
print_path(s1)

print('Time taken when using BFS: ' + str(time_bfs/times))

for i in range(times):
    start = 0
    end = 0
    start = time.time()
    s2 = dfs()
    end = time.time()
    time_dfs = time_dfs + (end-start)

print('USING DFS')
print_path(s2)

print('Time taken when using DFS: ' + str(time_dfs/times))

