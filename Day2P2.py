from collections import Counter

def read_strings():
    filepath = "Day2P2.txt"
    stringList = []
    with open(filepath) as fp:
        for line in fp:
            stringList.append(line.strip())
    return stringList

def get_box_id(textStringList):
    for textItem in textStringList:
        for compareTextItem in textStringList:
            if textItem == compareTextItem:
                continue
            else:
                # calculate the difference between the two strings
                diff = sum(1 for a, b in zip(textItem, compareTextItem) if a != b)

                if diff == 1:
                    print(textItem)
                    print(compareTextItem)

                    diffCh = set(textItem).difference(set(compareTextItem))
                    if len(diffCh) != 0:
                        diffChStr = diffCh.pop()
                        print((diffChStr))
                        textItem=textItem.replace(diffChStr,'')
                        return textItem


def main():
    textStringList = read_strings()
    print(get_box_id(textStringList))

if __name__ == '__main__':
   main()