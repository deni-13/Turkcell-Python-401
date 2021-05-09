class Veribilimci():
    bildgi_diller=["r","java"]  #genel
    bolum=[]
    def __init__(self): #self ornekleri temsil ediyor
        self.bildgi_diller=[] #örnek özellik tanımlama



ali=Veribilimci()
veli=Veribilimci() 

ali.bildgi_diller.append("python")
ali.bolum="elektronik müh"

veli.bildgi_diller.append("php")
veli.bolum="endustri muh"


print(ali.bildgi_diller)

print(veli.bildgi_diller)

print(ali.bolum)
print(veli.bolum)
