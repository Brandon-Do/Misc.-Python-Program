def can_pick(li, target):
    print(li, target)
    if li == []:
        return False
    if target == 0:
        return True
    if can_pick(li[1:], target - li[0]) == True:
        return True
    if can_pick(li[1:], target ) == True:
        return True
    return False
print(can_pick([2, 4, 6, 8], 10))