from constraint import Problem, AllDifferentConstraint
from itertools import combinations

# Teams (small demo with 4 teams)
teams = ["MI", "CSK", "RCB", "KKR"]

# Generate matches (single round robin)
matches = list(combinations(teams, 2))   # e.g., (MI, CSK), (MI, RCB), ...

# Available slots (days) – at least as many as matches
slots = list(range(1, len(matches) + 1))

# Create CSP problem
problem = Problem()

# Each match must be assigned to one day
for match in matches:
    problem.addVariable(match, slots)

# Constraint: a team cannot play 2 matches on the same day
def no_same_day(*days):
    return len(set(days)) == len(days)

for team in teams:
    team_matches = [m for m in matches if team in m]
    problem.addConstraint(no_same_day, team_matches)

# Constraint: each day has at most one match (all matches on different slots)
problem.addConstraint(AllDifferentConstraint(), matches)

# Solve
solutions = problem.getSolutions()

# Print one valid schedule
if solutions:
    print("Total valid schedules found: ", len(solutions))
    print("One possible schedule:\n")
    schedule = solutions[24]
    for match, day in sorted(schedule.items(), key=lambda x: x[1]):
        print(f"Day {day}: {match[0]} vs {match[1]}")
else:
    print("No valid schedule found")