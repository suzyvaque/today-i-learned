'''
Brute Force

1. Choose 8*8
2. Set two cases of first B or W
3. Calculate num for each cases
4. Update min
'''

# m*n board!!! not n*m
n, m = map(int, input().split())

board = [["-" for color in range(m)] for row in range(n)]

for row_num in range(n):
    board[row_num] = list(input())



min_count = 64  # 8 by 8

for x in range(0, m-7):
    for y in range(0, n-7):
        # x,y is the top left coordinate of checkerboard
        count = 0
        
        # Case 1. if top left is "W", coords at even row & col, odd row & col (if added, %2==0) should be "W"
        for col in range(x, x+8):
            for row in range(y, y+8):
                if (col+row)%2 == 0:
                    if board[row][col] != "W":
                        count += 1
                else:
                    if board[row][col] != "B":
                        count += 1
        # Case 2. top left is "B": 64-count
        min_count = min([min_count, count, 64-count])

print(min_count)
