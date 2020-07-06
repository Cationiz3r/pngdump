#!/bin/python3.8
import sys

def hex8(n):
    if (n == 0): return "00000000"
    else: return (8 - len(hex(n).split("x")[-1])) * "0" + hex(n).split("x")[-1]

input_file = sys.argv[1] + sys.argv[2]

reader = open(input_file, "r")
# print(reader.read());

hexes_str = reader.read()
hexes = hexes_str.split(" ")
reader.close()

# for i in range(10):
#     print(hexes[i], end = " ")
# print()

# print(len(hexes))

addresses = []

for i in range(len(hexes) - 4):
    if ((hexes[i] == "89") and hexes[i + 1] == "50" and
      (hexes[i + 2] == "4e" and hexes[i + 3] == "47")):
        # print(i)
        addresses.append(i)

# print(len(hexes))

addresses.append(len(hexes))
# print(addresses)

prefix = sys.argv[1] + ""
postfix = ".hex"
one_indexed = sys.argv[3] == "true";
for i in range(len(addresses) - 1):
    index = i
    if (one_indexed): index += 1
    writer = open(prefix + str(index) + postfix, "w")
    # writer.write(hexes_str[slice(addresses[i] * 3, addresses[i + 1] * 3)])
    # writer.close()

    print_address = 0

    for j in range(addresses[i + 1] - addresses[i]):
        if (j % 16 == 0):
            writer.write(hex8(print_address))
            writer.write(": ")
            print_address += 16
        writer.write(hexes[addresses[i] + j])
        if (j % 16 != 15 and j % 2 == 1): writer.write(" ")
        elif (j % 16 == 15): writer.write("\n")

    # break
