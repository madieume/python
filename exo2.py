def nettoyer_phrase(phrase):
    # Supprimer les espaces en début et fin, et remplacer les multiples espaces internes par un seul espace
    return ' '.join(phrase.split())

def main():
    # Saisie de la phrase par l'utilisateur
    phrase = input("Entrez une phrase : ")
    
    # Nettoyer la phrase
    phrase_nettoyee = nettoyer_phrase(phrase)
    
    # Afficher la phrase nettoyée
    print("Phrase nettoyée :", phrase_nettoyee)

# Appeler la fonction principale
main()