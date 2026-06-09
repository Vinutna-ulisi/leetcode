import matplotlib.pyplot as plt 
import heapq 

ROWS, COLS = 10, 10 
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)] 
obstacles = [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (5, 6), (5, 5), (5, 4)] 
for r, c in obstacles: 
    grid[r][c] = 1 
start, goal = (0, 0), (9, 9) 
def heuristic(a, b): 
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 
def get_neighbors(pos): 
    neighbors = [] 
    directions = [(0,1),(1,0),(-1,0),(0,-1)] 
    for dr, dc in directions: 
        nr, nc = pos[0] + dr, pos[1] + dc 
        if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0: 
            neighbors.append((nr, nc)) 
    return neighbors 
def greedy_search(start, goal): 
    frontier = [(heuristic(start, goal), start)] 
    came_from = {start: None} 
    while frontier: 
        _, current = heapq.heappop(frontier) 
        if current == goal: 
            break 
        for neighbor in get_neighbors(current): 
            if neighbor not in came_from: 
                came_from[neighbor] = current 
                heapq.heappush(frontier, (heuristic(neighbor, goal), neighbor)) 
    return reconstruct_path(came_from, goal) 
def a_star(start, goal): 
    frontier = [(heuristic(start, goal), 0, start)] 
    came_from = {start: None} 
    g_score = {start: 0} 
    while frontier: 
        _, cost, current = heapq.heappop(frontier) 
        if current == goal: 
            break 
        for neighbor in get_neighbors(current): 
            tentative_g = g_score[current] + 1 
            if neighbor not in g_score or tentative_g < g_score[neighbor]: 
                g_score[neighbor] = tentative_g 
                f_score = tentative_g + heuristic(neighbor, goal) 
                heapq.heappush(frontier, (f_score, tentative_g, neighbor)) 
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
    for r, c in path: 
        grid_copy[r][c] = 2 
    for r, c in obstacles: 
        grid_copy[r][c] = 1 
    grid_copy[start[0]][start[1]] = 3 
    grid_copy[goal[0]][goal[1]] = 4 
    cmap = plt.cm.get_cmap('Accent', 5) 
    plt.imshow(grid_copy, cmap=cmap, origin='upper') 
    plt.title(title) 
    plt.colorbar(ticks=[0,1,2,3,4], label='Legend') 
    plt.clim(-0.5, 4.5) 
    plt.grid(True) 
    plt.show() 

path_greedy = greedy_search(start, goal) 
path_astar = a_star(start, goal) 
draw_path(path_greedy, 'Greedy Best First Search Path') 
draw_path(path_astar, 'A* Search Path') 

