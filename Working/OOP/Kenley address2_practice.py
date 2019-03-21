class Address():

    def __init__(self):
        self.addressline_1 = ""
        self.addressline_2 = ""
        self.city = ""
        self.province = ""
        self.postalcode = ""
        self.country = "Canada"

    def print_address():
        print(self.addressline_1)
        if self.addressline_2 != "":
            print(self.addressline_2)
        print(self.city + "" + self.province + "" + self.postalcode + "" + self.coutry)

def main():
    my_address = Address()
    my_address.addressline_1 = "45 Henderson"
    my_address.addressline_2 = ""
    my_address.city = "Markham"
    my_address.province = "Ontario"
    my_address.postalcode = "L3T2K6"
    my_address.country = "Canada"
    print("My address is: " + my_address.print_address())

main()


