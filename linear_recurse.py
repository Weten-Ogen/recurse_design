def linear_sum(S,n):
    if n <= 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n - 1]
    
s = [1,3,5,6,7,8,9]
print(linear_sum(s,6))


def reverse(s,start,stop):
    if start < stop - 1:
        s[start],s[stop-1] = s[stop - 1],s[start]
    return reverse(s, start + 1,stop - 1)

def power(x,n):
    if n <= 0:
        return 1
    else:
        return x * power(x,n -1)
    
print(power(4,2))

