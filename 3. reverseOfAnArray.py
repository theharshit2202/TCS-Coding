APPROACH 1:-
def arr_reverse(arr):
    if len(arr)<2:
        return arr
    for i in range(len(arr) // 2): #// -> discards remaninder
        temp = arr[i]
        arr[i] = arr[len(arr)-i-1]
        arr[len(arr)-i-1] = temp
    return arr
        
arr = [5,4,3,2,1]
result = arr_reverse(arr)
print("Result : ",result)



APPROACH 2:-
def getReverse(arr):
    n = len(arr)
    arr.reverse()
    print(arr)

getReverse([1,2,3,4,5])

