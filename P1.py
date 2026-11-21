from collections import deque
import builtins

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph2 = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

def bfs(graph, start):
    if start not in graph:
        print("Invalid start node")
        return

    visited = []
    queue = deque([start])
    visited.append(start)

    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    print("BFS Traversal:", visited)

choice = builtins.input("Choose graph (1 or 2): ")

if choice == "1":
    start = builtins.input("Enter start node (A-F): ").strip().upper()
    bfs(graph, start)
elif choice == "2":
    start = builtins.input("Enter start node (1-7): ").strip()
    bfs(graph2, start)
else:
    print("Invalid graph choice")
