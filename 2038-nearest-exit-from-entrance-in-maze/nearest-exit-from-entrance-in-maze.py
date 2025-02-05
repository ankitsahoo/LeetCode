class Solution:
    def nearestExit(self, maze, entrance):
        from collections import deque

        m, n = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, distance)
        maze[entrance[0]][entrance[1]] = '+'  # Mark entrance as visited

        while queue:
            x, y, dist = queue.popleft()

            # Check if it's an exit
            if (x == 0 or x == m - 1 or y == 0 or y == n - 1) and (x != entrance[0] or y != entrance[1]):
                return dist

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    maze[nx][ny] = '+'  # Mark as visited
                    queue.append((nx, ny, dist + 1))

        return -1
