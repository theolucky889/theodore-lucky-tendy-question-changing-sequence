def find_changing_point(arr):
    if not arr or len(arr) < 3:
        return -1 # less than 3 elements cannot change trend

    increasing = arr[1] > arr[0]
        
    for i in range(1, len(arr) - 1):
        if increasing and arr[i] > arr[i + 1]:
            return i
        elif not increasing and arr[i] < arr[i + 1]:
            return i
    
    trend = arr[i] > arr[i - 1]
    
    for j in range(i + 1, len(arr)):
        if (trend and arr[j] < arr[j - 1]) or (not trend and arr[j] > arr[j - 1]):
            return j - 1
        return 1

# exmaple
arr = [1, 2, 4, 8, 4, 2]
print(find_changing_point(arr))