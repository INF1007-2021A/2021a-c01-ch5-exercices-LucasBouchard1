#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    return (number**2)**0.5


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    return [x+suffixe for x in prefixes]


def prime_integer_summation() -> int:
    nombre_premiers = []
    i = 2
    
    while len(nombre_premiers)<100:
        add = True
        for j in range(1,int(round(i/2,0))):
            if j != 1:
                if i%j==0:
                    add = False
                    break

        if add:
            nombre_premiers.append(i)
        i+=1
    return nombre_premiers


def factorial(number: int) -> int:
    result = 1
    for x in range(1,number + 1):
        result*=x
    return result


def use_continue() -> None:
    for x in range(10):
        if x==5:
            continue
        print(x)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    final = []
    for liste in groups:
        if (11>len(liste)>3 or min(liste)<18 or (max(liste)>70 and 50 in liste)) and 25 not in liste:
            final.append(False)
        final.append(True)
             
    return final


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
