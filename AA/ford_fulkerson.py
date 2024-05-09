def dfs(graph, source, sink, visited, path):
    visited[source] = True
    if source == sink:
        return path
    for v in range(len(graph[source])):
        if not visited[v] and graph[source][v] > 0:
            result = dfs(graph, v, sink, visited, path + [v])
            if result:
                return result
    return None
def ford_fulkerson_dfs(graph, source, sink):
    all_paths = []
    path_flows = []
    while True:
        path = dfs(graph, source, sink, [False]* len(graph), [source])
        if path is None:
            break
        path_flow = min(graph[path[i]][path[i + 1]] for i in range(len(path) - 1))
        all_paths.append(path)
        path_flows.append(path_flow)
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
    return all_paths, path_flows
graph = [[0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]]
all_paths, path_flows = ford_fulkerson_dfs(graph, source=0, sink=5)
print("Maximum flow:", sum(path for path in path_flows))
for path,path_flow in zip(all_paths,path_flows):
    print(f"Path:{path}\nFlow along path:{path_flow}")