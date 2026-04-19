# Quick Match Log for Mobile Legends: Bang Bang
heroes = ["Layla", "Tigreal", "Gusion", "Kagura", "Chou"]

def get_int(prompt, allow_zero=False):
    while True:
        try:
            v = int(input(prompt).strip())
            if v < 0 or (not allow_zero and v == 0):
                print("Enter a valid positive integer." if not allow_zero else "Enter a valid non-negative integer.")
                continue
            return v
        except ValueError:
            print("Please enter an integer.")

def get_result(prompt):
    while True:
        r = input(prompt).strip().upper()
        if r in ("W","L"):
            return r
        print("Enter 'W' for win or 'L' for loss.")

def compute_kda(kills, deaths, assists):
    denom = deaths if deaths != 0 else 1
    return (kills + assists) / denom

def tag_by_kda_and_result(kda, result):
    if kda >= 5:
        return "DOMINATION!" if result == "W" else "DOMINATION!!!!"
    else:
        return "Better Luck Next Game!" if result == "W" else "Better Luck Next Game!"

# Player info
ign = input("Enter player IGN (in-game name): ").strip()
rank = input("Enter player rank: ").strip()

matches = []  # each entry: dict or None if skipped
print("\nHero roster:")
for i, h in enumerate(heroes, start=1):
    print(f"{i}. {h}")

print("\nEnter up to 4 match entries. For each match choose hero number (1-5) or 0 to skip this match slot.")
for m in range(1, 5):
    while True:
        try:
            hero_num = int(input(f"\nMatch {m} - Hero number (0 to skip): ").strip())
        except ValueError:
            print("Please enter an integer 0-5.")
            continue
        if hero_num == 0:
            print("No stats recorded")
            matches.append(None)
            break
        if 1 <= hero_num <= 5:
            hero = heroes[hero_num - 1]
            kills = get_int("Kills: ", allow_zero=True)
            deaths = get_int("Deaths: ", allow_zero=True)
            assists = get_int("Assists: ", allow_zero=True)
            result = get_result("Result (W/L): ")
            kda = compute_kda(kills, deaths, assists)
            tag = tag_by_kda_and_result(kda, result)
            matches.append({
                "hero": hero,
                "kills": kills,
                "deaths": deaths,
                "assists": assists,
                "result": result,
                "kda": kda,
                "tag": tag
            })
            break
        else:
            print("Enter a number between 0 and 5.")

# Summaries
logged = [m for m in matches if m is not None]
matches_played = len(logged)
wins = sum(1 for m in logged if m["result"] == "W")
losses = sum(1 for m in logged if m["result"] == "L")
win_rate = int((wins / matches_played) * 100) if matches_played > 0 else 0

best_match_index = None
best_kda = -1
for idx, m in enumerate(matches, start=1):
    if m is not None and m["kda"] > best_kda:
        best_kda = m["kda"]
        best_match_index = idx

# Output formatted match log
print("\n----- Match Log -----")
print(f"IGN: {ign}")
print(f"Rank: {rank}\n")

for idx, m in enumerate(matches, start=1):
    if m is None:
        print(f"Match {idx}: No stats recorded")
    else:
        print(f"Match {idx}: Hero: {m['hero']}, KDA: {m['kda']:.2f}, Result: {m['result']}, Tag: {m['tag']}")

print(f"\nWin/Loss: {wins}/{losses}")
print(f"Win Rate: {win_rate}%")

if best_match_index is not None:
    bm = matches[best_match_index - 1]
    print(f"Best Match: Match {best_match_index} ({bm['hero']}) with KDA {bm['kda']:.2f}")
else:
    print("Best Match: None recorded")