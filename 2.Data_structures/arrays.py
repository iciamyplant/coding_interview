def array_dec():
    transposed = []
    print("declarer avec variable = []")

def array_methods():
    print("################    ARRAYS    ################\n")
    #List_A = [item 1, list_B, item 3….., item n]
    list_test = [1, 2.2, 'c', 4, "32"]
    print("list_test =", list_test)
    list_test.append(5) #Add an item to the end of the list
    print('.append(5) =', list_test)
    list_2 = ['a', 'b', 'c']
    list_test.extend(list_2) #ajoute l'arg à list
    print('.extend(list_2) =', list_test)
    list_test.insert(3, 'x') #insert le 2ème arg à l'indice du premier arg
    print(".insert(3, 'x') =", list_test)
    list_test.remove('x') #Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item
    #list_test.clear() #efface tout ce qui est dand la liste
    print(".remove('x') =", list_test)
    print(".list_test.count('c') = ", list_test.count('c')) #compte nombre de fois où l'arg est present dans la liste
    list_test_nbrs = [17, 1, 44, 29, 12, 6, 55]
    list_test_nbrs.sort(key=None, reverse=False) #arrive pas a sort si dans la liste y a des types des variabels de different types
    print(".sort(key=None, reverse=False)", list_test_nbrs)

def array_comprehension(): ##concise way to create lists
    print("\n################    ARRAYS COMPREHENSION    ################\n")
    ###[... for ... in ...] retourne la liste de ... for ... in ...
    squares = [x**2 for x in range(10)]
    two_lists = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y] 
    print("squares = [x**2 for x in range(10)]   =", squares) #list of squares without doing a loop
    print("two_lists = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]  =", two_lists) #combines the elements of two lists if they are not equal
    vec = [-4, -2, 0, 2, 4]
    print([x*2 for x in vec])
    print([x for x in vec if x >= 0]) #filter the list to exclude negative numbers
    print([abs(x) for x in vec]) #apply a function to all the elements
    print([(x, x**2) for x in range(6)]) #create a list of 2-tuples like (number, square)
    from math import pi
    [str(round(pi, i)) for i in range(1, 6)] #1 chiffre apres virg, 2chiffres,..
    vec = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],] #matrix 3x4
    [num for elem in vec for num in elem]
    print("matrix =", vec)

def array_behaviour():
    list_test = [1,2,3,4,5,6,7]
    print(list_test[1:3])     # Prints elements de list_test[1] jusqu'à list_test[3] non compris
    print(list_test[2:])      # Prints elements de list_test[2] jusqu'à la fin  #3,4,5,6,7
    print(list_test[:2])      # Prints elements du début jusqu'à list_test[2] non compris #1,2

def main_array():
    array_methods()
    array_comprehension()
    array_behaviour()
    array_dec()


#print("################    STACK    ################\n") #pile
#Last-in-First-Out
#to implement en stack we need two simple operations :
#push, adds an element to the top of the stack
#pop, removes the element at the top of the stack

#print("################    QUEUE    ################\n") #file d'attente
#First-in-First-Out : the first one to stand in line is the first one to buy a ticket and enjoy the movie
#To implement a queue we need two simple operations:
#enqueue - adds an element to the end of the queue
#dequeue - removes the element at the beginning of the queue

##utiliser dnas des contextes particuliers : genre si je fais un traitement de texte et que l'utilisateur veut annuler ses dernières actions une à une
#It's common for Stacks and Queues to be implemented with an Array or Linked List

def main_queues_stacks():
    print("################    QUEUES AND STACKS    ################\n")
    letters = []
    # Let's push some letters into our list
    letters.append('c')
    letters.append('a')
    letters.append('t')
    letters.append('g')
    print(letters)
    # Let's pop like a stack behavior
    last_chr = letters.pop() #teje de l'objet le dernier item et retourne ce dernier item
    print(last_chr)
    print(letters)
    #last_chr = letters.push('1')
    #print(letters)
    # Let's pop like a queue behavior
    letters.pop(0)
    letters.pop(1) # on met l'indice qu'on veut dans pop
    print(letters)


#print("################    SETS    ################\n")
#set is an unordered collection with no duplicate elements

def main_sets():
    a = set('abracadabra')
    b=set('coucou')
    c={'test'} #declaration d'un set
    print(type(c))
    print(a,b)
    print(a - b) #letters in a but not in b
    print(a | b) #letters in a or b or both
    print(a & b) # letters in both a and b #=union
    print(a ^ b) # letters in a or b but not both #=inter

def main_tuples():
    print ("\n################    TUPLES    ################\n") #est une valeur composée de plusieurs valeurs
    n1 = (15, 1.5, "programmation")
    print("n1 =", n1)
    print("n1[0] =", n1[0])
    #n1[0] = 12 # on peut pas faire ça, impossible de changer une valeur d'un tuple faut en créer un nouveau

#main_array()
#main_queues_stacks()
main_sets()
#main_tuples()


