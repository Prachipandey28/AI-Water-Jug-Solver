
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ==========================================
# 1. PROBLEM CONFIGURATION
# ==========================================

JUG_A = 4
JUG_B = 3
GOAL = 2

START_STATE = (0, 0)


# ==========================================
# 2. GENERATE VALID NEXT STATES
# ==========================================

def get_next_states(state):
    a, b = state
    next_states = []

    # Fill Jug A
    next_states.append(((JUG_A, b), "Fill Jug A"))

    # Fill Jug B
    next_states.append(((a, JUG_B), "Fill Jug B"))

    # Empty Jug A
    next_states.append(((0, b), "Empty Jug A"))

    # Empty Jug B
    next_states.append(((a, 0), "Empty Jug B"))

    # Pour Jug A into Jug B
    transfer = min(a, JUG_B - b)
    next_states.append(
        ((a - transfer, b + transfer), "Pour A -> B")
    )

    # Pour Jug B into Jug A
    transfer = min(b, JUG_A - a)
    next_states.append(
        ((a + transfer, b - transfer), "Pour B -> A")
    )

    # Remove actions that do not change the state
    return [
        (next_state, action)
        for next_state, action in next_states
        if next_state != state
    ]


# ==========================================
# 3. BREADTH-FIRST SEARCH (BFS)
# ==========================================

def bfs_water_jug():
    queue = deque([(START_STATE, [])])
    visited = {START_STATE}

    while queue:
        current, path = queue.popleft()
        a, b = current

        # Goal test
        if a == GOAL or b == GOAL:
            return path, current

        # Explore next possible states
        for next_state, action in get_next_states(current):

            if next_state not in visited:
                visited.add(next_state)

                new_path = path + [(action, next_state)]
                queue.append((next_state, new_path))

    return None, None


# ==========================================
# 4. DISPLAY WATER LEVELS VISUALLY
# ==========================================

def visualize_state(state, step, action):
    a, b = state

    fig, ax = plt.subplots(figsize=(7, 5))

    # Jug A outline
    ax.add_patch(
        Rectangle(
            (0.7, 0), 1.2, JUG_A,
            fill=False, edgecolor="black", linewidth=3
        )
    )

    # Jug B outline
    ax.add_patch(
        Rectangle(
            (3.0, 0), 1.2, JUG_B,
            fill=False, edgecolor="black", linewidth=3
        )
    )

    # Water in Jug A
    if a > 0:
        ax.add_patch(
            Rectangle(
                (0.7, 0), 1.2, a,
                color="deepskyblue"
            )
        )

    # Water in Jug B
    if b > 0:
        ax.add_patch(
            Rectangle(
                (3.0, 0), 1.2, b,
                color="deepskyblue"
            )
        )

    # Labels
    ax.text(
        1.3, -0.35, f"Jug A: {a}/{JUG_A} L",
        ha="center", fontsize=11
    )

    ax.text(
        3.6, -0.35, f"Jug B: {b}/{JUG_B} L",
        ha="center", fontsize=11
    )

    # Step and action
    ax.set_title(
        f"AI Water Jug Solver\nStep {step}: {action}",
        fontsize=14
    )

    ax.text(
        2.5, 4.5,
        f"Goal: Measure {GOAL} litres",
        ha="center", fontsize=11
    )

    ax.set_xlim(0, 5)
    ax.set_ylim(-0.8, 5)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout()
    plt.show()


# ==========================================
# 5. PRINT THE SOLUTION
# ==========================================

def main():
    print("=" * 40)
    print("       AI WATER JUG SOLVER")
    print("=" * 40)

    print(f"Jug A capacity: {JUG_A} litres")
    print(f"Jug B capacity: {JUG_B} litres")
    print(f"Target amount: {GOAL} litres")

    path, goal_state = bfs_water_jug()

    if path is None:
        print("\nNo solution found.")
        return

    print(f"\nInitial State: {START_STATE}")
    print("State format: (water in Jug A, water in Jug B)")

    print("\n========== SOLUTION ==========")
    print(f"Step 0: Start at {START_STATE}")

    # Show initial state
    visualize_state(START_STATE, 0, "Initial State")

    for step, (action, state) in enumerate(path, start=1):
        print(f"\nStep {step}: {action}")
        print(f"State: {state}")

        visualize_state(state, step, action)

    print("\n========== RESULT ==========")
    print("Goal reached!")
    print("Final state:", goal_state)
    print("Total actions:", len(path))

    print("\nAI Water Jug Solver completed successfully!")


# ==========================================
# 6. START THE PROGRAM
# ==========================================

if __name__ == "__main__":
    main()
