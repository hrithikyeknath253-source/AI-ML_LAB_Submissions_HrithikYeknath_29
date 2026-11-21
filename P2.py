graph_astar = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 1},
    'D': {'G': 3},
    'E': {'G': 1},
    'F': {'G': 5},
    'G': {}
}

heuristic_astar = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 3,
    'G': 0
}

open_list = []
start = 'A'
goal = 'G'

def astar(graph, heuristic, start, goal):
  open_list.append(start)
  cost = {start:0}
  while open_list:
    current = open_list[0]
    for node in open_list:
      if cost[node] + heuristic[node] < cost[current] + heuristic[current]:
        current = node
    if current == goal:
        print ("Goal node found!")
        return
    open_list.remove(current)
    for neighbour in graph[current]:
          if neighbour not in cost:
            cost[neighbour] = cost[current] + graph[current][neighbour]
            open_list.append(neighbour)
astar(graph_astar, heuristic_astar, start, goal)
