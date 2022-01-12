#Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys

def dict_dec():
    dic ={}#A pair of braces creates an empty dictionary: {}
    dic2 = {'jack': 4098, 'sape': 4139} #key:value
    print(dic2)
    dic2['guido'] = 4127#j'ajoute une key:value au dictionnaire
    print(dic2)
    print(list(dic2)) #list(dic) donne les keys sous forme de liste
    del dic2['sape'] #supprime la key:value sape
    print('guido' in dic2) #True
    #print(dic2[0]) #je ne peux pas utiliser les indices, erreur
    n1 = dict(valeur=15, coefficient=1.5, matiere="programmation")
    print("valeur" in n1) #renvoie true
    print("n1 =", n1)
    print("n1['valeur'] = ", n1['valeur'])

def huge_dict():
    dic={'anglais':[10],'francais':[15],'maths':[13]} #notes en premiere années
    print(dic)
    for key in dic.keys():
        print(key)
    for i in range(2): #notes en 2ème et 3ème année
        dic['anglais'].append(dic['anglais'][i]+2) #maéliorée de 2 points chaque année
        dic['francais'].append(dic['francais'][i]+1) #de 1 point
        dic['maths'].append(dic['maths'][i]+3) #de 3 points
    print(dic)

    test = [i for key,v, in dic.items() for i in v] #[10, 12, 14, 15, 16, 17, 13, 16, 19]
    test = [v for key,v, in dic.items()] #[[10, 12, 14], [15, 16, 17], [13, 16, 19]]
    test = [key for key in dic.items()] #[('anglais', [10, 12, 14]), ('francais', [15, 16, 17]), ('maths', [13, 16, 19])]
    test = [key for key in dic] #['anglais', 'francais', 'maths']
    print(test)

    dic2={'notesbyeleve':[(10,'eleve1'),(14,'eleve3'),(11,'eleve4'),(14,'eleve3')]}
    #print(sorted(set(dic2['notes'])))
    print(sorted(set(dic2['notesbyeleve']))) #sorted pour ordre croissant + set pour elenver le doublon
    
#dict_dec()
huge_dict()