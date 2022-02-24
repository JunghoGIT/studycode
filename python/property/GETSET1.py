class jungho:

    def __init__(self,weight):
        self.__weight = weight
        self.weight2 = weight+10
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,weight):
        self.__weight= weight