f=open("valaszok.txt","r")
a=len(f.readlines())
line1=f.read()
osszversenyzo=a-1





print("1. feladat: Az adatok beolvasása.")
print(f"2. feladat: A versenyen {osszversenyzo} versenyző indult.")
print(f"4. feladat: A helyes megoldás:{line1}")

f.close()
