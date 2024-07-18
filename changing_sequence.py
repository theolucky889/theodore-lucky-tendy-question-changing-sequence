def find_changing_point(arr):
    if len(arr) < 2:
        return -1 # less than 2 elements cannot change trend

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            trend = arr[i] > arr[i - 1]
            break
    for j in range (i, len(arr)):
        if (trend and arr[j] < arr[j - 1]) or (not trend and arr[j] > arr[j - 1]):
            return j - 1
        return 1

# exmaple
arr = [1, 2, 4, 8, 4, 2]
print(find_changing_point(arr))