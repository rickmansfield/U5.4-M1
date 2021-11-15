 from collections import deque
def all_paths(G):
    n = len(G)
    q = deque() # append(() & pop() at both ends
    ans = []
    while q:
        # current node path = q.popleft()
        # remember popleft only applies to deque
        # there is no popright() pop() pops from right
        # or pop(0) removes the left most element. 
        if curNode == n-1:
            ans.append(path)
            for nextNode in G[curList]:
                q.append((next.node, path+[next.node]))
                
            return ans