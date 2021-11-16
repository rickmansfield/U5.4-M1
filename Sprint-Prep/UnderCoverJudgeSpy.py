def find_judge(N, trust):  # O(k + v) =>  O(n) -> linear time complexity
    """
    Inputs:
    N -> int
    trust -> List[List[int]]
    Output:
    int
    """
    peopleWhoAreTrusted = [0] * (N + 1)  # O(1)
    peopleWhoTrustOthers = [0] * (N + 1)  # O(1)

    for a, b in trust:  # O(k)
        peopleWhoAreTrusted[b] += 1  # O(1) 
        peopleWhoTrustOthers[a] += 1  # O(1)

    for i in range(1, N + 1):  # O(n)
        if peopleWhoAreTrusted[i] == N - 1 and peopleWhoTrustOthers[i] == 0:  # O(1)
            return i  # O(1)

    return -1  # O(1)


find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
