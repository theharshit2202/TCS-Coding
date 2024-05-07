def getMin(arr):
    minimum_declared = float('inf')
    for i in range (len(arr)):
        minimum_found_out = min(minimum_declared, arr[i])
    return minimum_found_out

arr = [5,4,3,2,-1001]
result = getMin(arr)
print("Result",result)