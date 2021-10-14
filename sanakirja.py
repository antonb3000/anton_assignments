import json

try:
    with open("dictionary.json", "r") as f:
        sanakirja = json.load(f)

except OSError:
    print(f"Something went wrong opening the JSON file. Default dictionary loaded.")
    sanakirja = {"dog":"koira", "cat":"kissa"}

while True:
    sana = input("Please give me a word for Finnish translation (press Enter to exit and save given translations)\n> ")
    if not sana:
        with open ("dictionary.json", "w") as f:
            json.dump(sanakirja, f)
            break

    if sana in sanakirja:
        print(f"\n{sana} = {sanakirja[sana]}\n")
    else:
        print(f"\n{sana} not found.\n")
        definition = input("Please give a proper Finnish translation for " + f"{sana}".upper() + " or press Enter to cancel?\n> ")
        if definition:
            sanakirja[sana] = definition