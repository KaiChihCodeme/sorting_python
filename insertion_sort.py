inp = [6,1,7,8,9,3,5,4,2]

for i in range(len(inp)):
    for j in range(i, 0, -1):
        if inp[j] < inp[j-1]:
            tmp = inp[j]
            inp[j] = inp[j-1]
            inp[j-1] = tmp
        
print(inp)