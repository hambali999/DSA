def merge(*arrays):
    merged_array = []
    for array in arrays:
        for element in array:
            if element not in merged_array:
                merged_array.append(element)
                merged_array.sort()
    return merged_array

a = ["alpha", "charlie", "delta"]
b = ["bravo", "delta"]
c = ["golf", "delta"]
d = ["foxtrot", "delta", "echo"]


print(merge(a,b))