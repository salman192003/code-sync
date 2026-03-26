from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        visited = set()


        rows , cols = len(grid),len(grid[0])

        

        def bfs(r,c):

            q = deque() 

            q.append((r,c))
            visited.add((r,c))

            while q:
                (r,c) = q.pop()
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                
                for dr,dc in dirs:
                    nr,nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == "1" and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands = islands + 1
        
        return islands