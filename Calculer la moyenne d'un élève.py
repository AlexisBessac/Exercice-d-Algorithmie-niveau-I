#Calculer la moyenne d'un élève

fr = float(input("Veuiller saisir la note de français sur 20 :"))
maths= float(input("Veuiller saisir la note de maths sur 20 :"))
geometrie= float(input("Veuiller sasir la note de géométrie sur 20 : "))
informatique= float(input("Veuiller saisir la note d'informatique sur 20 : "))

Moyenne= (fr+maths+geometrie+informatique)/4

print(f"Vous avez {Moyenne} sur 20 de moyenne")