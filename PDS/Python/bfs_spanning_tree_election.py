from collections import deque

N, M, S = map(int, input().split())
ids = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [-1] * N
parent[S] = -2
queue = deque([S])
edges = []
print(f"Building spanning tree from P{S} using BFS:")
while queue:
    u = queue.popleft()
    for v in graph[u]:
        if parent[v] == -1:
            parent[v] = u
            queue.append(v)
            edges.append((u, v))
            print(f"  Tree edge: P{u} -^> P{v} added")

print(f"Spanning tree built: {len(edges^)} edges")
print("Parent array:", end=" ")
for i in range(N):
    p = "none" if i == S else (f"P{parent[i]}" if parent[i] != -1 else "unreachable")
    print(f"P{i}.parent={p}", end=" ")
print()

children = [[] for _ in range(N)]
for u, v in edges:
    children[u].append(v)
print(f"Tree election started at root P{S}")

def elect(u):
    for v in children[u]:
        print(f"P{u} sends ELECT to P{v}")
    for v in children[u]:
        elect(v)
elect(S)

def echo(u):
    winner = u
    for v in children[u]:
        w = echo(v)
        if ids[w] > ids[winner]:
            winner = w
    if u != S:
        print(f"P{u} sends ECHO(ID={ids[winner]}) to P{parent[u]}")
    return winner

winner = echo(S)
print(f"P{S} collected all ECHOs: max ID={ids[winner]}")
print(f"Election result: P{winner} (ID={ids[winner]}) is the new coordinator")
