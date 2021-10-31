'''
write a python class for a particle, don't forget the init, by giving Z and A
This class should have a method which gives the number of neutrons back. 
Instantiate this class with an example.
'''

A=0
Z=0

class particle:
    def __init__(self, A, Z):
        self.A=A
        self.Z=Z
        #self.N=A-Z
    
    def neutron_number(self):
        return self.A-self.Z

#example elements
H=particle(1,1)
He=particle(4,2)
Li=particle(7,3)
Be=particle(9,4)
B=particle(11,5)
C=particle(12,6)
N=particle(14,7)
O=particle(16,8)

print(C.A)
print(N.neutron_number())


