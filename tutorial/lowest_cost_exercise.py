def lowest_cost_search(start, successors, is_goal, action_cost):
    """Return the lowest cost path, starting from start state,
    and considering successors(state) => {state:action,...},
    that ends in a state for which is_goal(state) is true,
    where the cost of a path is the sum of action costs,
    which are given by action_cost(action)."""
    explored = set()  # set of states we have visited
    frontier = [[start]]  # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        state1 = final_state(path)
        if is_goal(state1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in successors(state1).items():
            if state not in explored:
                total_cost = pcost + action_cost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return Fail


Fail = []


def path_cost(path):
    "The total cost of a path (which is stored in a tuple with the final action)."
    if len(path) < 3:
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost


def final_state(path):
    return path[-1]


def add_to_frontier(frontier, path):
    "Add path to frontier, replacing costlier path if there is one."
    # (This could be done more efficiently.)
    # Find if there is an old path to the final state of this path.
    old = None
    for i, p in enumerate(frontier):
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return  # Old path was better; do nothing
    elif old is not None:
        del frontier[old]  # Old path was worse; delete it
    ## Now add the new path and re-sort
    frontier.append(path)
    frontier.sort(key=path_cost)


# Successors function (modify based on actual edge weights in your graph)
def successors(state):
    """
    This function should return a dictionary containing the neighboring
    stations reachable from the current state (station) along with the
    corresponding actions (traveling between stations) and their costs
    (based on edge weights in the graph).
    """
    if state == 1:
        return {2: ("travel to 2", 3)}
    elif state == 2:
        return {3: ("travel to 3", 4), 1: ("travel to 1", 2)}
    elif state == 3:
        return {4: ("travel to 4", 1)}
    elif state == 4:
        return {3: ("travel to 3", 2)}
    else:
        return {}  # No successors for destination


# Goal check function
def is_goal(state):
    return state == 4


# Find the lowest cost path
path = lowest_cost_search(1, successors, is_goal,
                          lambda action: action[1])  # action cost is the second element in the tuple

# Print the route taken
if path is not Fail:
    route = []
    for action in path[1:]:  # Skip the starting state (station 1)
        if not isinstance(action, int):
            action, total_cost = action
            route.append(action[0])
    print("Route taken:", " -> ".join(route))
    print(f"Total cost: {total_cost}")
else:
    print("No route found!")
