import heapq as hq
def solution(operations):
    answer = []
    heap=[]
    for i in range(len(operations)) :
        if not heap and "D" in operations[i]:
            continue
        if 'I' in operations[i] :
            hq.heappush(heap,int(operations[i][2:]))
        elif operations[i]=="D -1":
            hq.heappop(heap)
        elif operations[i]=="D 1":
            for i in range(len(heap)) :
	            heap[i]=-heap[i]
            hq.heapify(heap)
            hq.heappop(heap)
            for i in range(len(heap)) :
	            heap[i]=-heap[i]
            hq.heapify(heap)
    if not heap :
        return [0,0]
    return [max(heap),hq.heappop(heap)]
