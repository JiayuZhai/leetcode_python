class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        from collections import deque

        if len(deck) == 0:
            return []
        deck.sort()
        result = deque()
        result.append(deck[-1])
        for i in range(len(deck)-2, -1, -1):
            result.appendleft(result.pop())
            result.appendleft(deck[i])
        return list(result)
