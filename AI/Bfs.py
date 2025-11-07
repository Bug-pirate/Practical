from collections import deque

tree = {
  'A': ['B', 'C'],
  'B': ['D', 'E'],
  'C': ['F', 'G'],
  'D': [],
  'E': [],
  'F': [],
  'G': []
}

start = 'A'
queue = deque()
visited = set()

queue.append(start)
visited.add(start)

def bfs(tree, queue, visited):
    while queue:
        n = queue.popleft()
        print(n)
        for adj in tree[n]:
            if adj not in visited:
                queue.append(adj)
                visited.add(adj)

bfs(tree, queue, visited)

        












# queue = deque()
# visited = set()
# result = []

# start = 'A'
# queue.append("A")
# visited.add(start)
# while queue:
#   current = queue.popleft()
#   result.append(current)

#   for neighbors in graph[current]:
#     if neighbors not in visited:
#       queue.append(neighbors)
#       visited.add(neighbors)

# print(" → ".join(result))
