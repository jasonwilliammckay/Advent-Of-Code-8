# Per http://adventofcode.com/day/8 parts one and two

def main():
    stringCodeCountP1 = 0
    stringValueCountP1 = 0    
    stringCodeCountP2 = 2   # quotes not accounted for with \n checks

    with open ('input.txt', 'r') as fileInput:
        while True:                             # handle...
            c = fileInput.read(1)
            if (c == '\n'):                     # end of line
                stringCodeCountP2 += 2         
            elif (c == '"'):                    # quote
                stringCodeCountP1 += 1
                stringCodeCountP2 += 2
            elif (c == '\\'):                   # escape character
                stringCodeCountP1 += 1
                stringCodeCountP2 += 2
                stringValueCountP1 += 1
                c = fileInput.read(1)
                if (c =='\\' or c=='"'):        # escaped backslash or quote
                    stringCodeCountP1 += 1
                    stringCodeCountP2 += 2
                elif (c=='x'):                  # escaped hex
                    stringCodeCountP1 += 3
                    stringCodeCountP2 += 3
                    c = fileInput.read(2)       # move to the end of the escaped hex
            if not c:
                break

    fileInput.close()

    output = stringCodeCountP1 - stringValueCountP1
    print "Part 1:\n\t(String Code - String Characters) = %s\n" % output

    output = stringCodeCountP2 - stringCodeCountP1
    print "Part 2:\n\t(New String Code - Part 1 String Code) = %s\n" % output
    
main()