from collections import deque

def find_min_nodes_to_remove(nodes, edges, start_node, end_node):
    node_to_index = {nodes[i]: i for i in range(len(nodes))}
    graph = [[] for _ in range(len(nodes))]
    for f, t in edges:
        i, j = node_to_index[f], node_to_index[t]
        graph[i].append(j)
        graph[j].append(i)
    
    q = deque()
    q.append(node_to_index[start_node])
    visited = set()
    while q:
        node = q.popleft()
        if nodes[node] == end_node:
            return list(visited)
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                q.append(neighbor)
    return -1
n = int(input())
nodes = []
for i in range(n):
    nodes.append(int(input()))
e = int(input())
edges = []
for i in range(e):
    f, t = map(int, input().split())
    edges.append((f, t))
a = int(input())
b = int(input())

result = find_min_nodes_to_remove(nodes, edges, a, b)
print(nodes[result[0]],nodes[result[1]])
