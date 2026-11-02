# Simple deadlock detection using a Wait-For Graph.
# A directed cycle indicates deadlock in this single-instance model.

graph = {"P1": ["P2"], "P2": ["P1"], "P3": []}

def has_cycle(node, visited, active):
    visited.add(node)
    active.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            if has_cycle(neighbour, visited, active):
                return True
        elif neighbour in active:
            return True
    active.remove(node)
    return False

visited = set()
deadlock = False
for process in graph:
    if process not in visited and has_cycle(process, visited, set()):
        deadlock = True
        break

print("Deadlock Detected" if deadlock else "No Deadlock")
