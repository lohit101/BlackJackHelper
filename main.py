import random

list = []

for i in range(1, 11):
    print("Card number " + str(i) + " : ")
    cardInp = input(">>> ")
    list.append(cardInp)

print("\n")
print(list)

def main():
    x = 0

    while True:
        x = x + 1
        print("\n\n<========== " + str(x) + " ==========>")

        maxProb = max(set(list), key=list.count)

        count = list.count(maxProb)

        prob = int(count) / len(list)

        print("\nHighest probability occurence is: {} ({})".format(str(maxProb), str(prob)))

        inp = input("Hand: ").lower()

        rand = ["HIT", "HIT", "HIT", "HIT", "STAND", "STAND", "STAND"]

        if "12" in inp or "13" in inp or "14" in inp:
            rChoice = random.choice(rand)
            print(str(rChoice) + "\n")

            if "HIT" in rChoice:
                hitInp = input("What card did you get: ")
                list.append(str(hitInp))
                main()

            elif "STAND" in rChoice:
                main()

        if int(inp) + int(maxProb) <= 21:
            print("HIT\n")
            hitInp = input("What card did you get: ")
            list.append(str(hitInp))

            print(list)

        elif int(inp) + int(maxProb) > 21:
            print("STAND")

        else:
            print("Err: Invalid argument")
            print("\nExiting now with error code - (000x01a)")
            exit()

main()