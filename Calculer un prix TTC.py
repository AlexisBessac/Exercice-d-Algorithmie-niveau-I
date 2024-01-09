#Calculer le prix TTC

prix_ht = float(input("Veuiller saisir le prix ht en Euros : "))
quantite = int(input("Veuiller saisir la quantité : "))

prix_totalht = prix_ht*quantite

prix_totalht = prix_totalht-prix_totalht*(15/100)

tva = float(input("Saisir le taux de TVA en pourcentage : "))
prix_totalttc = prix_totalht+prix_totalht*(tva/100)

print(f"Le prix TTc est de {prix_totalttc} en euros")