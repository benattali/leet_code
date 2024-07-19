from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative_count = 0

        for row in reversed(grid):
            for col in reversed(row):
                if col < 0:
                    negative_count += 1
                else:
                    break

        return negative_count


print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
