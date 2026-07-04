import heapq
from copy import deepcopy

goal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

print("Enter the Initial State (Use 0 for Blank):")
initial=[]
for i in range(3):
    row=list(map(int,input(f"Row {i+1}: ").split()))
    initial.append(row)

def heuristic(state):
    h=0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0 and state[i][j]!=goal[i][j]:
                h+=1
    return h

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j]==0:
                return i,j

def get_neighbors(state):
    neighbors=[]
    x,y=find_blank(state)
    moves=[(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in moves:
        nx=x+dx
        ny=y+dy
        if 0<=nx<3 and 0<=ny<3:
            new_state=deepcopy(state)
            new_state[x][y],new_state[nx][ny]=new_state[nx][ny],new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def print_board(state):
    for row in state:
        print(row)
    print()

def a_star():
    priority_queue=[]
    visited=set()
    parent={}
    g_cost={}
    start=state_to_tuple(initial)
    g_cost[start]=0
    parent[start]=None
    heapq.heappush(priority_queue,(heuristic(initial),0,initial))
    while priority_queue:
        f,g,current=heapq.heappop(priority_queue)
        current_tuple=state_to_tuple(current)
        if current_tuple in visited:
            continue
        visited.add(current_tuple)
        if current==goal:
            print("\nGoal Reached!\n")
            path=[]
            while current is not None:
                path.append(current)
                current=parent[state_to_tuple(current)]
            path.reverse()
            print("Solution Path:\n")
            step=0
            for state in path:
                g=step
                h=heuristic(state)
                f=g+h
                print("Step",step)
                print("g =",g,"h =",h,"f =",f)
                print_board(state)
                step+=1
            print("Total Moves =",len(path)-1)
            return
        for neighbor in get_neighbors(current):
            t=state_to_tuple(neighbor)
            new_g=g+1
            if t not in g_cost or new_g<g_cost[t]:
                g_cost[t]=new_g
                parent[t]=current
                new_h=heuristic(neighbor)
                heapq.heappush(priority_queue,(new_g+new_h,new_g,neighbor))
a_star()

