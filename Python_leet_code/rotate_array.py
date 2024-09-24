

def rev(a_list, l, u):
    while l < u:
        a_list[l], a_list[u] = a_list[u], a_list[l]
        l += 1
        u -= 1

def rotate_array(a_list, k):
    n = len(a_list)
    k = k % n
    rev(a_list, 0, n-1)
    rev(a_list, 0, k-1)
    rev(a_list, k, n-1)
    return a_list



a = [1, 2, 3, 4, 5, 6, 7]

print(rotate_array(a, 3)) # [5, 6, 7, 1, 2, 3, 4]