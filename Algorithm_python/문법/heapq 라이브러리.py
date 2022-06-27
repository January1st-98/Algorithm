import heapq

# 최대 힙
def heapsort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)

    for _ in range(len(h)):
        result.append(-heapq.heappop(h))

    return result

result = heapsort([1, 0, 8, 3, 7, 5, 4, 2, 9, 6])
print(result)