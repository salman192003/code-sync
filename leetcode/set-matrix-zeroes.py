class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        visited = set()

        #finding initial zero indexes

        initial = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    initial.append((r,c))


        for (r,c) in initial:
                #iterating the row of that (col staying same)
                for dr in range(rows):
                    matrix[dr][c] = 0

                #iterating the col of that ( row staying same)
                for dc in range(cols):
                    matrix[r][dc] = 0