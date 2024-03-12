n = int(input())
best_score = 0
scores = list(map(float, input().split()))    # for the division later

for score in scores:
    if score > best_score:
        best_score = score

score_sum = 0

for score in scores:
    score_sum += (score/best_score)*100

print(score_sum/n)