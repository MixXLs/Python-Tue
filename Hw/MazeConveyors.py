def maze_solver_with_conveyors(maze: list[list[str]]) -> dict:
    rows, cols = len(maze), len(maze[0]) if maze else 0

    # หา S และ E
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    if start is None or end is None:
        return {"distance": -1, "path": []}

    # ทิศทางสายพาน
    DIR = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def is_conveyor(ch: str) -> bool:
        return ch in DIR

    # จำลองการไหลบนสายพาน
    def slide_from(nr: int, nc: int):
        if not in_bounds(nr, nc) or maze[nr][nc] == '#':
            return False, None, None
        segment = []

        if not is_conveyor(maze[nr][nc]):
            segment.append((nr, nc))
            return True, (nr, nc), segment

        seen_in_slide = set()
        cr, cc = nr, nc
        while True:
            if not in_bounds(cr, cc) or maze[cr][cc] == '#':
                return False, None, None
            segment.append((cr, cc))

            ch = maze[cr][cc]
            if not is_conveyor(ch):
                return True, (cr, cc), segment

            if (cr, cc) in seen_in_slide:
                return False, None, None
            seen_in_slide.add((cr, cc))

            dr, dc = DIR[ch]
            nr2, nc2 = cr + dr, cc + dc
            if not in_bounds(nr2, nc2) or maze[nr2][nc2] == '#':
                return False, None, None

            if maze[nr2][nc2] == 'E' or maze[nr2][nc2] == '.':
                segment.append((nr2, nc2))
                return True, (nr2, nc2), segment

            cr, cc = nr2, nc2

    # BFS (ใช้ list แทน deque)
    q = [start]
    dist = {start: 0}
    parent = {start: (None, [])}
    STEPS = [(0,1),(0,-1),(1,0),(-1,0)]

    while q:
        r, c = q.pop(0)
        if (r, c) == end:
            break

        for dr, dc in STEPS:
            nr, nc = r + dr, c + dc
            if not in_bounds(nr, nc) or maze[nr][nc] == '#':
                continue

            if maze[nr][nc] == '.' or maze[nr][nc] == 'E':
                end_ok = True
                final_cell = (nr, nc)
                segment = [final_cell]
            else:
                end_ok, final_cell, segment = slide_from(nr, nc)

            if not end_ok:
                continue

            if final_cell not in dist:
                dist[final_cell] = dist[(r, c)] + 1
                parent[final_cell] = ((r, c), segment)
                q.append(final_cell)

    if end not in dist:
        return {"distance": -1, "path": []}

    # กู้คืนเส้นทางเต็ม
    segments = []
    cur = end
    while cur != start:
        prev, seg = parent[cur]
        segments.append(seg)
        cur = prev
    segments.reverse()

    full_path = [start]
    for seg in segments:
        full_path.extend(seg)

    return {"distance": dist[end], "path": [[r, c] for (r, c) in full_path]}

    pass



if __name__ == "__main__":
    maze = [
        ['S', '.', '>', '>', 'E'],  # 0
        ['#', '#', '#', '#', '#']   #  1
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)   
    #Output: {'distance': 2, 'path': [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]]}  #path คือลำดับขั้นที่เดินทาง

    maze = [
        ['S', '.', '>', '#', 'E'], # 
        ['#', '#', '#', '#', '#'] 
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {"distance": -1, "path": []}   ถ้าเจอ #(กำแพง) = ไม่มีเส้นทางให้แสดง path []


    maze = [
        ['S', '.', 'v', '.', 'E'], # > > v v v > ^ ^ ^ >
        ['#', '#', 'v', '.', '#'],
        ['.', '.', 'v', '.', '.'],
        ['#', '#', '.', '.', '#'],
        ['.', '.', '.', '.', '.']
    ]
    result = maze_solver_with_conveyors(maze)
    print(result)
    #Output: {'distance': 7, 'path': [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [3, 3], [2, 3], [1, 3], [0, 3], [0, 4]]}
