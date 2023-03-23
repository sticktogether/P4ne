import random
import ipaddress

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self):
        first = random.randint(1, 255)
        second = random.randint(0, 255)
        third = random.randint(0, 255)
        fourth = random.randint(0, 255)
        mask = random.randint(16, 32)

        string = ""
        string += str(first)
        string += "."
        string += str(second)
        string += "."
        string += str(third)
        string += "."
        string += str(fourth)
        string += "/"
        string += str(mask)

        super().__init__(string, False)
    def key_value(self):
        return int(str(self).split("/")[1])

array = []
for i in range(50):
    address = IPv4RandomNetwork()
    array.append(address)

# print(array)
array.sort(key=lambda x: x.key_value())

for i in range(len(array)) :
    print(array[i])

