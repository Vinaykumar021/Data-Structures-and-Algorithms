class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)  #stores the count of each value
        maxHeap = [-cnt for cnt in count.values()]  # converts it into an -ve array for maxheap
        heapq.heapify(maxHeap) # converts it into maxHeap

        t = 0 #initializes time
        q = deque() # creates a queue
        while maxHeap or q:
            t += 1
            if not maxHeap: # if maxheap is empty and q is not empty then t is skipped to q[0][1] to reduce iterations
                t = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap) #else removes the element from maxheap
                if cnt:
                    q.append([cnt, n + t]) # if cnt is not empty, it is appended to q and wait time is updated
            if q and q[0][1] == t: # if waittime in q == t , q values is pushed bacj to heap
                heapq.heappush(maxHeap, q.popleft()[0])
        return t # returns final time




