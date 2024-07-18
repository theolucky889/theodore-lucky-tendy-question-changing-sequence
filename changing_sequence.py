def find_changing_point(arr):
    if len(arr) < 3:
        return -1 # less than 3 elements cannot change trend

    # for i in range(1, len(arr)):
    #     if arr[i] != arr[i - 1]:

    i = 1
    while i < len(arr) and arr[i] == arr[i - 1]:
        i += 1
        
    if i == len(arr):
        return -1 # if all equal
    
    trend = arr[i] > arr[i - 1]
    
    for j in range (i  + 1, len(arr)):
        if (trend and arr[j] < arr[j - 1]) or (not trend and arr[j] > arr[j - 1]):
            return j - 1
        return 1

# exmaple
arr = [1, 2, 4, 8, 4, 2]
print(find_changing_point(arr))