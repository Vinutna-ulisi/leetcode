import matplotlib.pyplot as plt
import heapq

ROWS, COLS = 10, 10
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

obstacles = [(1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5), (5, 5), (5, 6), (6, 6)]

for r, c in obstacles:
    grid[r][c] = 1

start, goal = (0, 0), (9, 9)

def get_neighbors(pos):
    neighbors = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for dr, dc in directions:
        nr, nc = pos[0] + dr, pos[1] + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0:
            neighbors.append((nr, nc))
    return neighbors

def dijkstra(start, goal):
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        cost, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor in get_neighbors(current):
            new_cost = cost_so_far[current] + 1 
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))
                came_from[neighbor] = current  

    return reconstruct_path(came_from, goal)

def reconstruct_path(came_from, end):
    if end not in came_from:
        return None
    path = []
    while end:
        path.append(end)
        end = came_from[end]
    return path[::-1]

def draw_path(path, title):
    grid_copy = [row[:] for row in grid]
    if path:
        for r, c in path:
            grid_copy[r][c] = 2
    for r, c in obstacles:
        grid_copy[r][c] = 1
    grid_copy[start[0]][start[1]] = 3  
    grid_copy[goal[0]][goal[1]] = 4    

    cmap = plt.cm.get_cmap('Accent', 5)
    plt.imshow(grid_copy, cmap=cmap, origin='upper')
    plt.title(title)
    plt.colorbar(ticks=[0, 1, 2, 3, 4], label='Legend\n0-Free\n1-Obstacle\n2-Path\n3-Start\n4-Goal')
    plt.clim(-0.5, 4.5)
    plt.grid(True)
    plt.show()

path_dijkstra = dijkstra(start, goal)
draw_path(path_dijkstra, 'Dijkstra’s Shortest Path (New Obstacles)')
