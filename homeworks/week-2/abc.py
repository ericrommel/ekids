# a= "b"
# print(a)
# print(a + a)
# print(a * 3)
# # print(a + 1)

# UNORDERED=[45, 3, 5, 12, 1, 40]
# print(UNORDERED)
# print(UNORDERED.sort())
# print(UNORDERED)

UNORDERED = [45, 3, 5, 12, 1, 40]
for i in range(len(UNORDERED)):
    print(UNORDERED[i])
    print(UNORDERED[i + 1])

if UNORDERED[1] > UNORDERED[2]:
    TEMP = UNORDERED[1]
    UNORDERED[1] = UNORDERED[5]
    UNORDERED[0] = TEMP
