def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(max_num(25, 38, 17)) #expects 38