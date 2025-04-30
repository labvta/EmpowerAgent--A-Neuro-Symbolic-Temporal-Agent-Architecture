def compose_goals(goal_list):
    return " -> ".join(goal_list)

def bidirectional_map(forward_map):
    backward = {}
    for k, vs in forward_map.items():
        for v in vs:
            backward.setdefault(v, set()).add(k)
    return backward
