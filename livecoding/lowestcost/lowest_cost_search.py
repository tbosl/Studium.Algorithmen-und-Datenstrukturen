def lowest_cost_search(start, successors, is_goal, action_cost):
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        state1 = path[-1]
        if is_goal(state1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in successors(state1).items():
            if state not in explored:
                total_cost = pcost + action_cost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return []


def path_cost(path):
    if len(path) < 3:
        return 0
    action, total_cost = path[-2]
    return total_cost

