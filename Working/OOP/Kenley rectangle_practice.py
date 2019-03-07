class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

def get_area(rec):
    return(rec.width * rec.height)

def main():
    rec1 = Rectangle() #instance
    rec1.height = int(input())
    rec1.width = int(input())
    print(get_area(rec1))

main()

