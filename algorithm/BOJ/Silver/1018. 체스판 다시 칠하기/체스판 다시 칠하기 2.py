"""
Point 1. n*m array -> n rows, m columns (m elements for each row)
Point 2. do not initialize "min" to 0 -> would always be 0
Point 3. try not to inspect every case -> devise methods as 64-count, checking the top left ...
"""

n, m = map(int, input().split())
# initially was told m*n but input is actually in n*m format...
board = [list(input()) for _ in range(n)]

# if set to 0, min_count will always be 0
min_count = n * m

for topleft_row in range(n-7):
    for topleft_col in range(m-7):
        topleft_color = board[topleft_row][topleft_col]
        count = 0

        for row in range(topleft_row, topleft_row+8):
            for col in range(topleft_col, topleft_col+8):
                color = board[row][col]
                if (row+col) % 2 == 0:
                    if color != topleft_color:
                        count += 1
                else:
                    if color == topleft_color:
                        count += 1

        count = min(count, 64-count)
        min_count = min(count, min_count)

print(min_count)
