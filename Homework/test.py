from collections import deque
def solution(graph):
    ans = []
    n = len(graph)
    q = deque([(0, [0])])
    
    while q:
        curNode, curPath = q.popleft()
        if curNode == n-1:
            ans.append(curPath)
            for nextNode in graph[curNode]:
                q.append((nextNode, curPath + [nextNode]))
    return ans

print(help(deque.leftpop)
