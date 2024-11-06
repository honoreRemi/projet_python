#coding:utf-8

nb = 7
def tab(nb, max = 10) :
    i = 0

    while i < max :
        print(i + 1, '*', nb, '=', (i + 1) * nb)
        i += 1 # on incremente la valeur
tab(nb)