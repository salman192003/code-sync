class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
    
        starting = (0,0)
        queue = deque()
        row, cols = len(grid), len(grid[0])
        visited = set()
        n = len(grid)

        if (grid[0][0] == 1 or grid[n-1][n-1] == 1): #unreachable case:
            return -1

        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[-1,-1],[1,-1]]

        queue.append((0,0,1))
        visited.add((0,0))

        
        while queue:
            r,c,l = queue.popleft()

            if r == n - 1 and c == n-1:
                return l

            for dr,dc in dirs:
                nr,nc = r+dr, c + dc
                if nr in range(row) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] != 1:
                    queue.append((nr,nc,l+1))
                    visited.add((nr,nc))

        
        return -1