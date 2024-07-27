def afficher_mois(mois):
    # Afficher les mois en 4 colonnes et 3 lignes
    for i in range(3):
        print("{mois[i]} {mois[i+3]} {mois[i+6]} {mois[i+9]}")

def menu():
    # Tableau des mois en français
    mois_fr = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", 
               "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    
    # Tableau des mois en anglais
    mois_en = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
    
    # Affichage du menu 
    print("Choisissez la langue:")
    print("f - Français")
    print("a - Anglais")
    
    choix = input("Entrez votre choix (f/a): ").strip().lower()
    
    # Affichage des mois selon le choix de l'utilisateur
    if choix == 'a':
        afficher_mois(mois_en)
    else:
        afficher_mois(mois_fr)


# Appel de la fonction principale
menu()