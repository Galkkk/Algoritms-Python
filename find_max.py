def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1]  else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max 
    

print(max([11,5,22,0,199]))