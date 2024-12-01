import requests
print("enter 'stop' to stop the program!")
while(True):
    pokemon = input("\nPlease enter your pokemon name: ")
    if(pokemon=="stop"):
        break
    
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    request = requests.get(url) # Step 1 : fetch the data
    if request.status_code==200:
        data = request.json() # Step 2 : store it in json

        # Types
        print("\nTypes:")
        print(len("Types:")*'-')
        for type in data["types"]:
            print(f"- {type["type"]["name"]}")

        # Abilities
        print("\nAbilities:")
        print(len("Abilities:")*'-')
        for ability in data["abilities"]:
            print(f"- {ability["ability"]["name"]}")

        #Stats
        print("\nStats:")
        print(len("Stats:")*'-')
        for stat_data in data["stats"]:
            stat=stat_data["stat"]["name"]
            base_stat=stat_data["base_stat"]
            print(f"- {stat}:{base_stat}")
        # print("\n")

    else:
        print("The pokemon not found...\n")    
