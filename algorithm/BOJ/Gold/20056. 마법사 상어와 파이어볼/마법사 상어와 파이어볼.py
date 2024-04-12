# reference https://jennnn.tistory.com/77

n, m, k = map(int, input().split())
fireballs = []
for _ in range(m):
    x, y, mass, speed, dir = list(map(int, input().split()))
    # use x-1, y-1 to manage board in range 0 to n
    # we don't need an index bro...
    fireballs.append([x-1, y-1, mass, speed, dir])

board = [[[] for _ in range(n)] for _ in range(n)]
# use dirX, Y to move easily
# I got row and col messed up below;;
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    while len(fireballs) > 0:
        x, y, mass, speed, dir = fireballs.pop(0)
        newx = (x + dx[dir] * speed) % n
        newy = (y + dy[dir] * speed) % n
        board[newx][newy].append([mass, speed, dir])
    # don't need to keep fireballs list!!!
    # keep the info right in the board, and create new fireballs after merge

    for x in range(n):
        for y in range(n):

            if len(board[x][y]) > 1:
                sum_mass, sum_speed, count_odd, count = 0,0,0,len(board[x][y])
                while len(board[x][y]) > 0:
                    mass, speed, dir = board[x][y].pop(0)
                    sum_mass += mass
                    sum_speed += speed
                    if dir%2 != 0:
                        count_odd += 1
                if int(sum_mass/5) > 0:
                    # else, this fireball disappears
                    new_dir = []
                    if count_odd == count or count_odd == 0:
                        new_dir = [0, 2, 4, 6]
                    else:
                        new_dir = [1, 3, 5, 7]
                    for i in range(4):
                        fireballs.append([x, y, int(sum_mass/5), int(sum_speed/count), new_dir[i]])

            elif len(board[x][y]) == 1:
                fireballs.append([x, y] + board[x][y].pop(0))

print(sum([spec[2] for spec in fireballs]))


"""
# My attempt...

class Fireball:
    def __init__(info):
        num = info[0]
        x = info[1] - 1 # to manage the board in range 0, n
        y = info[2] - 1 # to manage the board in range 0, n
        mass = info[3]
        speed = info[4]
        dir = info[5]

n, m, k = map(int, input().split())
dirX = [0, 1, 1, 1, 0, -1, -1, -1]
dirY = [-1, -1, 0, 1, 1, 1, 0, -1]
fireballs = list()
for i in range(m):
    fireballs.append(Fireball([i]+list(map(int, input().split()))))

def move():
    for i in range(len(fireballs)):
        fireball = fireballs[i] # shallow copy
        fireball.x = (fireball.x + dirX[fireball.dir] * fireball.speed) % n
        fireball.y = (fireball.y + dirY[fireball.dir] * fireball.speed) % n

def merge():
    pass
    # problem 1. how can i efficiently check if multiple balls are in same loc
    # problem 2. how can i delete and append to fireballs... WHILE managing the Fireball.num???
"""
