from collections import deque

def bfs(graph, source, sink):
    # Perform BFS to find a single augmenting path from source to sink
    queue = deque([(source, [source])])
    visited = set()
    while queue:
        current_node, path = queue.popleft()
        visited.add(current_node)
        for neighbor in range(len(graph[current_node])):
            if graph[current_node][neighbor] > 0 and neighbor not in visited:
                # If there is available capacity and neighbor has not been visited
                new_path = path + [neighbor]
                if neighbor == sink:
                    return new_path
                queue.append((neighbor, new_path))
                visited.add(neighbor)
    return None  # Return None if no augmenting path is found

def ford_fulkerson(graph, source, sink):
    total_flow = 0
    all_paths = []
    path_flows = []
    
    while True:
        path = bfs(graph, source, sink)
        if not path:
            break
        
        # Calculate the flow through the path
        path_flow = min(graph[path[i]][path[i+1]] for i in range(len(path)-1))
        
        # Update the graph based on the path flow
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
        
        total_flow += path_flow
        all_paths.append(path)
        path_flows.append(path_flow)
    
    return total_flow, all_paths, path_flows

# Example usage:
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
