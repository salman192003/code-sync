class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:


        result = []

        rows = len(matrix)
        cols = len(matrix[0])
         
        visited = set()

 
        r = 0
        c = 0

        while(len(visited) != rows*cols):

            while( c < cols  and (r,c) not in visited ):
                result.append(matrix[r][c])
                visited.add((r,c))
                c = c + 1
            
            c = c - 1
            r = r + 1
            
            while (r < rows and (r,c) not in visited):
                result.append(matrix[r][c])
                visited.add((r,c))
                r = r + 1

            r = r - 1
            c = c - 1


            while ( c >= 0 and (r,c) not in visited):
                result.append(matrix[r][c])
                visited.add((r,c))
                c = c - 1

            c = c + 1
            r = r - 1

            while ( r >= 0 and (r,c) not in visited) :
                result.append(matrix[r][c])
                visited.add((r,c))
                r = r - 1
            
            r = r + 1
            c = c + 1


        return result