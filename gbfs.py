import heapq

def gbfs(graph, heuristic, start, goal):
    visited = set()
    pq = []                          # priority queue (heuristic, node, path)
    heapq.heappush(pq, (heuristic[start], start, [start]))

    while pq:
        h, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    pq,
                    (heuristic[neighbour], neighbour, path + [neighbour])
                )

    return None


# Example graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 2,
    'F': 0
}

path = gbfs(graph, heuristic, 'A', 'F')
print("Path found:", path)