
ITEMS_PER_PAGE = 2

def offsets(pages):
    offset_start = ITEMS_PER_PAGE
    offset_array = []
    n = 0
    
    for i in range(pages):
        offset_array.append(n)
        n += offset_start

    return offset_array    