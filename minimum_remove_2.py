from collections import deque

# function to find the shortest path from A to B in the network
def find_shortest_path(graph, A, B):
    visited = set()
    queue = deque([(A, [A])])
    while queue:
        (node, path) = queue.popleft()
        if node == B:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))
    return None

# read input
N = int(input())
members = [int(input()) for i in range(N)]
E = int(input())
edges = [tuple(map(int, input().split())) for i in range(E)]
A = int(input())
B = int(input())

# build the network graph
graph = {m: set() for m in members}
for (follower, following) in edges:
    graph[follower].add(following)

print(graph)

# find the shortest path from A to B
path = find_shortest_path(graph, A, B)

# output the result
if path is not None:
    nodes_to_remove = set(path[1:-1])
    print(" ".join(str(node) for node in nodes_to_remove))
else:
    print("")
