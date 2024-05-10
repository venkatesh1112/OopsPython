from ClassandObject import Calculator
class mathFormulas(Calculator):
    num2 = 20
    def __init__(self):
        Calculator.__init__(self,2,3)
    def areaofTriangle(self):
        result = self.num2 + self.sum()

obj2=mathFormulas()
print(obj2)