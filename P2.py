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

def dfs(graph, start):
    visited = []
    stack = []

    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

    print(visited)

choice = builtins.input("Choose graph (1 or 2): ")

if choice == "1":
    start = builtins.input("Enter start node: ").strip().upper()
    dfs(graph, start)
elif choice == "2":
    start = builtins.input("Enter start node: ").strip()
    dfs(graph2, start)
else:
    print("Invalid graph choice")
