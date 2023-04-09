from collections import defaultdict

def build_graph(n, edges):
    graph = defaultdict(list)
    for i in range(n):
        graph[i+1] = []
    for edge in edges:
        graph[edge[0]].append(edge[1])
    return graph

def dfs(graph, visited, start, end):
    if start == end:
        return True
    visited[start] = True
    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, visited, neighbor, end):
                return True
    return False

n = int(input())
members = [int(input()) for i in range(n)]
e = int(input())
edges = [list(map(int, input().split())) for i in range(e)]
graph = build_graph(n, edges)
visited = {}
follower = int(input())
following = int(input())
if dfs(graph, visited, follower, following):
    print(1)
else:
    print(0)