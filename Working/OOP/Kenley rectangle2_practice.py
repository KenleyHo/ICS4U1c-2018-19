class Rectangle():

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return self.width * self.length

def main():
    rec1 = Rectangle(2, 4)
    print("The area of the rectangle is " + str(rec1.get_area()))
    rec2 = Rectangle(7, 19)
    print("The area of the rectangle is " + str(rec2.get_area()))
    rec3 = Rectangle(8, 17)
    print("The area of the rectangle is " + str(rec3.get_area()))

main()