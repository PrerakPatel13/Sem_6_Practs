from collections import deque

def bfs(graph, source, sink):
    queue = deque([(source, [source])])
    visited = set()
    while queue:
        source, path = queue.popleft()
        visited.add(source)
        for v in range(len(graph[source])):
            if graph[source][v] > 0 and v not in visited:
                new_path = path + [v]
                if v == sink:
                    return new_path
                queue.append((v, new_path))
                visited.add(v)
    return None

def ford_fulkerson(graph, source, sink):
    total_flow = 0
    all_paths = []
    path_flows = []
    while True:
        path = bfs(graph, source, sink)
        if not path:
            break
        path_flow = min(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
        total_flow += path_flow
        all_paths.append(path)
        path_flows.append(path_flow)
    return total_flow, all_paths, path_flows

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

source = 0
sink = 5
total_flow, all_paths, path_flows = ford_fulkerson(graph, source, sink)

print("Maximum flow:", total_flow)
for path, path_flow in zip(all_paths, path_flows):
    print(f"Path: {path}, Flow along path: {path_flow}")
