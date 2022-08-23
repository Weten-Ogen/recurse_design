def binary_sum(s,start,stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    else:
        mid =(start + stop) // 2
        return binary_sum(s,start,mid) + binary_sum(s,mid,stop)

s = [2,3,4,6,7,8]
print(binary_sum(s,0,5))

(0,2.5) (2.5,5)
