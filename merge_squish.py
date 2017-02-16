def merge_squish(a,b):
    for item in a:
        if not item in b:
            b.append(item)

    return sorted(b)

print(merge_squish([1, 2, 3, 4, 5, 6], [5, 6, 7, 8, 2]))