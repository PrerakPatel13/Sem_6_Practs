from collections import deque

def bfs(graph, source, sink):
    paths = []
    queue = deque([(source, [source])])

    while queue:
        u, path = queue.popleft()
        for v, capacity in enumerate(graph[u]):
            if capacity > 0 and v not in path:
                if v == sink:
                    paths.append(path + [v])
                else:
                    queue.append((v, path + [v]))
    return paths

def modify_graph(graph, path, flow):
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        graph[u][v] -= flow
        graph[v][u] += flow  
    return graph

def ford_fulkerson(graph, source, sink):
    n = len(graph)
    max_flow = 0
    all_paths = []
    path_flows = []

    while True:
        paths = bfs(graph, source, sink)
        if not paths:
            break

        for path in paths:
            path_flow = min(graph[path[i]][path[i+1]] for i in range(len(path)-1))
            all_paths.append(path)
            path_flows.append(path_flow)

            max_flow += path_flow
            graph = modify_graph(graph, path, path_flow)

    return max_flow, all_paths, path_flows

graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

source = 0
sink = 5
max_flow, all_paths, path_flows = ford_fulkerson(graph, source, sink)

print("Maximum flow:", max_flow)
print("All augmenting paths and their corresponding flows:")
for i, path in enumerate(all_paths):
    print("Path:", path)
    print("Flow along path:", path_flows[i])
