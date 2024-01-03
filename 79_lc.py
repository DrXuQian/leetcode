from typing import List


class Solution:
    def search_from_point_for(self, i, j, word, board, visited):
        if len(word) == 0:
            return True
        if board[i][j] != word[0]:
            return False
        if len(word) == 1:
            return True
        visited.add((i, j))
        if i < len(board) - 1 and (i + 1, j) not in visited:
            ret = self.search_from_point_for(i + 1, j, word[1:], board, visited)
            if ret:
                return True
        if i > 0 and (i - 1, j) not in visited:
            ret = self.search_from_point_for(i - 1, j, word[1:], board, visited)
            if ret:
                return True
        if j < len(board[0]) - 1 and (i, j + 1) not in visited:
            ret = self.search_from_point_for(i, j + 1, word[1:], board, visited)
            if ret:
                return True
        if j > 0 and (i, j - 1) not in visited:
            ret = self.search_from_point_for(i, j - 1, word[1:], board, visited)
            if ret:
                return True
        visited.remove((i, j))
        return False


    def exist(self, board: List[List[str]], word: str) -> bool:
        for i, column in enumerate(board):
            for j, element in enumerate(column):
                visited = set()
                ret = self.search_from_point_for(i, j, word, board, visited)
                if ret:
                    return True
        return False

ret = Solution().exist(board = [["A","B","C","E"],
                                ["S","F","E","S"],
                                ["A","D","E","E"]], word = "ABCESEEEFS")
print(ret)
