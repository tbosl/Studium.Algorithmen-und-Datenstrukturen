def shortest_path_search(start, successors, is_goal):
    if is_goal(start):
        return [start]
    frontier = [[start]]
    explored = set([start])
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []


def is_goal(state):
    return state == (6, 0)  # state is tuple of water levels of left and right glas.


def successors(X, Y):  # capacities of how large the glasses can be
    def sc(state):
        x, y = state
        assert x <= X and y <= Y  # could also check that x and y are non-negative
        return {
            (X, y): 'fill x',  # fill left glass to entirety but don't touch right glass
            (x, Y): 'fill y',
            (0, y): 'empty x',
            (x, 0): 'empty y',
            (0, y + x) if y + x <= Y else (x - (Y - y), Y): 'x->y',
            (x + y, 0) if x + y <= X else (X, y - (X - x)): 'y<-x'
        }

    return sc


start_state = (0, 0)
res = shortest_path_search(start_state, successors(418, 986),
                           lambda state: state == (6, 0))  # inner function will be returned and can access X and Y
print(res)
print('%s transitions' % (int(len(res) / 2)))
