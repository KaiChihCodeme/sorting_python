inp = [6,1,7,8,9,3,5,4,2]

for j in range(len(inp)):
    mini = float("inf")
    min_ind = 0

    # linear search
    for i in range(j, len(inp)):
        if mini > inp[i]:
            mini = inp[i]
            min_ind = i
    
    # swap min
    tmp = inp[j]
    inp[j] = inp[min_ind]
    inp[min_ind] = tmp


print(inp) 
