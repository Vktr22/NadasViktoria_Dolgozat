import random
import math

def elso_feladat():
    bekertszam = int(input("Kérek egy páros számot! "))
    while bekertszam % 2 != 0:
        bekertszam=int(input("Ez nem páros! PÁROS számot kérek! "))
    print(bekertszam)

def masodik_feladat():
    i:int = 0
    harommaloszthato = 0
    while i < 13:
        szam: int = math.floor(random.random()*140 +10)
        print(szam, end=" ")
        if szam % 3 == 0:
            harommaloszthato += 1
        i+=1
    print("")
    print("A számok között " +str(harommaloszthato)+ "db 3-al osztható van!")

def harmadik_feladat():
    be_szoveg = input("Adj meg egy rövid szöveget: ")
    be_szam = int(input("Adj meg egy karakterszámot: "))
    if len(be_szoveg) < be_szam:
        print("Nincs "+str(be_szam)+" karakter!")
    else:
        print("A szöveg "+str(be_szam)+". karaktere", end=" ")
        eredmeny = be_szoveg[be_szam - 1]
        print(eredmeny + "-" + eredmeny.upper()*3)

def negyedik_feladat():
    i=0
    nev_beker = input("Adj meg egy nevet: ")
    while nev_beker != "@":
        i +=1
        nev_beker = input("Adj meg egy nevet: ")
    if nev_beker == "@":
        print("A felhasználó "+str(i)+" nevet adott meg.")

def otodik_feladat():
    beker = input("Kő, papír, vagy olló? ")
    while not (beker == "Kő" or beker == "KŐ" or beker == "kő" or beker == "papír" or beker == "Papír" or beker == "PAPÍR" or beker == "olló" or beker == "Olló" or beker == "Olló"):
        beker = input("Kő, papír, vagy olló? ")
    felhasznalo_tippje = beker.lower()


    i:int = 0
    while i < 1:
        gep_tip: int = math.floor(random.random()*2 +1)
        print(gep_tip, end=" ")
        i+=1
    gep_tippje = 0
    if gep_tip == 1:
        gep_tippje = "kő"
    elif gep_tip == 2:
        gep_tippje = "papír"
    else:
        gep_tippje = "olló"

    if gep_tippje == "kő" and felhasznalo_tippje == "olló":
        print("A gép nyert.")
    elif gep_tippje == felhasznalo_tippje:
        print("Döntetlen.")
    elif gep_tippje == "kő" and felhasznalo_tippje == "papír":
        print("A felhasználó nyert.")
    elif gep_tippje == "papír" and felhasznalo_tippje == "kő":
        print("A gép nyert.")
    elif gep_tippje == "papír" and felhasznalo_tippje == "olló":
        print("A felhasználó nyert.")
    elif gep_tippje == "olló" and felhasznalo_tippje == "kő":
        print("A felhasználó nyert.")
    else:
        print("A gép nyert.")