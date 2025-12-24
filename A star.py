import heapq

def astar(start, goal, neighbors_fn, heuristic_fn):
    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor in neighbors_fn(current):
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_fn(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    if goal not in came_from:
        return None, float('inf')

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()
    return path, cost_so_far[goal]


# ---- REQUIRED TEST CODE ----
def neighbors(n):
    return [n - 1, n + 1]

def heuristic(a, b):
    return abs(a - b)

path, cost = astar(0, 5, neighbors, heuristic)
print("Path:", path)
print("Cost:", cost)
