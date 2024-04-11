# yield vs return https://www.daleseo.com/python-yield/
def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            # return lists with single elements
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:], r-1):
                # arr[i+1:] to escape redundancy
                # 1 element i + r-1 elements from the rest of the list
                yield next + [arr[i]]
                # yield returns a generator with individual combinations
                # should later wrap it with list() for use

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
# basically... meaning for 0<=x<n AND 0<=y<n, save as [x,y] if value is 2
chickens = [[x,y] for x in range(n) for y in range(n) if city[x][y]==2]
houses = [[x,y] for x in range(n) for y in range(n) if city[x][y]==1]

chicken_combs = list(combination(chickens, m))

def cal_distance(house, chicken_remaining):
    # set initial min as possible max
    d_min = 2*n
    for chicken in chicken_remaining:
        dist = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
        d_min = min(d_min, dist)
    return d_min

all_total_distances = []
for chicken_remaining in chicken_combs:
    total = 0
    for house in houses:
        total += cal_distance(house, chicken_remaining)
    all_total_distances.append(total)

print(min(all_total_distances))