from data import data
import random

# výběr položky
a = data[random.randint(0, len(data) - 1)]
aa = (f"{a["name"]}, {a["description"]}, z {a["country"]}")

b = random.choice(data)
bb = (f"{b["name"]}, {b["description"]}, z {b["country"]}")

score = 0

while True:
    print(f"Porovnejte A: {aa}\nPorovnejte B: {bb}")

    guess = input("Kdo má více sledujících na instagramu? ").upper()
    if guess == "A":
        if a["follower_count"] > b["follower_count"]:
            score += 1
            print(f"Uhádli jste. Vaše skóre je {score}")
            b = random.choice(data)
            bb = (f"{b["name"]}, {b["description"]}, z {b["country"]}")
        else:
            print(f"To je špatně. Vaše konečné skóre je {score}")
            break
    elif guess == "B":
        if b["follower_count"] > a["follower_count"]:
            score += 1
            print(f"Uhádli jste. Vaše skóre je {score}")
            a = data[random.randint(0, len(data) - 1)]
            aa = (f"{a["name"]}, {a["description"]}, z {a["country"]}")
        else:
            print(f"To je špatně. Vaše konečné skóre je {score}")
            break



