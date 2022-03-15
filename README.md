# Plan

| Data Structures | Algorithms | Concepts |
|----------|-------|-------|
| Linked Lists | Breadth-First-Search| Bit Manipulation|
|Trees, Tries, Graphs| Depth-First Search | Memory (Stack vs. Heap)|
|Stacks & Queues| Binary Search| Recursion|
|Heaps|Merge Sort|Dynammic Programming|
|Vectors/ArrayLists|Quick Sort| Big O Time&Space|
|Hash Tables|||

## 1. Documentation

2 x 45min sur un Google doc

Exercice simple pour commencer. Ensuite ils posent des questions genre : comment tu ferais pour accélérer l’exécution du programme ? qu’est-ce que tu ferais si les données étaient distribuées sur plusieurs machines ? Ils augmentent progressivement la difficulté

Vidéo d’exemple : https://www.youtube.com/watch?v=wwIysnVmAUg&t=526s

Le problème :
- **ECOUTER** : la moindre précision sur le problème est là pour une raison. “given two arrays that are sorted, find…”. Sorted not unsorted. Les précisions affectent la solution.
- **NOTER** ces précisions pour ne pas oublier 10min plus tard.
- **CLARIFICATIONS** demander des clarifications obligatoirement !!! Anticiper tous les cas chelous (est-ce que ça peut être des chiffres négatifs? est-ce que c’est des integer? Est-ce qu’il y a des exigences de complexité de temps ou d’espace ?)
DESSINER UN EXEMPLE 

La solution :
- **PENSER À HAUTE VOIX** penser à haute voix tout le process de réflexion que j’ai dans ma tête : doivent comprendre comment j’arrive à une solution. 
- **BRUTE FORCE** : expliquer la première solution. Dire pourquoi ça n’est pas la meilleure solution : space and time complexity
- **AMÉLIORER AVEC LE RECRUTEUR** quand j’ai trouvé une solution, essayer de l’améliorer avec l’interviewer, prendre tous ses tips, faire comme si c’était une discussion technique et pas un entretien
- **SAVOIR CLAIREMENT CE QUE JE VAIS CODER** : prends quoi en entrée ? quoi en sortie ?
- **CODER** code facile à lire et robuste
- **RELIRE CHAQUE LIGNE** : il ne semble pas y avoir d’erreur ?
- **TESTER** ses solutions : cas classiques, cas extrêmes, cas particuliers
- **FIXER LES PROBLÈMES** prendre son temps pour voir pourquoi on a fait cette erreur et si on fix de la bonne manière
- **J’ADORE RÉSOUDRE DES PROBLÈMES DIFFICILES** : ne pas give up même si je galère : montrer que je suis excitée de résoudre des problèmes difficiles

## 2. Data Structures

#### 2.1 Hash Tables
hash tables : particulièrement important. les tables de hashage : connaitre les détails sur 'l'utilisation de ces tables (ou maps ou dictionnaires) comment les consturire, comment les appliquer.  y a une légende que y aurait une question lors de l’entretien ou la réponse est table de hashage : y aura forcément un moment où y en aura beosin dans l’entretien. maps et dictionnaires

#### 2.2 Trees
Particulièrement important. Connaître les arbres, comment les construire, traverser des arbres. Algos de parcours des arbres, de manipulation. Se familisariser avec : 
- les abres binaires
- n-aryes
- tie-triees

#### 2.3 Min/Max Heaps
Comprendre comment les utiliser, identifier les problemes ou les heaps peuvent être utiles

#### 2.4 Graphs
linked lists

#### 2.5 Stacks, Queues, Sets
#### 2.6 Linked Lists

## 3. Algorithms
- savoir discuter de la space and time complexity. Savoir discuter de la complexité big O de mes solutions + penser à la complexité de la mémoire
- savoir discuter du sourcing et du hashage
- on peut etre invité à gérer des quantités de données obscenes : si on arrive faire tel truc avec 10 ou 100 articles, qu’est-ce qui pourrait changer si je fais ça avec un million ou un milliard d’articles ?
- connaître les détails d’au moins un algorithme de tri n*(log)n. Idéalement deux, donc quicksort et mergesort. mergesort peut parfois être pratique là ou quicksort l’est pas. Savoir quelles sont les fonctions de tri courantes. 
- sorting, searching, binary search
- divide-on-conquer
- dynamic programming and memorization
- greedy algorithms
- recursion
- graph traversal, breadth, and depth-first
- on devrait connaître NP-complete problems, like the traveling salesman and the knapsack + essayer de comprendre ce que signifie NP- complete
si on a le temps d’étudier le Djikstra ou A*, cela vous aidera probablement

## 4. Concepts

- algorithmes space and time complexity : Big O, savoir a quel point mon algorithme est complexe : en terme de temps et d’espace. Et savoir comment l’améliorer ou le modifier. the runtime. Think about the best conceivable runtime (discussed on page 72)
- programmation orientée objet
- questions de System Design and Scalability
- bit, comprendre l'allocation des ressources (ressources dont un processus ou un thread peut avoir besoin)context switching : il est initié dans l’OS, et le matériel sous-jacent. Voir powers of 2 table
- certains problèmes impliquent de penser de manière récursive. Pratiquer des problèmes qui peuvent être résolus de manière itérative, mais une solution plus élégante est la récursivité
- Systèmes d’exploitation : avoir une bonne compréhension des processus, les threads, les problèmes de concurrence et tout ce qui s’y rapporte (sémaphores, mutex, les verrous etc), toutes les construction du système d’exploitation standard, de leur fonctionnement, de la façon dont ils cassent, donc des impasses, des blocages etc. Comprendre comment fonctionne le changement de contexte d’un processus à lautre, comment l’OS le pilote
- on attend de vous que vous connaissiez les API
- load performances, security tests
- maths : certains itw poseront des problèmes de mathématiques discrets de base : prb de comptage, de probabilité, des choses qui arrivent dans la vie de tous les jours. Revoir l’essentiel de la théorie des probabilités et de la combinatoire
être familier avec les n k problèmes


## 5. Training

Be sure to check out Google code jam archives, GeeksforGeeks, HackerRank or CodeForces, where you can train your skills and get into the problem-solving mindset. 
clash of code de codingame

- Faire des tests avec des mauvais inputs pour voir si c’est solide
- try to solve problems on your own, sans chercher la solution sur internet : s’habituer à résoudre des problèmes
- write the code on a paper
- tester son code sur papier : cas généraux, cas basiques, cas d’erreur :s’attendre à des questions telles que : comment vous testeriez le code que vous venez d’écrire ? A quelles entrées ou cas de tests intéressants pouvez-vous penser ? 
- tapper son code tel qu'on l'a fait sur papier dans un oridnateur : voir ses erreurs et retenir les erreurs qu’on fait
- construire / parcourir des datas structures
- implement system routines
- prendre des ensemble de données volumineux et de les réduire d’une manière ou d’une autre
- faire une transformation sur un ensemble de données

Du code clean :
- le bon nom des variables. i et j c’est que pour des situations d’incrémentation pas pr autre chose
- au lieu de perdre du temps à initialiser une matrice, imaginer que y a une fonction qui le fait : initIncrementalMatrix(int size)
- Si je dois retourner deux listes, je peux renvoyer un tableau mais c’est préférable de renvoyer une liste d’objets



#### my working environment

1. Install brew
````
xcode-select -r
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
````

2. Install iTerm2, zsh, Oh My Zsh!
````
brew install iterm2
brew install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
upgrade_oh_my_zsh #to upgrade it
~/.zshrc #location zshrc
````
3. Configure vim
````
vim ~/.vimrc
````
