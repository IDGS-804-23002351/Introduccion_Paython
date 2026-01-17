#clases
class OperasBas:
    #declaracion de variables
    num1 = 0
    num2 = 0
    res = 0
    #declaracion del constructos this
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
    #declaracion de metodos de clase}
    def sumar(self,a):
        self.num1 = a
        self.res = self.num1 + self.num2
        print("La suma es: {} "+ str(self.res))
    def restar(self):
        self.res = self.num1 - self.num2
        print("La resta es: {} "+ str(self.res))
def main():
    object =OperasBas()
    object.sumar(3)
if __name__ == "__main__":
    main()