#3. feladat
import math
a1=int(input("Adja meg az 'a' pont első koordinátáját: "))
a2=int(input("Adja meg az 'a' pont második koordinátáját: "))
b1=int(input("Adja meg a 'b' pont első koordinátáját: "))
b2=int(input("Adja meg a 'b' pont második koordinátáját: "))

tav=math.sqrt(((b1-a1)**2)+((b2-a2)**2))
tav=round(tav,2)
tav=str(tav)
print("A két pont távolsága: "+tav)


#3. feladat máshogy
import math
a=(input("Adja meg az 'a' pont koordinátáit, vesszővel elválasztva: "))
b=(input("Adja meg a 'b' pont koordinátáit, vesszővel elválasztva: "))

list=a.split(",")
a1=int(list[0])
a2=int(list[1])

list=b.split(",")
b1=int(list[0])
b2=int(list[1])

tav=round((math.sqrt(((b1-a1)**2)+((b2-a2)**2))),2)
print(f"A két pont távolsága: {tav}")


#4. feladat
def osszegszamolo(x):
    lista=list(x)
    sum=0
    for i in lista:
        i=int(i)
        sum=sum+i
    print(f"A szám számjegyeinke összege: {sum}")

x=input("Adjon meg egy viszonylag nagyobb számot: ")
osszegszamolo(x)


#5. feladat
def rendezo(szoveg):
    lista=szoveg.split((","))
    lista.sort()
    jolista=[]
    for i in lista:
        if i not in jolista:
            jolista.append(i)
    print(jolista)

szoveg=input("Adj meg szavakat, vesszővel elválasztva: ")
rendezo(szoveg)


#6. feladat
szo=input("Adj meg egy szót: ")
szam=int(input("Adj meg egy számot: "))
def levago(szo,szam):
    if len(szo)<3:
        return szo
    else:
        return szo[0:(szam)]

print(levago(szo,szam))