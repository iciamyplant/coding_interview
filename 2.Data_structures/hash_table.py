#Hash table is a type of data structure that maps keys to its value pairs
#makes accessing data faster as the index value behaves as a key for data value
#It is implemented through built-in dictionary data type.

#imagine j'ai une liste cest ca liste = Jan, Tim, Mia, Sam, Leo, Ted, Ada
#si je veux trouver Ada faut je teste chaque nom avant, sur une enorme bdd ca va durer lgtp
#par contre si je connais le numéro d'index 6, je vais trouver rapidement peut importe la taille de l'array
#hash_table =========>  chaque index peut etre calculé à partir de la valeur elle meme
# par ex pour Mia : M c'est 77, i 105, a 97, = 279 % nb delts dans la table ici 11 = 4. L'indice de Mia est 4

####with numeric keys : divide the key by the number of available addresses,n, and take the remainder
#### address = key Mod n
#def hash_function():


####with alphanumeric keys : divide the sum of ASCII codes in a key by the number of available addresses,n,and take the remainder


####folding method : un numero de tel peut etre divisé groupes de 2, ceux-ci peuvent etre additionnés, on peut diviser par une constante, puis prendre le remainder
####01 + 45 + 28 + 34 + 56 + 54 = 218. 218/15 = 8



##collisions : ca peut générer le meme index. Dans ce cas on fait un open adressing. 
#open adressing = variété de techniques pour placer là ou n'est pas censé etre. Par ex, on place à la premiere place disponible aprex l'index quon avait trouvé = linear research
#le mieux est davoir une table de hashage + grande où 70% est occupé. load factor = totalnomberofitemssotred/size of the array. On peut faire une table de hashage avec une mémoire dynamique selon le load array
#tant que le load array est raisonnable, la linear search ca va
# autre moyen d'open adressing : chaining

def main():
    s = "ababcd"