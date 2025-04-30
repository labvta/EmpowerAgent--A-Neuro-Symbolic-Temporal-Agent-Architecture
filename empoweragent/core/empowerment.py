def compute_empowerment(transition_model, state, horizon=2):
    visited = set()
    frontier = [state]
    for _ in range(horizon):
        next_frontier = []
        for s in frontier:
            successors = transition_model.get_successors(s)
            next_frontier.extend(successors)
        visited.update(next_frontier)
        frontier = next_frontier
    return len(visited)
