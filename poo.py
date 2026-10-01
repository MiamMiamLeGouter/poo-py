class Personnage_3:
    def __init__(self, nb_vies, age):
        self.vie = nb_vies
        self.age = age


gollum = Personnage_3(15, 117)

print("gollum a", gollum.vie, "vies et il a", gollum.age, "ans.")
