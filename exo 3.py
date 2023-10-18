def myTable(tab):
    n = len(tab)
    #Traverse tout les elements
    for i in range(n):
        for j in range(0, n-i-1):
            # echanger si il est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]


#test du code
tab = [10,25,4,14,20,30,40,1]

myTable(tab)

print ("le tableau trié est")
for i in range(len(tab)):
    print ("%d" %tab[i])

#
import array as arr

tab = arr.array('i', [10,25,4,14,20,30,40,1])

for i in tab:
    print(i)