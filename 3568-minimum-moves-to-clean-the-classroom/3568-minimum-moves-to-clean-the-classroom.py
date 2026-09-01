from typing import List
from collections import deque


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        start_r = start_c = 0

        # Give every litter cell an index:
        # first L -> bit 0
        # second L -> bit 1
        # ...
        litter_id = {}
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c

                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        # No litter
        if litter_count == 0:
            return 0

        # If there are 3 litter cells:
        # target = 111
        target_mask = (1 << litter_count) - 1

        # best[r][c][mask]
        # = maximum remaining energy with which we have reached
        # this position after collecting exactly `mask`.
        best = [
            [[-1] * (1 << litter_count) for _ in range(n)]
            for _ in range(m)
        ]

        # queue:
        # (row, col, remaining_energy, collected_mask, moves)
        q = deque()

        q.append((start_r, start_c, energy, 0, 0))
        best[start_r][start_c][0] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:

            r, c, curr_energy, mask, moves = q.popleft()

            # Cannot move anymore
            if curr_energy == 0:
                continue

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                # Boundary check
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Cannot cross obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Moving costs 1 energy
                new_energy = curr_energy - 1
                new_mask = mask

                # Recharge
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # Collect litter
                if classroom[nr][nc] == 'L':

                    idx = litter_id[(nr, nc)]

                    new_mask |= (1 << idx)

                # Everything collected
                if new_mask == target_mask:
                    return moves + 1

                # If we've already reached the exact same
                # (position + collected litter state)
                # with MORE energy, this state is useless.
                if best[nr][nc][new_mask] >= new_energy:
                    continue

                best[nr][nc][new_mask] = new_energy

                q.append(
                    (
                        nr,
                        nc,
                        new_energy,
                        new_mask,
                        moves + 1
                    )
                )

        return -1