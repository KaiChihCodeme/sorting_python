def quick_sort(inp):
    if len(inp) < 1:  # 終止條件，當長度小於1回傳空陣列
        return []
    
    pick = inp[0] #隨便挑一個base，我挑最前面的
    l = list()  # divide two arrays
    r = list()
    for i in range(1, len(inp)):  # 比對，比pick小放l, else r
        if pick < inp[i]:
            r.append(inp[i])
        else:
            l.append(inp[i])

    return quick_sort(l) + [pick] + quick_sort(r)  # recursive, return l+pick+r



inp = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
print(quick_sort(inp))