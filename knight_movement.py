from collections import deque

# All 8 possible knight moves
KNIGHT_MOVES = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2), (1, 2),
    (2, -1), (2, 1)
]

def is_valid(x, y):
    return 0 <= x < 8 and 0 <= y < 8  # 8x8 chessboard

def minimum_turns_to_capture(startA, startB):
    queue = deque()
    visited = set()

    # Each state: (posA, posB, turn_count, whose_turn, history)
    queue.append((startA, startB, 1, 'A', []))  # Start from turn 1
    visited.add((startA, startB, 'A'))

    while queue:
        posA, posB, turns, turn_owner, history = queue.popleft()

        if turn_owner == 'A':
            for dx, dy in KNIGHT_MOVES:
                newA = (posA[0] + dx, posA[1] + dy)
                if is_valid(*newA):
                    # Capture check happens immediately after move
                    if newA == posB:
                        print(f"{turns} // knightA moves to {list(newA)}, knightA captures knightB on {list(newA)}")
                        return turns
                    state = (newA, posB, 'B')
                    if state not in visited:
                        visited.add(state)
                        move_desc = f"knightA moves to {list(newA)}"
                        queue.append((newA, posB, turns + 1, 'B', history + [move_desc]))
        else:  # knightB's turn
            for dx, dy in KNIGHT_MOVES:
                newB = (posB[0] + dx, posB[1] + dy)
                if is_valid(*newB):
                    # Capture check
                    if newB == posA:
                        print(f"{turns} // knightB moves to {list(newB)}, knightB captures knightA on {list(newB)}")
                        return turns
                    state = (posA, newB, 'A')
                    if state not in visited:
                        visited.add(state)
                        move_desc = f"knightB moves to {list(newB)}"
                        queue.append((posA, newB, turns + 1, 'A', history + [move_desc]))

    print("No capture possible.")
    return -1

# Input handler
def get_position_input(label):
    pos = input(f"Enter position for {label} in the form x,y: ")
    x, y = map(int, pos.strip().split(","))
    return (x, y)

# Main program
if __name__ == "__main__":
    knightA = get_position_input("knightA")
    knightB = get_position_input("knightB")
    minimum_turns_to_capture(knightA, knightB)