import heapq

def shortest_path(network, A, B):
    t = {member: float('inf') for member in network}
    t[A] = 0
    pq = [(0, A)]
    while pq:
        curr_distance, curr_node = heapq.heappop(pq)
        if curr_distance > t[curr_node]:
            continue
        for neighbor, weight in network[curr_node].items():
            distance = curr_distance + weight
            if distance < t[neighbor]:
                t[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    print(t[B])

MEMBERS = {}
N = int(input())
for i in range(N):
    value = input()
    MEMBERS[value] = int(value)

network = {member: {} for member in MEMBERS}
e = int(input())
for i in range(e):
    f, t, d = input().split()
    network[f][t] = int(d)

A = input().split()[0]
B = input().split()[0]

shortest_path(network, A, B)
