import heapq

def ucs(graph, start, goal):
    visited = set()
    pq = []                      # priority queue (cost, node, path)
    heapq.heappush(pq, (0, start, [start]))

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return path, cost

        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (cost + weight, neighbour, path + [neighbour]))

    return None, float('inf')


# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 3)],
    'F': []
}

path, cost = ucs(graph, 'A', 'F')
print("Path:", path)
print("Cost:", cost)