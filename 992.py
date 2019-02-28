from collections import Counter
from copy import copy
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        max_left = 0
        min_left = 0
        right = -1
        max_count_different = 0
        min_count_different = 0
        max_counter = Counter()
        min_counter = None

        while max_count_different != K:  # prepare right
            right += 1
            if right >= len(A):
                return 0
            right_value = A[right]
            max_counter[right_value] += 1
            if max_counter[right_value] == 1:
                max_count_different += 1

        min_counter = copy(max_counter)

        while True:  # prepare min left
            left_value = A[min_left]
            if min_counter[left_value] == 1:
                break
            # left move
            min_counter[left_value] -= 1
            min_left += 1
        min_count_different = max_count_different  # = K
        result = min_left - max_left + 1

        # after prepare

        while True:
            right += 1
            if right == len(A):
                return result
            right_value = A[right]
            max_counter[right_value] += 1
            min_counter[right_value] += 1
            if max_counter[right_value] == 1:
                while True:  # adjust left_max
                    left_value = A[max_left]
                    if min_left == max_left:
                        min_left += 1
                        min_counter[left_value] -= 1
                    max_counter[left_value] -= 1
                    max_left += 1
                    if max_counter[left_value] == 0:
                        break
                while True:  # adjust left_min
                    left_value = A[min_left]
                    if min_counter[left_value] == 1:
                        break

                    min_counter[left_value] -= 1
                    min_left += 1  # left move

                result += min_left - max_left + 1
            else:
                while True:  # adjust left_min
                    left_value = A[min_left]
                    if min_counter[left_value] == 1:
                        break

                    min_counter[left_value] -= 1
                    min_left += 1  # left move
                result += min_left - max_left + 1
