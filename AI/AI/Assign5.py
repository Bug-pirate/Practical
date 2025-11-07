# Knowledge base: rules

rules = [
    ([("problem", "power_light_off")],
     ("solution", "check_power_supply")),

    ([("problem", "computer_not_starting"),
      ("solution", "power_supply_ok")],
     ("solution", "check_RAM")),

    ([("problem", "blank_display"),
      ("solution", "power_supply_ok")],
     ("solution", "check_monitor_cable")),

    ([("problem", "computer_not_starting"),
      ("problem", "blank_display")],
     ("solution", "check_graphics_card")),

    ([("problem", "strange_beep")],
     ("solution", "check_motherboard")),

    ([("problem", "computer_not_starting"),
      ("problem", "strange_beep")],
     ("solution", "check_hard_disk")),

    ([("problem", "computer_not_starting"),
      ("solution", "RAM_ok")],
     ("solution", "check_operating_system")),
]


# Forward Chaining Algorithm
def forward_chaining(facts, rules):
    inferred = set(facts)
    changed = True

    while changed:
        changed = False
        for premises, conclusion in rules:
            if all(p in inferred for p in premises):
                if conclusion not in inferred:
                    inferred.add(conclusion)
                    changed = True

    return inferred


# Interactive System
if __name__ == "__main__":
    print("-------------------------------------------------")
    print("   Troubleshooting Expert System (Forward Chaining)")
    print("-------------------------------------------------\n")

    print("Enter observed problems (symptoms).")
    print("Available options:")
    print(" - computer_not_starting")
    print(" - power_light_off")
    print(" - blank_display")
    print(" - strange_beep")
    print("Type 'done' when finished.\n")

    facts = []

    while True:
        symptom = input("Enter a problem (or 'done'): ").strip()
        if symptom.lower() == "done":
            break
        if symptom in ["computer_not_starting", "power_light_off",
                       "blank_display", "strange_beep"]:
            facts.append(("problem", symptom))
        else:
            print("Unknown problem. Please choose from the list above.")

    # Run inference
    inferred_facts = forward_chaining(facts, rules)

    # Display results
    print("\nSuggested Actions / Solutions:")
    solutions_found = False

    for f in inferred_facts:
        if f[0] == "solution":
            print(" -", f[1])
            solutions_found = True

    if not solutions_found:
        print("No solution found. Please provide more symptoms.")
