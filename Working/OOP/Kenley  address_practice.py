class Address(object):
    def __init__(self):
        self.addressline_1 = ""
        self.addressline_2 = ""
        self.postalcode = ""
        self.city = ""
        self.province = ""
        self.country = "Canada"

def print_address(addr):
    print(addr.address_line1)
    if addr.address_line2 != "":
        print(addr.address_line2)
    print(addr.city + ", " + addr.postal_code + ", " + addr.province)
    print(addr.country)

def main():
    home_address = Address()
    home_address.addressline_1 = "45 Henderson"
    home_address.addressline_2 = ""
    home_address.postalcode = "L3T2K6"
    home_address.city = "Markham"
    home_address.province = "Ontario"
    home_address.country = "Canada"
    print("Home Address")
    print_address(home_address)
    work_address = Address()
    print("Work Address")
    print_address(work_address)

main()
