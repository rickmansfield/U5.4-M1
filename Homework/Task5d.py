"""
FINDING ALL PATHS FROM SOURCE TO TARGET IN A DIRECTED ACYCLIC GRAPH (DAG) USING BREADTH FIRST SEARCH ALGORITHM
The current node is the last node in the current path, thus we can simply push a list of nodes (current path) into the queue.
"""

from collections import deque

def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
    ans = []
    n = len(G)
    q = deque([[0]])
    while q:
        curPath = q.popleft()
        curNode = curPath[-1]
        if curNode == n - 1:
            ans.append(curPath)
        for nextNode in G[curNode]:
            q.append(curPath + [nextNode])
    return ans