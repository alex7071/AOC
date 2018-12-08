def main():
    filepath = "Day1P2.txt"
    continueScan=True
    freqTotal=0
    fileFreqList = []
    freqList = set()

    with open(filepath) as fp:
        for line in fp:
            freq = int(line)
            fileFreqList.append(freq)

    while (continueScan):
        for freq in fileFreqList:
            freqTotal += freq
            if freqTotal in freqList:
                continueScan = False
                print(freqTotal)
                break
            else:
                freqList.add(freqTotal)
        print('continueScan')

if __name__ == '__main__':
    main()
