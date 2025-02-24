def _Heapify(arr: list[int], n: int, i: int):
    largest = i
    left, right = 2 * i, 2 * i + 1

    if left <= n and arr[left] > arr[largest]:
        largest = left

    if right <= n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _Heapify(arr, n, largest)


def HeapSort(arr: list[int]):
    # 인덱스 1부터 시작
    arr.insert(0, 0)

    N = len(arr) - 1

    for i in range(N // 2, 0, -1):
        _Heapify(arr, N, i)
    
    for i in range(N, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        _Heapify(arr, i - 1, 1)

    arr.pop(0)