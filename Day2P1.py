import numpy as np

def read_strings():
    filepath = "Day2P1.txt"
    stringList = []
    with open(filepath) as fp:
        for line in fp:
            stringList.append(line)
    return stringList

def frequency_count(text):
    #elem is an array of the unique elements in a string
    #and count is its corresponding frequency
    elem, count = np.unique(tuple(text), return_counts=True)
    print(count)
    return count

def main():
    textStringList = read_strings()
    twoFreq=0
    threeFreq=0
    for txt in textStringList:
        freqCountList = frequency_count(txt)
        if 2 in freqCountList:
            twoFreq += 1
        if 3 in freqCountList:
            threeFreq += 1
    checksum = twoFreq * threeFreq
    print(checksum)

if __name__ == '__main__':
   main()