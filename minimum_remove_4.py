

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

N = int(input())
members = [int(input()) for i in range(N)]
E = int(input())
edges = [tuple(map(int, input().split())) for i in range(E)]
A = int(input())
B = int(input())
graph = {m: set() for m in members}
for (follower, following) in edges:
    graph[follower].add(following)

paths = find_all_paths(graph, A, B)
to_be_removed = []
new_paths = []
for path in paths:
    flag = True
    for node in path[1:-1]:
        to_be_removed.append(node)
        flag = False
    if flag:
        new_paths.append(path)
if new_paths:
    to_be_removed.append(A)
out = []
for i in members:
    if(i in to_be_removed):
        out.append(i)

out = set(out)

for i in out:
    prit