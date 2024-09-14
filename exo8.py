# Liste pour stocker les étudiants
etudiants = []

# Fonction pour demander et valider les informations de l'étudiant
def ajouter_etudiant():
    while True:
        telephone = input("Entrez le numéro de téléphone unique : ")
        if not telephone.isdigit() or len(telephone) != 9:
            print("Le numéro de téléphone doit contenir 9 chiffres.")
            continue
        if any(etudiant['telephone'] == telephone for etudiant in etudiants):
            print("Ce numéro de téléphone existe déjà.")
            continue
        
        nom = input("Entrez le nom : ")
        prenom = input("Entrez le prénom : ")
        classe = input("Entrez la classe : ")
        
        try:
            note_devoir = float(input("Entrez la note de devoir (0-20) : "))
            note_projet = float(input("Entrez la note de projet (0-20) : "))
            note_examen = float(input("Entrez la note d'examen (0-20) : "))
            if not (0 <= note_devoir <= 20 and 0 <= note_projet <= 20 and 0 <= note_examen <= 20):
                print("Les notes doivent être entre 0 et 20.")
                continue
        except ValueError:
            print("Veuillez entrer des notes valides.")
            continue
        
        moyenne = round((note_devoir + note_projet + note_examen) / 3, 2)
        
        etudiants.append({
            "telephone": telephone,
            "nom": nom,
            "prenom": prenom,
            "classe": classe,
            "note_devoir": note_devoir,
            "note_projet": note_projet,
            "note_examen": note_examen,
            "moyenne": moyenne
        })
        
        continuer = input("Voulez-vous ajouter un autre étudiant ? (o/n) : ").lower()
        if continuer != 'o':
            break

# Fonction pour afficher tous les étudiants
def afficher_etudiants():
    if etudiants:
        print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            "Téléphone", "Nom", "Prénom", "Classe", "Devoir", "Projet", "Examen", "Moyenne"))
        for etudiant in etudiants:
            print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                etudiant['telephone'], etudiant['nom'], etudiant['prenom'], etudiant['classe'],
                etudiant['note_devoir'], etudiant['note_projet'], etudiant['note_examen'], etudiant['moyenne']))
    else:
        print("Aucun étudiant trouvé.")

# Fonction pour trier et afficher par ordre décroissant de la moyenne
def trier_etudiants():
    if etudiants:
        etudiants_tries = sorted(etudiants, key=lambda x: x['moyenne'], reverse=True)
        afficher_etudiants()
    else:
        print("Aucun étudiant trouvé.")

# Fonction pour rechercher un étudiant
def rechercher_etudiant():
    critere = input("Rechercher par (telephone, nom, prenom, classe) : ").lower()
    valeur = input(f"Entrez la valeur pour {critere} : ")
    
    resultats = [etudiant for etudiant in etudiants if etudiant[critere] == valeur]
    if resultats:
        afficher_etudiants()
    else:
        print("Aucun étudiant trouvé pour ce critère.")

# Fonction pour modifier les notes d'un étudiant
def modifier_notes():
    telephone = input("Entrez le numéro de téléphone de l'étudiant à modifier : ")
    etudiant = next((etudiant for etudiant in etudiants if etudiant['telephone'] == telephone), None)
    
    if etudiant:
        try:
            etudiant['note_devoir'] = float(input("Entrez la nouvelle note de devoir (0-20) : "))
            etudiant['note_projet'] = float(input("Entrez la nouvelle note de projet (0-20) : "))
            etudiant['note_examen'] = float(input("Entrez la nouvelle note d'examen (0-20) : "))
            if not (0 <= etudiant['note_devoir'] <= 20 and 0 <= etudiant['note_projet'] <= 20 and 0 <= etudiant['note_examen'] <= 20):
                print("Les notes doivent être entre 0 et 20.")
                return
            etudiant['moyenne'] = round((etudiant['note_devoir'] + etudiant['note_projet'] + etudiant['note_examen']) / 3, 2)
            print("Notes mises à jour avec succès.")
        except ValueError:
            print("Entrée invalide pour les notes.")
    else:
        print("Aucun étudiant trouvé avec ce numéro de téléphone.")

# Fonction principale pour afficher le menu
def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Afficher tout")
        print("2. Trier et afficher (par ordre décroissant de la moyenne)")
        print("3. Rechercher un étudiant")
        print("4. Modifier les notes d'un étudiant")
        print("5. Sortir")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            afficher_etudiants()
        elif choix == "2":
            trier_etudiants()
        elif choix == "3":
            rechercher_etudiant()
        elif choix == "4":
            modifier_notes()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Exécution du programme
ajouter_etudiant()
menu()
