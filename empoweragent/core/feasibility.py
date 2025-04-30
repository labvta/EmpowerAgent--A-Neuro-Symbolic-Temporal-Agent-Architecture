def check_feasibility(task_graph, current_state, goal):
    return goal in task_graph.get(current_state, [])
