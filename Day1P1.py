def main():
   filepath ="Day1P1.txt"

   with open(filepath) as fp:
       total=0
       for line in fp:
           total += int(line)
       print(total)

if __name__ == '__main__':
   main()