set1 = set(input().lower().split())
set2 = set(input().lower().split())

union = sorted(set(set1.union(set2)))
intersection = sorted(set(set1.intersection(set2)))

print(*union)
print(*intersection)