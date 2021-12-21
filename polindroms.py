k=int(input())
count = 0

for p in range(k+1):
    x = p

    if x < 10:
        count += 1

    if x >= 10:
        y=str(x)

        if ( len(y) % 2 )==0:
            for i in range( (len(y)//2) ):
                if y[i] == y[ (len(y))-i-1 ]:
                    count += 1
            
            
        for i in range( ((len(y)-1)//2) ):
            if y[i] == y[ (len(y))-i-1 ]:
                count += 1
        

print(count)