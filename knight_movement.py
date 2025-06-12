from collections import deque

# All 8 possible knight moves in chess
KNIGHT_MOVES = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

# Check if a position is valid on an 8x8 chessboard
def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8

# Breadth-First Search to find the minimum number of moves to capture
def find_min_turns_to_capture(startA, startB):
    queue = deque()
    visited = set()

    # Try both starting with Knight A and Knight B
    queue.append((startA[0], startA[1], startB[0], startB[1], 0, 'A'))
    queue.append((startA[0], startA[1], startB[0], startB[1], 0, 'B'))

    while queue:
        xA, yA, xB, yB, moves, turn = queue.popleft()

        state = (xA, yA, xB, yB, turn)
        if state in visited:
            continue
        visited.add(state)

        if turn == 'A':
            for dx, dy in KNIGHT_MOVES:
                new_xA, new_yA = xA + dx, yA + dy
                if is_valid(new_xA, new_yA):
                    if new_xA == xB and new_yA == yB:
                        return moves + 1, 'A', (new_xA, new_yA)
                    queue.append((new_xA, new_yA, xB, yB, moves + 1, 'B'))
        else:
            for dx, dy in KNIGHT_MOVES:
                new_xB, new_yB = xB + dx, yB + dy
                if is_valid(new_xB, new_yB):
                    if new_xB == xA and new_yB == yA:
                        return moves + 1, 'B', (new_xB, new_yB)
                    queue.append((xA, yA, new_xB, new_yB, moves + 1, 'A'))

    return -1, '', (-1, -1)

# Test input where Knight A captures Knight B in 1 move
startA = (2, 1)  # Knight A
startB = (4, 2)  # Knight B

# Run the algorithm
turns, capturer, position = find_min_turns_to_capture(startA, startB)
victim = 'B' if capturer == 'A' else 'A'

# Print the result
if turns != -1:
    print(f"{turns} // knight{capturer} moves to {list(position)}, knight{capturer} captures knight{victim} on {list(position)}")
else:
    print("No capture possible.")


