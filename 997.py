class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        people, trust_dict = set(), {}
        for a, b in trust:
            people.add(a)
            trust_dict[b] = trust_dict.get(b, 0) + 1
        if len(people) != N-1:
            return -1
        all = set(range(1, N+1))
        candi = list(all - people)
        if trust_dict.get(candi[0], 0) == N-1:
            return candi[0]
        return -1
