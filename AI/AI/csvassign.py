import csv
from datetime import datetime, timedelta
from tabulate import tabulate  # pip install tabulate

# -------------------------
# CONFIG
# -------------------------
teams = ["CSK", "MI", "RCB", "GT", "KKR", "SIH"]
venues = ["Chennai", "Mumbai", "Bangalore"]
start_date = datetime(2025, 9, 20)
gap_days = 2
output_file = "tournament_schedule.csv"
# -------------------------

def round_robin(teams_list):
    """Generate round-robin pairings using circle method"""
    n = len(teams_list)
    schedule = []
    teams_local = teams_list[:]
    if n % 2 == 1:
        teams_local.append("BYE")
        n += 1

    rounds = n - 1
    half = n // 2
    for r in range(rounds):
        pairs = []
        for i in range(half):
            t1 = teams_local[i]
            t2 = teams_local[n - 1 - i]
            if t1 != "BYE" and t2 != "BYE":
                pairs.append((t1, t2))
        schedule.append(pairs)
        # rotate teams (except first)
        teams_local = [teams_local[0]] + [teams_local[-1]] + teams_local[1:-1]
    return schedule

def generate_schedule(teams, venues, start_date, gap_days):
    rounds = round_robin(teams)
    rows = []
    match_id = 1
    current_date = start_date
    for r_idx, matches in enumerate(rounds, start=1):
        for m in matches:
            venue = venues[(match_id - 1) % len(venues)]  # cycle venues
            date_str = current_date.strftime("%Y-%m-%d")
            rows.append([match_id, f"Round {r_idx}", m[0], m[1], venue, date_str])
            match_id += 1
        current_date += timedelta(days=gap_days)
    return rows

def save_csv(rows, filename):
    header = ["MatchID", "Round", "TeamA", "TeamB", "Venue", "Date"]
    with open(filename, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)
    print(f"✅ Schedule saved to {filename}")

def display_schedule(rows):
    header = ["MatchID", "Round", "TeamA", "TeamB", "Venue", "Date"]
    print("\n📅 Tournament Schedule:\n")
    print(tabulate(rows, headers=header, tablefmt="fancy_grid"))

def main():
    schedule = generate_schedule(teams, venues, start_date, gap_days)
    display_schedule(schedule)   # show in terminal
    save_csv(schedule, output_file)

if __name__ == "__main__":
    main()
