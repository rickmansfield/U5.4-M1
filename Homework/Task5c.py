"""
FINDING ALL PATHS FROM SOURCE TO TARGET IN A DIRECTED ACYCLIC GRAPH (DAG) USING BREADTH FIRST SEARCH ALGORITHM
This version is for LeetCode 
"""

from collections import deque

def allPathsSourceTarget(self, G: List[List[int]]) -> List[List[int]]:
    ans = []
    n = len(G)
    q = deque([(0, [0])])
    while q:
        curNode, curPath = q.popleft()
        if curNode == n - 1:
            ans.append(curPath)
        for nextNode in G[curNode]:
            q.append((nextNode, curPath + [nextNode]))
    return ans