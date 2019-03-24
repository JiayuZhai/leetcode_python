class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        selfmanhadun = abs(target[0]) + abs(target[1])
        for x in ghosts:
        	if abs(x[0] - target[0]) + abs(x[1] - target[1]) < selfmanhadun:
        		return False
        return True
