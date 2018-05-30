def binary_search(alist, item, fuzzy):
    """ binary search through a sorted list """
    alist = sorted(alist)
    first = 0
    last = len(alist) - 1
    midpoint = 0
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2

        if fuzzy:
            check = alist[midpoint].startswith(item)
        else:
            check = alist[midpoint] == item

        if check:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found, midpoint
