class Clothes:
    V = int()
    H = int()
    def __init__(self, clothes, v, h):
        self.clothes = clothes
        V = v
        N = h


    @property
    def clothes(self):
        return self.__clothes__


    @clothes.setter
    def clothes(self, clothes):
        if clothes == 'coat':
            self.__clothes__ = Clothes.V/6.5 + 0.5
        elif clothes == 'suit':
            self.__clothes__ = Clothes.H * 2 + 0.3


    def clothes_c(self):
        return self.clothes

c = Clothes(clothes=input(), v=int(input()), h=int(input()))
print(c.clothes_c())