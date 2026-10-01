class Personnage_2:
    def __init__(self, nb_vies):
        self.vie = nb_vies


gollum = Personnage_2(15)
bilbo = Personnage_2(20)

print("Vie de Gollum :", gollum.vie)
print("Vie de Bilbo :", bilbo.vie)