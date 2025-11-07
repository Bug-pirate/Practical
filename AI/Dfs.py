from collections import deque
def bfs(tree, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.append(node)
            print(node, end=" ")
        
            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [], 'E' : [], 'F' : [], 'G' : []
}
bfs(tree, 'A')