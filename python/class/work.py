class employee:
    hourlywage = 8600
    def __init__(self,name,time):
        self.name=name
        self.time=time
        #self.hourlywage=hourlywage

    def wage(self):
        wage=self.time * self.hourlywage
        print(f"{self.name}님의 이번 달 근무 시간은 {self.time}시간이며, 예상 급여는 {wage}원 입니다.")

    @classmethod
    def set_hourlywage(cls,N):
        cls.hourlywage=N

    @staticmethod
    def clac(self,x,y):
        return x*y