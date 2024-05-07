def getMax(arr):
    if(len(arr))<2:
        return -1
    largest, second_largest = float('-inf'), float('-inf')
    #for i in range (len(arr)):
    for num in arr:
        if num > largest
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest if second_largest != float('-inf') else -1
        
def getMin(arr):
    if(len(arr))<2:
        return -1
    minimum, second_minimum = float('inf'), float('inf')
    #for i in range (len(arr)):
    for num in arr:
        if num < minimum:
            second_minimum = minimum
            minimum = num
        elif num < second_minimum:
            second_minimum = num
    return second_minimum if second_minimum != float('inf') else -1
        
        
arr = [5,4,3,2,1,-1001]
result_min = getMin(arr)
result_max = getMax(arr)
print("Result : ",result_min, result_max)