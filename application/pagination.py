
ITEMS_PER_PAGE = 3

def offsets(pages):
    offset_increase = ITEMS_PER_PAGE
    offset_array = []
    n = 0
    
    for i in range(pages):
        offset_array.append(n)
        n += offset_increase

    return offset_array    