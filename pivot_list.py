def partition(li, pivot):

    li_low = []
    li_high = []

    for item in li:
        if item <= pivot:
            li_low.append(item)
        if item > pivot:
            li_high.append(item)

    return [sorted(li_low), sorted(li_high)]

print(partition([ 7, -3, 4, 16, -13, 12, 1 ], 2))