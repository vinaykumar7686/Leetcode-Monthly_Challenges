# Jump Game IV

'''
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
 

Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
'''

'''
A) Classical BFS

The code below presents a BFS implementation to solve this problem. All elements of the same value are treated as connected "nodes" in a graph, and further connections are added to their neighbors ( i+1 , i-1 ). The code runs with O(n) time complexity thanks to the use of a Queue/Stack tracking nodes pending for visit, and a dictionary with the lowest distances reached. (We can avoid using a Min-Heap as a Priority Queue since all operations add 1 in distance, so the order of our Stack is never lost, we always advance in patterns, such as 0,1,1,2,2,3,3,4,4).

Another important step to achieve O(n) time complexity is to "teleport" our pointer across nodes with the same value only once. This can be easily achieved by erasing our shared dictionary after the first query.

# Python 2/3
class Solution:
    def minJumps(self, arr):
        E = len(arr) - 1
        if not E:
            return 0
        C = {}
        for i,x in enumerate(arr):
            if x in C:
                C[x].append(i)
            else:
                C[x] = [i]
        def getConns(n):
            a = arr[n]
            if a in C:
                for n2 in C[a]:
                    yield n2
                del C[a]
            if n>1:
                yield n-1
            if n<E:
                yield n+1
        d = {0:0}
        q = collections.deque([0])
        while True:
            if E in d:
                return d[E] # Success
            n = q.popleft()
            x = d[n] 
            for n2 in getConns(n):
                if n2 in d:
                    continue   # Point Already Visited
                d[n2] = x+1    # Lowest Distance for this Point
                q.append(n2)
B) Bidirectional BFS

To reach 100% Speed, it's better to use a Birectional BFS algorithm. These algorithms track the distances from both the start and the target points at the same time, so they are able to find an intersection at the middle. These intersections occur after less extensive searches than in classical BFS, so there's always a speed-up even for small graphs. (In large graphs, the time complexity can be reduced to O(K^0.5), where "K" is the time complexity of a classical BFS).

The code is a bit more intricate due to the need to handle the parallel BFS cases, but it's just an extension. I hope you find it helpful. Cheers,

class Solution:
    def makeConns(self):
        self.C = C = defaultdict(list)
        for i,x in enumerate(self.arr):
            C[x].append(i)
    def getConns(self,n,warp):
        if warp:
            for n2 in self.C[self.arr[n]]:
                yield n2
        if n<self.last:
            yield n+1
        if n>0:
            yield n-1
    def minJumps(self, arr):
        if len(arr)<=1:
            return 0
        self.arr  = arr
        self.last = len(arr) - 1
        self.makeConns()
        S,E   = 0,len(arr)-1 # Start, End
        q1,q2 = collections.deque([S]), collections.deque([E]) # Track Lowest Distances
        # Note: Deque preserves lowest cost, since edges add +1 every time (so we have 0,1,1,1,2,2,2,3,3,4,4)
        d1,d2 = {S:0}, {E:0}
        v1,v2 = set(),set() # Visited Points
        while True:
            for q,vis,own,oppo in [[q1,v1,d1,d2],[q2,v2,d2,d1]]:
                step = own[q[0]] # Ensure advancing one uniform step
                while q and own[q[0]]==step:
                    n    = q.popleft() # visit lowest cost index
                    x    = own[n]
                    warp = not arr[n] in vis
                    vis.add(arr[n])
                    for n2 in self.getConns(n,warp): # visit connections (at the lowest cost)
                        if n2 in own:
                            continue # Exit: already appended to queue at lower cost (or equal)
                        if n2 in oppo:
                            return x+1+oppo[n2] # Success
                        # Add to queue and register Distance
						own[n2] = x+1
                        q.append(n2)
'''

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
