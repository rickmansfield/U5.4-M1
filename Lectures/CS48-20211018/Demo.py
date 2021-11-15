"""
In a town, there are `N` people labelled from `1` to `N`.  There is a rumor
that one of these people is secretly the town judge.
If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.
You are given `trust`, an array of pairs `trust[i] = [a, b]` representing that
the person labelled a trusts the person labelled `b`.
If the town judge exists and can be identified, return the label of the town
judge.  Otherwise, return `-1`.

Example 1:
```plaintext
Input: N = 2, trust = [[1,2]]
Output: 2
```

Example 2:
```plaintext
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
```

Example 3:
```plaintext
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```

Example 4:
```plaintext
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
```
Example 5:
```plaintext
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
```
Constraints:
- `1 <= N <= 1000`
- `0 <= trust.length <= 10^4`
- `trust[i].length == 2`
- `trust[i]` are all different
- `trust[i][0] != trust[i][1]`
- `1 <= trust[i][0], trust[i][1] <= N`

counter? dictionary? or list
iterate over trust
[4, 3]
 a, b
inward_trust =   [0, 0, 0, 3, 2]
outward_trust =  [0, 2, 2, 0, 1]

count the trust

iterate over the trust of 1 to N + 1
  check the two constraints ... Inward Trust == N - 1
  and outward trust == 0
  return the persons ID

return -1


"""


def find_judge(N, trust):  # O(k + v) =>  O(n) -> linear time complexity
    """
    Inputs:
    N -> int
    trust -> List[List[int]]
    Output:
    int
    """
    inward_trust = [0] * (N + 1)  # O(1)
    outward_trust = [0] * (N + 1)  # O(1)

    for a, b in trust:  # O(k)
        outward_trust[a] += 1  # O(1)
        inward_trust[b] += 1  # O(1)

    for i in range(1, N + 1):  # O(n)
        if inward_trust[i] == N - 1 and outward_trust[i] == 0:  # O(1)
            return i  # O(1)

    return -1  # O(1)


find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]])
