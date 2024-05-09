from collections import OrderedDict
def bfs(graph, source, sink):
    paths = []
    queue= OrderedDict()
    queue[source] = [source]
    while queue:
        u, path = queue.popitem(last=False)
        for v, capacity in enumerate(graph[u]):
            if capacity > 0 and v not in path:
                new_path = path + [v]
                if v == sink:
                    paths.append(new_path)
                else:
                    queue[v] = new_path
    return paths
def ford_fulkerson(graph, source, sink):
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
            for i in range(len(path)-1):
                u, v = path[i], path[i+1]
                graph[u][v] -= path_flow
                graph[v][u] += path_flow 
    return all_paths, path_flows
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
all_paths, path_flows = ford_fulkerson(graph, source=0, sink=5)
print("Maximum flow:", sum(path for path in path_flows))
for path,path_flow in zip(all_paths,path_flows):
    print(f"Path:{path}\nFlow along path:{path_flow}")