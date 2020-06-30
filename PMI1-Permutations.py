# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import copy


def factorielle(n):
    if n==1: #fin de la récursivité lorsque n=1
        return 1
    else:
        return n*factorielle(n-1) #utilisation de la récursivité pour avoir le factorielle

def traductions_avec_message(): #fonctionne pour tout n, et n'affiche pas les coefficients qui valent 0
    n=input("Nombre entier positif à décomposer : ")
    while n.isnumeric()==False: #en cas de saisie non numérique (lettre...), on demande à l'utilisateur une autre saisie
        print("Saisie invalide !")
        n=input("Nombre entier positif à décomposer : ")
    n=int(n) #on transforme la chaîne de caractère entrée par l'utilisateur en nombre entier
    message = str(n) + " s'écrit " #préparation du message à retourner à l'utilisateur
    dividende=n
    fact_max=1
    while dividende//fact_max > fact_max: #détermination de la valeur du plus grand factorielle de la décomposition (voir divisions)
        dividende=dividende//fact_max
        fact_max+=1
    coeff = list((fact_max*[None])) #on créer une liste vide pour les coefficients des factorielles
    for i in range(fact_max,0,-1): #formation de la liste coeff qui mémorise tous les coefficients
        coeff[i-1] = n//factorielle(i)
        n = n%factorielle(i) #la nouvelle valeur de n correspond au reste de la division
        if coeff[i-1]!=0: #fabrication du message, on ajoute les coefficients seulement s'ils ne sont pas nuls
            message = message + str(coeff[i-1]) + "." + str(i) + "!"
            message = message + "+"
    if message[-1]=="+": #on enlève le dernier signe "+" pour avoir une affichage propre
        message = message[:-1]
    return message


def traductions(n):
    dividende=n
    fact_max=1
    while dividende//fact_max > fact_max: #détermination de la valeur du plus grand factorielle de la décomposition (voir divisions)
        dividende=dividende//fact_max
        fact_max+=1
    coeff = list((fact_max*[None])) #on créer une liste vide pour les coefficients des factorielles
    for i in range(fact_max,0,-1):
        coeff[i-1] = n//factorielle(i)
        n = n%factorielle(i) #la nouvelle valeur de n correspond au reste de la division
    return coeff # 119ème rang ---> [1,2,3,4] ---> 1*1!+2*2!+3*3!+4*4!


def initialisation_5_lettres(): #choix du modèle + refus si pas 5 lettres + on ordonne le modèle
    modèle=input("Liste des caractères souhaités à l'écriture (en donner 5) : ")
    while len(modèle)!=5: #en cas de mauvaise saisie, on en redemande une
        print("Il n'y a pas 5 lettres ! Essayer de nouveau.")
        modèle=input("Liste des caractères souhaités à l'écriture (en donner 5) : ")
    modèle = list(modèle)
    modèle.sort() #pour avoir les permutations dans l'ordre alphabétique ou numérique
    return modèle


def permutations_5_lettres():
    modèle = initialisation_5_lettres() #on récupère le modèle entré par l'utilisateur, dans l'ordre alphabétique ou numérique
    rang=input("Choix du rang de la permutation (entre 1 et 120): ") #rang de la permutation choisi par l'utilisateur
    if rang.isnumeric()==False: #si l'utilisateur ne rentre pas un nombre, rang=0 pour engendrer une mauvaise saisie
        rang=0
    while int(rang)<1 or int(rang)>120: #en cas de mauvaise saisie, on en redemande une
        print("Erreur dans le choix du rang ! Essayer de nouveau.")
        rang=input("Choix du rang de la permutation (entre 1 et 120): ")
        if rang.isnumeric()==False:
            rang=0
    coeff = traductions(int(rang)-1) #si l'utilisateur demande le 120ème rang, on cherche liste[119] car une liste commence à liste[0]
    mot = list() #on défini "mot" comme une liste qui va se former lettre par lettre
    for i in range (3,-1,-1):#de 3 à 0
        try:
            mot.append(modèle[coeff[i]]) #explication sur le compte-rendu
            modèle.remove(modèle[coeff[i]])
        except:
            mot.append(modèle[0]) #explication sur le compte-rendu
            modèle.remove(modèle[0])
    mot.append(modèle[0])
    mot = mot[0]+mot[1]+mot[2]+mot[3]+mot[4] #on transforme la liste "mot" en chaîne de caractère formant la permutation
    return mot


def liste_permutations_5_lettres():
    modèle_fixe = initialisation_5_lettres() #on récupère le modèle entré par l'utilisateur, dans l'ordre alphabétique ou numérique
    liste = list()
    for i in range(factorielle(5)):#de 0 à 119
        coeff = traductions(i) #coeff est la liste des coefficients des factorielles pour un rang donné (ex: 119ème rang = [1,2,3,4])
        mot = list() #on défini "mot" comme une liste qui va se former lettre par lettre
        modèle = copy.copy(modèle_fixe) #modèle copie modèle_fixe sans le modifier
        for i in range (3,-1,-1):#de 3 à 0
            try:
                mot.append(modèle[coeff[i]]) #explication sur le compte-rendu
                modèle.remove(modèle[coeff[i]])
            except:
                mot.append(modèle[0]) #explication sur le compte-rendu
                modèle.remove(modèle[0])
        mot.append(modèle[0])
        mot = mot[0]+mot[1]+mot[2]+mot[3]+mot[4] #on transforme la liste "mot" en chaîne de caractère formant la permutation
        liste.append(mot) #"liste" récupère toutes les permutations pour les renvoyer à l'utilisateur à la fin de la fonction
    return liste


def initialisation_n_lettres(): #choix du modèle + refus si plus de 8 lettres + on ordonne le modèle
    modèle=input("Liste des caractères souhaités à l'écriture (maximum 8 lettres) : ")
    while len(modèle)>8: #en cas de mauvaise saisie, on en redemande une
        print("Il y a plus de 8 lettres ! Essayer de nouveau.")
        modèle=input("Liste des caractères souhaités à l'écriture (maximum 8 lettres) : ")
    modèle = list(modèle)
    modèle.sort() #pour avoir les permutations dans l'ordre alphabétique ou numérique
    return modèle


def permutations_n_lettres():
    modèle = initialisation_n_lettres() #on récupère le modèle entré par l'utilisateur, dans l'ordre alphabétique ou numérique
    taille = len(modèle)
    print("Choix du rang de la permutation ( entre 1 et",factorielle(taille),"): ") #on demande un rang comptatible avec le nombre de permutations
    rang=input()
    if rang.isnumeric()==False: #si l'utilisateur ne rentre pas un nombre, rang=0 pour engendrer une mauvaise saisie
        rang=0
    while int(rang)<1 or int(rang)>factorielle(taille): #en cas de mauvaise saisie, on en redemande une
        print("Erreur dans le choix du rang ! Essayer de nouveau.")
        print("Choix du rang de la permutation (entre 1 et",factorielle(taille),"): ")
        rang=input()
        if rang.isnumeric()==False:
            rang=0
    coeff = traductions(int(rang)-1) #si l'utilisateur demande le 120ème rang, on cherche liste[119] car une liste commence à liste[0]
    #print(coeff) #permet le débuggage
    mot = list() #on défini "mot" comme une liste qui va se former lettre par lettre
    for i in range (taille-2,-1,-1):#si on a un mot de 8 lettres, on aura 7 coefficients avec 6 sous-listes
        try:
            mot.append(modèle[coeff[i]]) #explication sur le compte-rendu
            modèle.remove(modèle[coeff[i]])
        except:
            mot.append(modèle[0]) #explication sur le compte-rendu
            modèle.remove(modèle[0])
    mot.append(modèle[0])
    permutation = str()
    for i in range (taille):#si on a un mot de 8 lettres, on aura 7 coefficients
        permutation = permutation + str(mot[i]) #permutation est une chaîne de caractères qui se forme avec les lettres de la liste "mot"
    return permutation


def liste_permutations_n_lettres():
    modèle_fixe = initialisation_n_lettres() #on récupère le modèle entré par l'utilisateur, dans l'ordre alphabétique ou numérique
    liste = list()
    taille = len(modèle_fixe)
    for i in range(factorielle(taille)):
        coeff = traductions(i) #coeff est la liste des coefficients des factorielles pour un rang donné (ex: 119ème rang = [1,2,3,4])
        mot = list() #on défini "mot" comme une liste qui va se former lettre par lettre
        modèle = copy.copy(modèle_fixe) #modèle copie modèle_fixe sans le modifier
        for j in range (taille-2,-1,-1): #si on a un mot de 8 lettres, on aura 7 coefficients avec 6 sous-listes
            try:
                mot.append(modèle[coeff[j]]) #explication sur le compte-rendu
                modèle.remove(modèle[coeff[j]])
            except:
                mot.append(modèle[0]) #explication sur le compte-rendu
                modèle.remove(modèle[0])
        mot.append(modèle[0])
        permutation = str()
        for i in range (taille): #si on a un mot de 8 lettres, on aura 7 coefficients
            permutation = permutation + str(mot[i]) #permutation est une chaîne de caractères qui se forme avec les lettres de la liste "mot"
        liste.append(permutation) #"liste" récupère toutes les permutations pour les renvoyer à l'utilisateur à la fin de la fonction
    envoi(liste)
    return liste

print(liste_permutations_n_lettres())

def envoi(liste):
    réponse = input("Envoyer les permutations sur un fichier Résultat (O/N) ? ") #proposition à l'utilisateur
    while réponse != "O" and réponse != "N": #tant que sa réponse n'est pas correcte, on lui repose la question
        print("Saisie invalide !")
        réponse = input("Envoyer les permutations sur un fichier Résultat (O/N) ? ")
    #ouverture d'un fichier "Résultats.txt" afin d'écrire éventuellement les permutations dessus
    with open("Résultats.txt",'w',encoding="utf_8_sig") as f: #on écrit tout d'abord le nombre de permutations
        if réponse == "O": #si l'utilisateur répond "O" pour "oui"
            f.write("Nombre de permutations : "+str(len(liste))+2*"\n") #on écrit tout d'abord le nombre de permutations
            for i in range(len(liste)):
                if i%6 == 5: #on écrit sur le fichier en sautant une ligne toutes les 6 permutations
                    f.write(liste[i]+"\n")
                else:
                    f.write(liste[i]+"   ")
        else:
            f.write("") #si l'utilisateur répond "N" pour "non", on écrit rien sur le fichier


def max_min(): #recherche du maximum et du minimum d'une fonction définie sur l'ensemble des anagrammes
    resultat=list()
    liste=liste_permutations_5_lettres() #on récupère la liste des permutations du mot de 5 lettres entré par l'utilisateur
    while liste[0].isnumeric()==False: #en cas de chaîne de caractères non numérique, on redemande une saisie
        print("Chaîne non numérique")
        liste=liste_permutations_5_lettres()

    #CHOIX COEFF FONCTION
    facteurs = list(5*[None]) #on créer une liste vide pour les facteurs de chaque caractère
    for i in range(5):
        message="Coefficient n°"+str(i+1)+" : "
        facteurs[i] = input(message)  #on demande à l'utilisateur la valeur qu'il souhaite attribuer à chaque facteur
        while facteurs[i].isnumeric()==False: #si le facteur entré n'est pas numérique, on redemande une saisie
            print("Saisie invalide !")
            facteurs[i] = input(message)
        facteurs[i]=int(facteurs[i]) #puis, on transforme le facteur entré par l'utilisateur en nombre entier
    #liste des images en fonction des anagrammes
    for k in range (len(liste)):
        resultat.append(facteurs[0]*int(liste[k][0]) + facteurs[1]*int(liste[k][1]) + facteurs[2]*int(liste[k][2]) + facteurs[3]*int(liste[k][3]) + facteurs[4]*int(liste[k][4]))#liste[k][n]k pour l'anagramme,n pour la lettre

    dicouple = dict(zip(liste,resultat)) #création d'un dictionnaire (liste des permutations, coûts)
    liste1, resultat1 = max(dicouple.items(), key = lambda p: p[1])#p:p[0]=maximum pour liste1, p:p[1]=maximum pour résultat1
    liste2, resultat2 = min(dicouple.items(), key = lambda p: p[1])

    #GRAPHIQUE
    plt.plot(liste, resultat, "r-",marker = ".",color = "cyan", linewidth = 1)
    plt.xlabel("Anagramme")
    plt.ylabel("Image")
    plt.xticks(rotation = 'vertical')
    plt.tick_params(axis = 'x', labelsize = 3)

    #Pour sauvegarder le graphe
    #plt.figure(1, figsize=(19, 6)) #19inches de long, le 1 pour dire que c'est la figure numéro 1
    #plt.savefig('Anagramme.png',dpi=600) #dpi point par inche

    plt.show()

    message = "Le maximum est atteint avec l'anagramme " + str(liste1) + ". Il a pour valeur " + str(resultat1) + "." + "\n"
    message = message + "Le minimum pour l'anagramme " + str(liste2) + ". Il a pour valeur " + str(resultat2) + "."
    return message


def programme_principal(): #utilisation d'un programme principal pour créer une interface facile à utiliser pour l'utilisateur
    print("***** PROJET MATHS-INFO - PERMUTATIONS *****") #série d'affichages proposant 6 options différentes à l'utilisateur
    print("1 : Ecrire la décomposition en somme de factorielles d'un nombre")
    print("2 : Ecrire la permutation d'un mot de 5 lettres pour un rang donné")
    print("3 : Ecrire toutes les permutations d'un mot de 5 lettres")
    print("4 : Ecrire la permutation d'un mot de n lettres pour un rang donné")
    print("5 : Ecrire toutes les permutations d'un mot de n lettres (avec envoi optionnel sur un fichier)")
    print("6 : Rechercher le maximum d'une fonction définie sur l'ensemble des anagrammes")
    m=input("Que souhaitez-vous faire ? (sélectionner un chiffre entre 1 et 6) : ") #l'utilisateur doit ensuite faire son choix
    while m!="1" and m!="2" and m!="3" and m!="4" and m!="5" and m!="6": #en cas de mauvaise saisie, on en redemande une
        print("Saisie non valide !")
        m=input("Que souhaitez-vous faire ? (sélectionner un chiffre entre 1 et 6) : ")
    if m==("1"): #suivant le choix effectué par l'utilisateur, on lance la fonction adaptée
        return traductions_avec_message()
    if m==("2"):
        return permutations_5_lettres()
    if m==("3"):
        return liste_permutations_5_lettres()
    if m==("4"):
        return permutations_n_lettres()
    if m==("5"):
        return liste_permutations_n_lettres()
    if m==("6"):
        return max_min()

print(programme_principal())
