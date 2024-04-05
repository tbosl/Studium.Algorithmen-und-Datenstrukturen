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
    # state is tuple first index is origin, second destination. Index one of inner list
    # are cannibals
    return state == ((0, 0), (3, 3), 'd')


def successors():  # capacities of how large the glasses can be
    def sc(state):
        o, d, boat_position = state
        succs = {}
        if boat_position == 'o':
            succs[((o[0] - 1, o[1] - 1), (d[0] + 1, d[1] + 1), 'd')] = "1 cannibal -> d; 1 missionary -> d"
            succs[((o[0] - 1, o[1]), (d[0] + 1, d[1]), 'd')] = "1 cannibal -> d; 0 missionary -> d"
            succs[((o[0] - 2, o[1]), (d[0] + 2, d[1]), 'd')] = "2 cannibal -> d; 0 missionary -> d"
            succs[((o[0], o[1] - 1), (d[0], d[1] + 1), 'd')] = "0 cannibal -> d; 1 missionary -> d"
            succs[((o[0], o[1] - 2), (d[0], d[1] + 2), 'd')] = "0 cannibal -> d; 2 missionary -> d"
        elif boat_position == 'd':
            succs[((o[0] + 1, o[1] + 1), (d[0] - 1, d[1] - 1), 'o')] = "1 cannibal -> o; 1 missionary -> o"
            succs[((o[0] + 1, o[1]), (d[0] - 1, d[1]), 'o')] = "1 cannibal -> o; 0 missionary -> o"
            succs[((o[0] + 2, o[1]), (d[0] - 2, d[1]), 'o')] = "2 cannibal -> o; 0 missionary -> o"
            succs[((o[0], o[1] + 1), (d[0], d[1] - 1), 'o')] = "0 cannibal -> o; 1 missionary -> o"
            succs[((o[0], o[1] + 2), (d[0], d[1] - 2), 'o')] = "0 cannibal -> o; 2 missionary -> o"

        for state in list(succs.keys()):
            if not __is_valid_state(state):
                del succs[state]
        return succs

    return sc


def __is_valid_state(state):
    o, d, _ö = state
    return (o[0] <= o[1] or o[1] == 0) and (d[0] <= d[1] or d[1] == 0) and d[0] >= 0 and d[1] >= 0 and o[0] >= 0 and o[
        1] >= 0


start_state = ((3, 3), (0, 0), 'o')

res = shortest_path_search(start_state, successors(),
                           lambda state: state == (
                               (0, 0), (3, 3), 'd'))  # inner function will be returned and can access X and Y
print(res)
for r in res:
    print(r)
