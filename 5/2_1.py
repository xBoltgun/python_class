def find_outlier(integers):
    odd=[]
    par=[]
    for num in integers:
        if num%2 ==0:
            par.append(num)
        else:
            odd.append(num)
    if len(par)>len(odd):
        return odd[0]
    else:
        return par[0]
    return None