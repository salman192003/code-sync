class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        

        #start from a;; rotten orange, thus find the position of the rotten oranges

        starting = ()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 2):
                    queue.append((i,j))
                    
        
        depth = 0

        while queue:
            rotten_this_layer=False
            for i in range(len(queue)):
                node = queue.popleft()
                
                
                
                directions = [[0,1],[1,0],[0,-1],[-1,0]]

                for dir in directions:
                    nr,nc = node[0] + dir[0], node[1] + dir[1]
                    if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2 #make it rotten
                        rotten_this_layer = True
                        queue.append((nr,nc))
            
            if (rotten_this_layer):
                depth = depth + 1

        for row in grid:
            if 1 in row:
                return -1



        return depth

        
        # now run a bfs from a rotten orange in such a manner that you count the number of layers until all rotten