def sum(arr, total=0):
    if len(arr) == 1:
        return arr[0]      
    else:
        return arr.pop(0) + sum(arr)
        
print(sum([1,2,3]))
