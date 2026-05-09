tet_lst = [100, 4, 200, 1, 3, 2, 101, 102, 104, 103, 105, 106]
def longest_consecutive(tet_lst):
    if not tet_lst:
        return 0
 
    sorted_lst = sorted(tet_lst)
   
    longest = 1
    current = 1
 
    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i+1] == sorted_lst[i] + 1:
            current += 1
        elif sorted_lst[i+1] == sorted_lst[i]:
            continue
        else:
            if current > longest:
                longest = current
            current = 1
 
    if current > longest:
        longest = current
       
    return longest
 
result = longest_consecutive(tet_lst)
print(result)