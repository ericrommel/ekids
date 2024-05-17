unordered = [45, 3, 5, 12, 1, 40]
ordered = []
for i in range(len(unordered)):
    if i == 0:
        ordered.insert(0, unordered[i])
    for j in range(len(ordered)):
        if i >= ordered[j]:
            ordered.insert(j+1, unordered[i])
        else:
            ordered.insert(j-1, unordered[i])
print(ordered)
