import numpy as np
from collections import deque

def flood_fill_border_zero_to_two(grid):
    grid = np.array(grid)
    rows, cols = grid.shape
    # Utwórz macierz wynikową
    result = grid.copy()
    # Kolejka do BFS
    q = deque()
    visited = np.zeros_like(grid, dtype=bool)

    # Dodaj wszystkie krawędziowe zero do kolejki
    for r in range(rows):
        for c in range(cols):
            if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and grid[r][c] == 0:
                q.append((r, c))
                visited[r][c] = True
    
    # BFS
    while q:
        r, c = q.popleft()
        result[r][c] = 2
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    q.append((nr, nc))
                    visited[nr][nc] = True

input_grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

output = flood_fill_border_zero_to_two(input_grid)
print(output)