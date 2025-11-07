# -------------------------------
# Experiment 7: Goal Stack Planning in Block World Domain
# -------------------------------

class GoalStackPlanner:
    def __init__(self, initial, goal, actions):
        """Initialize the Goal Stack Planner."""
        self.state = set(initial)
        self.goal = goal
        self.actions = actions
        self.stack = list(goal)
        self.plan = []

    def is_satisfied(self, fact):
        """Check if a fact (goal condition) is satisfied in the current state."""
        return fact in self.state

    def apply_action(self, action):
        """Apply an action — update the current state."""
        for d in action["delete"]:
            self.state.discard(d)
        for a in action["add"]:
            self.state.add(a)

    def plan_steps(self):
        """Generate plan using Goal Stack Planning."""
        while self.stack:
            top = self.stack.pop()

            # If the top of the stack is a goal (string)
            if isinstance(top, str):
                if not self.is_satisfied(top):
                    # Find an action that can achieve this goal
                    for action in self.actions:
                        if top in action["add"]:
                            # Push the action and its preconditions
                            self.stack.append(action)
                            self.stack.extend(action["preconditions"])
                            break

            # If the top of the stack is an action (dict)
            elif isinstance(top, dict):
                if all(pre in self.state for pre in top["preconditions"]):
                    # Preconditions satisfied → execute the action
                    self.apply_action(top)
                    self.plan.append(top["name"])

        return self.plan


# -------------------------------
# STRIPS OPERATORS for Block World
# -------------------------------

def PickUp(x):
    return {
        "name": f"PickUp({x})",
        "preconditions": [f"OnTable({x})", f"Clear({x})", "ArmEmpty"],
        "add": [f"Holding({x})"],
        "delete": [f"OnTable({x})", "ArmEmpty"]
    }

def PutDown(x):
    return {
        "name": f"PutDown({x})",
        "preconditions": [f"Holding({x})"],
        "add": [f"OnTable({x})", f"Clear({x})", "ArmEmpty"],
        "delete": [f"Holding({x})"]
    }

def Stack(x, y):
    return {
        "name": f"Stack({x},{y})",
        "preconditions": [f"Holding({x})", f"Clear({y})"],
        "add": [f"On({x},{y})", f"Clear({x})", "ArmEmpty"],
        "delete": [f"Holding({x})", f"Clear({y})"]
    }

def UnStack(x, y):
    return {
        "name": f"UnStack({x},{y})",
        "preconditions": [f"On({x},{y})", f"Clear({x})", "ArmEmpty"],
        "add": [f"Holding({x})", f"Clear({y})"],
        "delete": [f"On({x},{y})", "ArmEmpty"]
    }


# -------------------------------
# INITIAL & GOAL STATES
# -------------------------------

initial_state = [
    "OnTable(A)", "OnTable(B)", "OnTable(C)",
    "Clear(A)", "Clear(B)", "Clear(C)",
    "ArmEmpty"
]

goal_state = ["On(C,B)", "On(B,A)"]

actions = [
    PickUp("A"), PickUp("B"), PickUp("C"),
    PutDown("A"), PutDown("B"), PutDown("C"),
    Stack("A", "B"), Stack("A", "C"), Stack("B", "A"),
    Stack("B", "C"), Stack("C", "A"), Stack("C", "B"),
    UnStack("A", "B"), UnStack("A", "C"),
    UnStack("B", "A"), UnStack("B", "C"),
    UnStack("C", "A"), UnStack("C", "B")
]


# -------------------------------
# RUNNING THE PLANNER
# -------------------------------

planner = GoalStackPlanner(initial_state, goal_state, actions)
plan = planner.plan_steps()

print("\n-------------------------------")
print("Final Plan Sequence:")
print("-------------------------------")
for step in plan:
    print("→", step)

print("\n-------------------------------")
print("Final State:")
print("-------------------------------")
for s in sorted(planner.state):
    print(s)
