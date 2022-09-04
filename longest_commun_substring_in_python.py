def intersection(s, t):
    """
    Cette fonction calcule l’intersection entre deux chaînes de caractères s et t.
    On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots.
    Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.
    Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans s.
    """
    L = [[0 for i in range(len(t))] for i in range(len(s))]
    z = 0
    ret = 0

    for i in range(len(s)):
        for j in range(len(t)):
            if (s[i]==t[j]):
                if ((i == 0) or (j == 0)):
                    L[i][j] = 1
                else:
                    L[i][j] = L[i-1][j-1] + 1
                if L[i][j] > z:
                    z = L[i][j]
                    ret = i

    return s[ret-z+1:ret+1]

# Test
print(intersection('programme', 'grammaire')) # retourne 'gramm'
print(intersection('bbaacc', 'aabb')) # Retourne 'bb' (Sous-chaine d'indice minimal
print(intersection('salut', 'merci')) # Retourne '' (vide)
print(intersection('merci', 'adieu')) # Retourne 'e'
