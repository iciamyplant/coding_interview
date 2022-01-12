#nombres complexes sont de la forme  z=a+ib, où a et b sont deux nombres réels
#ex : z=4+5i . Partie imaginaire vaut 5 et partie réelle 4

def complex_nb():
    a = 8 + 5j #une partie réelle et une partie imaginaire
    print(type(a))
    print('Real Part a = ', a.real)
    print('Imaginary Part a = ', a.imag)
    print('Conjugate a = ', a.conjugate())
    b = complex(10,2)
    print('Real Part b = ', b.real)
    print('Imaginary Part b = ', b.imag)
    print('Conjugate b = ', b.conjugate())    
    c = (b.imag + a.imag) #additionne les deux parties reelles
#a + b = (8+10)+(5+2)i. Soit 18+7i
    d=(b+ a)
    print("c =", c)
    print("d =", d)


complex_nb()
#hashing


