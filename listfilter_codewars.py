
def filter_list(l):
    nlist = []
    for filter in l:
      #print(filter)
        if isinstance(filter, int) == True:
            if filter > 0:
                nlist.append(filter)
    return nlist






l = [1, 'a', 'b', 0, 15]
print(filter_list(l))