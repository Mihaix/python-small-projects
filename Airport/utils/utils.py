def sort(arr, key_func, compare_func = lambda x, y: x > y):
    """
    Sorts a list of objects by a key function.
    :param arr: list of objects
    :param key_func: key function
    :param compare_func: compare function
    :return: the sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_func(key_func(arr[j]), key_func(arr[j + 1])):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def filter(lst, key, value):
    """
    Filters a list of objects by a key and a value.
    :param lst: list of objects
    :param key: key to filter by
    :param value: value to filter by
    :return: the filtered list
    """
    return [obj for obj in lst if key(obj) == value]

def backtracking(arr, condition_func, k, start = 0, group = None, result = None):
    """
    Backtracking algorithm to generate groups of size k based on a condition.
    :param arr: list of objects
    :param condition_func: lambda function to check if a group is valid
    :param k: size of the group to generate
    :param start: starting index for the backtracking
    :param group: current group being generated
    :param result: list to store all valid groups
    :return: list of all valid groups
    """
    if group is None:
        group = []

    if result is None:
        result = []

    if len(group) == k and condition_func(group):
        result.append(group[:])

    for i in range(start, len(arr)):
        group.append(arr[i])
        backtracking(arr, condition_func, k, i + 1, group, result)
        group.pop()

    return result