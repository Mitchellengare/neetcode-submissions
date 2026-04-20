class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        row, col = len(grid), len(grid[0])
        minutes = 0
        fresh = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c]== 2:
                    q.append((r,c))
                if grid[r][c]== 1:
                    fresh+=1

        while q and fresh > 0:
            for i in range(len(q)):
                (r,c) = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= 0 and nc >= 0 and nr < row 
                        and nc < col and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))

            minutes += 1

        return minutes if fresh == 0 else -1