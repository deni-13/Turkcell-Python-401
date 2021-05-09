#örnek metodlari

class Veribilimci():  #bunun altındakiler default
    calısanlar=[]
    bolum =[]
#özel
    def __init__(self): #self ornekleri temsil ediyor
        self.bildgi_diller=[] #örnek özellik tanımlam

    def dilekle(self,yenidil):
        yenidil=self.bildgi_diller.append(yenidil)


ali=Veribilimci()
print(ali.bolum)



veli=Veribilimci()
print(veli.bolum)


#dilekle cagırcaz

a=ali.dilekle("c++")
print(ali.bildgi_diller)
