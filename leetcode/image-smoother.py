class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        rows = len(img)
        cols = len(img[0])

        dirs = [[0,1],[0,-1],[-1,0],[1,0],[1,1],[-1,-1],[-1,1],[1,-1]]

        result = [[0 for _ in range (cols)] for _ in range(rows)]


        for r in range(rows):
            for c in range(cols):
                neighbours = []
                neighbours.append(img[r][c])
                for (dr,dc) in dirs:
                    nr = r + dr
                    nc = c + dc
                    if (nr in range(rows) and nc in range(cols)):
                        neighbours.append(img[nr][nc])
                neigh_avg = math.floor(sum(neighbours)/ len(neighbours))
                result[r][c] = neigh_avg

        return result