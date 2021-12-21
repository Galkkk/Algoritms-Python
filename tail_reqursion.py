def tailreq (x, total=0):
    if x == 0:
        return total
    else:
        return tailreq(x-1, total+x)

print(tailreq(3))