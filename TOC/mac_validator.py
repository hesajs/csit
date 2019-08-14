# Write a program that validates the 48 bit MAC address


class Mac_Val:
    def __init__(self, mac_addr):
        self.mac_addr = mac_addr.lower()

    def is_mac_valid(self):
        if(len(self.mac_addr) > 12 or len(self.mac_addr) < 12):
            return False
        for x in range(len(self.mac_addr)):
            if not (self.mac_addr[x].isnumeric() or
                    (ord(self.mac_addr[x]) >= 97 and ord(self.mac_addr[x]) <= 102)):
                print(f'here {x}')
                return False
        return True


def main():
    mac = input("Enter the MAC Address: ")
    mac_check = Mac_Val(mac)
    if(mac_check.is_mac_valid()):
        print(f"'{mac}' is valid MAC address")
    else:
        print(f"'{mac}' is Invalid MAC address")


if __name__ == '__main__':
    main()
