"""
2352. Equal Row and Column Pairs - Medium
https://leetcode.com/problems/equal-row-and-column-pairs/
Pattern: Hash Map (counting), matrix transpose
Time: O(n²)   Space: O(n²)
"""


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = {}
        for l in grid:
            key = tuple(l)
            rows[key] = rows.get(key, 0) + 1
        
        columns = [[] for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                columns[j].append(grid[i][j])
        for i in range(len(columns)):
            columns[i] = tuple(columns[i])

        return sum(rows.get(c,0) for c in columns)


if __name__ == "__main__":
    sol = Solution()
    assert sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
    assert sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
    print("all tests passed")