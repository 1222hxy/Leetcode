class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0]*n for _ in range(n)]
        count = 1
        start_index = 0
        while not count >= n**2:
            for i in range(start_index,n-1-start_index):
                mat[start_index][i] = count
                count += 1

            for j in range(start_index, n -1 - start_index):
                mat[j][n-1 - start_index] = count
                count += 1

            for x in range(n-1 - start_index,start_index,-1):
                mat[n-1 - start_index][x] = count
                count += 1

            for y in range(n-1 - start_index,start_index,-1):
                mat[y][start_index] = count
                count += 1

            start_index += 1

        if n % 2 == 1:
            mat[n//2][n//2] = count
        return mat


class Solution2:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0]*n for _ in range(n)]
        count = 1
        start = 0
        while not count >= n**2:
            end = n - 1 - start

            for i in range(start,end):
                mat[start][i] = count
                count += 1

            for j in range(start,end):
                mat[j][end] = count
                count += 1

            for x in range(end,start,-1):
                mat[end][x] = count
                count += 1

            for y in range(end,start,-1):
                mat[y][start] = count
                count += 1

            start += 1

        if n % 2 == 1:
            mat[n//2][n//2] = count

        return mat