#### Imports et définition des variables globales
import sys

sys.setrecursionlimit(1100)


#### Fonctions secondaires
'''
doccod
'''


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée
      en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    cnt = []
    char = []
    n = len(s)
    result = []

    char.append(s[0])
    cnt.append(1)

    for i in range (1, n) :

        if s[i] == s[i-1] :
            cnt[-1] += 1

        else :

            char.append(s[i])
            cnt.append(1)

    for i in zip(char, cnt) :
        result.append(i)

    return result


def artcode_r(s):
    """retourne la liste de tuples encodant 
    une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici

    if not s:
        return []

    ref = s[0]
    cnt = 0

    while cnt < len(s) and s[cnt] == ref :
        cnt += 1
    return [ (ref, cnt) ] + artcode_r(s[cnt:])


    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif


#### Fonction principale


def main():
    '''
    jhvkjsdbvkdgsuicvljsjhbefg
    '''
    print(artcode_i("KKKX"))
    print(artcode_r("KKKX"))

if __name__ == "__main__":
    main()
