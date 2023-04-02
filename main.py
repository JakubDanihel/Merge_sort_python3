#merge sort funguje tak ze rozdeli pole na mensie polia ktore sa nasledne porovnavaju medi sebou a triedia sa
#nasledne sa vsetky mensie polia zlucia do vacsich poli kde sa nasledne znova prekontroluje ich postupnost
import random

def mergeSort(pole):
    if (len(pole) > 1):
        #najdi stred pola
        stred = len(pole)//2

        #rozdelene pola na casti
        L = pole[:stred]
        R = pole[stred:]

        #triedenie prvej polovice s pouzitin znova tejto funkcie
        mergeSort(L)

        #triedenie druhej polo
        mergeSort(R)

        i = j = k = 0

        #skopirovanie udajov z docasneho pola L a R
        while ((i < len(L)) and (j < len(R))):
            if L[i] <= R[j]:
                pole[k] = L[i]
                i += 1
            
            else:
                pole[k] = R[j]
                j += 1
            k += 1

        #zisti ci sa v docasnych poliach nenachadzza ziadny dalsi element
        while(i < len(L)):
            pole[k] = L[i]
            i += 1
            k += 1
        while(j < len(R)):
            pole[k] = R[j]
            j += 1
            k += 1

#spustenie kodu
if __name__ == '__main__':
    #zadefinovanie pola
    velkost_pola = int(input("zadaj velkost pola: "))
    pole = [0]*velkost_pola
    #pouzivatelom zadana maximalna velkost ktoru moze v poli dosiahnut
    max_hod = int(input("Zadaj maximalnu hodnotu pre velkost pola: "))

    #naplnenie pola cislami
    for i in range(len(pole)):
        pole[i] = random.randint(0, max_hod)
    
    #vypisanie pola
    print("Neutriedene pole je: ", pole)
    mergeSort(pole)
    print("Utriedene pole je: ", pole)