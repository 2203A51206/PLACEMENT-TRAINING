def freq(arr):
    if not arr:
        return []
    freq = {}
    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    sorted_numbers = sorted(freq.keys(), key=lambda x: freq[x],reverse=True)

    result = []
    for num in sorted_numbers:
        result.extend([num] * freq[num])

    return result

arr = [1, 2, 3, 4, 7, 7, 8, 2, 1, 3]
print(freq(arr))