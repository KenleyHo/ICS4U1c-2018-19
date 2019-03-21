class Rectangle():

    def __init__(self):
        self.width = 0
        self.length = 0

    def get_area(self):
        return self.width * self.length

def main():
    rec1 = Rectangle()
    rec1.width = 2
    rec1.length = 4
    print("The area of the rectangle is " + str(rec1.get_area()))
    rec2 = Rectangle()
    rec2.width = 7
    rec2.length = 19
    print("The area of the rectangle is " + str(rec2.get_area()))
    rec3 = Rectangle()
    rec3.width = 8
    rec3.length = 17
    print("The area of the rectangle is " + str(rec3.get_area()))

main()