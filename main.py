import random
import json


with open('data.json') as f:
    bets = json.load(f)


def reset():
    for i in bets["bets"]:
        i["score"] = 1000000


items = [item["game"] for item in bets["bets"]]
scores = [score["score"] for score in bets["bets"]]


num_of_questions = int(input("Unesite željeni broj pitanja:\n"))
question = random.choices(items, weights=scores, k=num_of_questions)

correct = 0
not_correct = 0

for item in question:
    print(item)
#     game = bets["bets"][question]["game"]
#     code = bets["bets"][question]["code"]
#     score = bets["bets"][question]["score"]
    game = next(i for i in bets["bets"] if i["game"] == item)
    answer = input(f"Unesite šifru za igru: {game['game']}\n")
    try:
        int(answer)
    except ValueError:
        print(answer)
        if answer.lower() == "x":
            break
        elif answer.lower() == "reset":
            reset()
            break

    else:
        if int(answer) == game["code"]:
            print(f"Tačno, šifra za {game['game']} je {game['code']}!\n")
            game["score"] -= 1
            correct += 1
        else:
            game["score"] += 1
            print(f"Na žalost, to nije tačno.\nŠifra za {game['game']} je {game['code']}!\n")
            not_correct += 1


print(f"Tačnih odgovora {correct}.\nNetačnih odgovora {not_correct}")

print(f"Procenat uspešnosti: {correct/len(question)*100}%")
with open('data.json', 'w') as f:
    json.dump(bets, f, indent=2)

