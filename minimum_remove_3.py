N = int(input())
members = [int(input()) for i in range(N)]
E = int(input())
edges = [tuple(map(int, input().split())) for i in range(E)]
A = int(input())
B = int(input())

graph = {m: set() for m in members}
for (follower, following) in edges:
    graph[follower].add(following)

def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

all_paths = dfs(graph, A, B)

nodes_on_paths = set([node for path in all_paths for node in path])
nodes_on_paths.remove(B)
out = []
for i in members:
    if(i in nodes_on_paths):
        out.append(i)
for i in range(len(out)):
    if i == len(out) - 1:
        print(out[i])
    else:
        print(out[i], end=" ")
