friends = ["Aditya", "Rahul", "Priya", "Sneha", "Kiran"]
name_lengths = [(name, len(name)) for name in friends]
print("Friend names with lengths:", name_lengths)

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

total_you = sum(your_expenses.values())
total_partner = sum(partner_expenses.values())

print("Your total expenses:", total_you)
print("Partner's total expenses:", total_partner)

if total_you > total_partner:
    print("You spent more.")
elif total_partner > total_you:
    print("Partner spent more.")
else:
    print("Both spent the same.")

differences = {k: abs(your_expenses[k] - partner_expenses[k]) for k in your_expenses}
biggest_diff = max(differences, key=differences.get)
print("Biggest difference in category:", biggest_diff, "with difference of", differences[biggest_diff])
