class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # 1. Initialize constraints from the given board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)

        # 2. Backtracking function
        def backtrack(r, c) -> bool:
            # Reached end of board -> puzzle solved
            if r == 9:
                return True

            # Move to the next row if at end of current column
            next_r = r + 1 if c == 8 else r
            next_c = 0 if c == 8 else c + 1

            # Skip pre-filled cells
            if board[r][c] != ".":
                return backtrack(next_r, next_c)

            box_idx = (r // 3) * 3 + (c // 3)

            # Try digits '1' through '9'
            for digit in map(str, range(1, 10)):
                if (
                    digit not in rows[r]
                    and digit not in cols[c]
                    and digit not in boxes[box_idx]
                ):

                    # Place digit & mark sets
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    # Recurse
                    if backtrack(next_r, next_c):
                        return True

                    # Undo placement (backtrack)
                    board[r][c] = "."
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)

            return False

        backtrack(0, 0)