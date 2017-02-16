def uniform(li):
    value = 0
    if li[0] != []:
        for num in li[0]:
            value += num

    comp_val = 0
    for k in range(1, len(li)):
        for ea in li[k]:
            print(ea)
            comp_val += ea
        if comp_val != value:
            return False
        comp_val = 0
    return True

print(uniform( [[ 192, 344, 17]] ))