import numpy as np
from state import next_state, solved_state
from location import next_location, solved_location
from collections import OrderedDict
import heapq as hp


def solve(init_state, init_location, method):
    """
    Solves the given Rubik's cube using the selected search algorithm.
 
    Args:
        init_state (numpy.array): Initial state of the Rubik's cube.
        init_location (numpy.array): Initial location of the little cubes.
        method (str): Name of the search algorithm.
 
    Returns:
        list: The sequence of actions needed to solve the Rubik's cube.
    """

    # instructions and hints:
    # 1. use 'solved_state()' to obtain the goal state.
    # 2. use 'next_state()' to obtain the next state when taking an action .
    # 3. use 'next_location()' to obtain the next location of the little cubes when taking an action.
    # 4. you can use 'Set', 'Dictionary', 'OrderedDict', and 'heapq' as efficient data structures.

    expand = [0]
    explored = [0]

    if method == 'Random':
        return list(np.random.randint(1, 12+1, 10))
    
    elif method == 'IDS-DFS':
        limit = 1
        def dfs(n):
            current_state = init_state
            solution = []
            stack = []
            stack.append((current_state, []))
            while len(stack):
                current_state = stack[-1][0]
                solution = stack[-1][1]
                stack.pop()
                expand[0] += 1
                if np.array_equal(current_state, solved_state()):
                    return np.array(solution)
                
                if len(solution) < n:
                    for i in range(12, 0, -1):
                        stack.append((next_state(current_state, i), (solution + [i])))
                        explored[0] += 1
                
            return np.array([0])
        while True:
            ans = dfs(limit)
            if not np.array_equal(ans, np.array([0])):
                print('expand: ', expand[0])
                print('explored: ', explored[0])
                return ans
            limit += 1
    
    elif method == 'A*':
        def heuristic(array):
            d1 = {}
            d2 = {}
            sum = 0
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        d1.update({array[x][y][z] : (x, y, z)})
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        d2.update({solved_location()[x][y][z] : (x, y, z)})

            for i in range(1, 9):
                sum += (abs(d1[i][0] - d2[i][0]) + abs(d1[i][1] - d2[i][1]) + abs(d1[i][2] - d2[i][2]))
            return sum / 4
        
        
        current_state = init_state
        current_location = init_location
        solution = []
        heap = []
        count = 0
        hp.heappush(heap, ((len(solution) + heuristic(current_location)), count, current_state, current_location, solution))
        visited = set()
        while True:
            visited.add(str(current_state))
            current_state = heap[0][2]
            current_location = heap[0][3]
            solution = heap[0][4]
            hp.heappop(heap)
            expand[0] += 1
            if np.array_equal(current_state, solved_state()):
                print('expand: ', expand[0])
                print('explored: ', count)
                return np.array(solution)
            
            for i in range(1, 13):
                nloc = next_location(current_location, i)
                nstate = next_state(current_state, i)
                count += 1
                if str(nstate) not in visited:
                    hp.heappush(heap, ((len(solution) + heuristic(nloc) + 1), count, nstate, nloc, (solution + [i])))
               

    elif method == 'BiBFS':

        def str_to_numpy_array(s):
            l = []
            count = 0
            pair = []
            for i in s:
                if i in {'1','2','3','4','5','6'} :
                    if count % 2 == 0:
                        pair.append(int(i))
                    else:
                        pair.append(int(i))
                        l.append(pair)
                        pair = [] 
                    count += 1
            return np.array(l)
        
        current_state_s = init_state
        current_state_d = solved_state()
        solution_s = []
        solution_d = []
        queue_s = OrderedDict()
        queue_d = OrderedDict()
        queue_s.update({str(current_state_s): []})
        queue_d.update({str(current_state_d): []})
        while True:
            for x, y in queue_s.items():
                current_state_s = str_to_numpy_array(x)
                solution_s = y
                break
            for x, y in queue_d.items():
                current_state_d = str_to_numpy_array(x)
                solution_d = y
                break

            queue_s.popitem(last=False)
            queue_d.popitem(last=False)
            
            expand[0] += 2
            
            for i in range(1, 13):
                nstate = str(next_state(current_state_s, i))
                queue_s.update({nstate: (solution_s + [i])})
                explored[0] += 1
                if nstate in queue_d.keys():
                    print('expand: ', expand[0])
                    print('explored: ', explored[0])
                    r = solution_s + [i]
                    s = queue_d[nstate]
                    t = []
                    for j in range(len(s) - 1, -1, -1):
                        new = (s[j] + 6) % 12
                        if new == 0:
                            t += [12]
                        else:
                            t += [new]
                    return np.array(r + t)
            for i in range(1, 13):
                nstate = str(next_state(current_state_d, i))
                queue_d.update({nstate: (solution_d + [i])})
                explored[0] += 1
                if nstate in queue_s.keys():
                    print('expand: ', expand[0])
                    print('explored: ', explored[0])
                    r = queue_s[nstate]
                    s = solution_d + [i]
                    t = []
                    for j in range(len(s) - 1, -1, -1):
                        new = (s[j] + 6) % 12
                        if new == 0:
                            t += [12]
                        else:
                            t += [new]

                    return np.array(r + t)    
    
    else:
        return []
