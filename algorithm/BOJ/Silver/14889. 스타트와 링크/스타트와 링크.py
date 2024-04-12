n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for smallerComb in combination(arr[i+1:], r-1):
                yield smallerComb + [arr[i]]

people = [num for num in range(n)]
teams = list(combination(people, n/2))
numTeams = len(teams)

minDiff = -1

for teamNum in range(int(len(teams)/2)):
    score1 = 0
    score2 = 0
    
    
    for i in teams[teamNum]:
        for j in teams[teamNum]:
            score1 += s[i][j]

    for i in teams[numTeams-1-teamNum]:
        for j in teams[numTeams-1-teamNum]:
            score2 += s[i][j]
    
    
    if minDiff == -1:
        minDiff = abs(score1 - score2)
    else:
        minDiff = min(minDiff, abs(score1 - score2))

print(minDiff)