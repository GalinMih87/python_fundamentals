number_of_lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shild_price = float(input())
armor_price = float(input())

total_helmets_broken = number_of_lost_fight // 2
total_sword_broken = number_of_lost_fight // 3
total_shild_broken = number_of_lost_fight // 6
total_armor_broken = total_shild_broken // 2
expenses = total_helmets_broken * helmet_price + total_sword_broken * sword_price + total_shild_broken * shild_price + \
           total_armor_broken * armor_price

print(f"Gladiator expenses: {expenses:.2f} aureus")