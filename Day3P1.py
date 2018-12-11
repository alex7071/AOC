import numpy as np
import re

def read_strings():
    filepath = "Day3P1.txt"
    stringList = []
    with open(filepath) as fp:
        for line in fp:
            stringList.append(line.strip())
    return stringList

def main():
    textStringList = read_strings()

    fabric = np.zeros((1100, 1100), dtype=np.int16)

    for line in textStringList:
        instr = re.findall('\d+',line)
        value_to_fill = int(instr[0])
        row = int(instr[1])#inches_from_left_edge
        column = int(instr[2])#inches_from_top_edge
        inches_width = int(instr[3])
        inches_height = int(instr[4])

        fabric_to_fill = fabric[column:column+inches_height, row:row+inches_width]
        fabric_to_fill = (np.where((fabric_to_fill > 0) | (fabric_to_fill == -1), -1, value_to_fill))
        fabric[column:column + inches_height, row:row + inches_width] = fabric_to_fill

        # for w in range(0, inches_width):
        #     for h in range(0, inches_height):
        #         print(value_to_fill, inches_from_top_edge+w, inches_from_left_edge+h)
        #         arrayVal = fabric[inches_from_top_edge+w][inches_from_left_edge+h]
        #         if arrayVal > 0:
        #             fabric[inches_from_top_edge + w][inches_from_left_edge + h] = -1
        #         else:
        #             fabric[inches_from_top_edge+w][inches_from_left_edge+h] = inches_height
        #

    print((fabric == -1).sum())

if __name__ == '__main__':
   main()
