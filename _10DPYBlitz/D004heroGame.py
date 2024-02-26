
hero_name = input("Give your hero a name, courageous adventurer? >")

the_hero = {
    "name" : hero_name,
    "xp" : 0,
    "level" : 1,
    "money" : 5,
    "atk_p" : 5,
    "def_p" :2,
    "hp" : 10,
    "mp" : 5,
    "weapon" : "punch",
    "inventory" : ["health_potion",]
}

game_on = True
while(game_on):
    print(f"What would you like to do, {the_hero['name']}?")
    print(f"1. Fight a monster to gain XP")
    print(f"2. Go to the shop")
    print(f"3. Polish your weapon")
    print(f"4. Rest in hotel")
    action = input(" > ")
    if(action == "3"):
        game_on = False
        print("Exit Game")