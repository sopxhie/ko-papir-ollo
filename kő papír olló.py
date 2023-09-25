import random

ok1 = input("kő, papír vagy olló?:")
ok2 = random.choice(["kő", "papír", "olló"])
print("a gép választása:", ok2)

if ok1 == ok2:
    print("ugyan azt választottátok")
if ok1 == "kő" and ok2 == "papír":
    print("az első játékos nyert")
if ok2 == "kő" and ok1 == "papír":
    print("a második játékos nyert")
if ok1 == "kő" and ok2 == "olló":
    print("a második játékos nyert")
if ok1 == "olló" and ok2 == "kő":
    print("az első játékos nyert")
if ok1 == "papír" and ok2 == "olló":
    print("a második játékos nyert")
if ok1 == "olló" and ok2 == "papír":
    print("az első játékos nyert")
else:
    print("nincs ilyen lehetőség")