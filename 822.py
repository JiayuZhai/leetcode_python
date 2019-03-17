class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        lookup = { x for x, y in zip(fronts,backs) if x == y}
        return min([i for i in fronts+backs if i not in lookup] or [0])
