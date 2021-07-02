class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Afficher(self):
        print("L'abscisse est :{}".format(self.x))
        print("L'ordonnee est :{}".format(self.y))


class cercle(Point):

    def __init__(self, x, y, R):
        self.x = x
        self.y = y
        self.R = R

    def getPerimetre(self):
        p = 2*3.14*self.R
        print("Le perimetre du cercle est:" +str(p))


    def getSurface(self):
        s = 3.14 * self.R * self.R
        print("la surface du cercle est"+str(s))
    def afficher(self):
        print("CERCLE DE CENTRE O DE COORDONEES{}".format(self.x)+"{}".format(self.y))
        print("ET DE RAYON R={}".format(self.R))
class cylindre(cercle):
    def __init__(self,R,h):
        self.R=R
        self.h=h

    def getVolume(self):
        volume=3.14*self.R*self.R*self.h
        print("le volume du cylindre est:"+str(volume))






# PROGRAMME PRINCIPAL
print("___________________")
print("la classe POINT")
print("___________________")

h1 = Point(2, 5)
h1.Afficher()
print("___________________")
print("La classe cercle")
print("___________________")

h2 =cercle(2,4,3)
h2.afficher()
h2.getPerimetre()
h2.getSurface()

print("___________________")
print("La classe cylindre")
print("___________________")
h3=cylindre(3,5)
h3.getVolume()





