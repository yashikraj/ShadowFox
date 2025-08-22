justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Number of members:", len(justice_league))

justice_league.extend(["Batgirl", "Nightwing"])
print("After adding members:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman leader:", justice_league)

justice_league.remove("Superman")
justice_league.insert(justice_league.index("Flash"), "Superman")
print("After separating Aquaman & Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

justice_league.sort()
print("Sorted team:", justice_league)
print("New leader:", justice_league[0])
