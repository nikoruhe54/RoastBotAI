import gcpDataStoreCalls

with open('roastDoc.txt', 'r') as roastDoc:
    image = ""
    roast1 = ""
    roast2 = ""
    roast3 = ""
    roast4 = ""
    roast5 = ""
    lineCount = 1
    for line in roastDoc:
        if (lineCount == 1):
            image = line.strip()
            lineCount += 1
        elif (lineCount == 2):
            roast1 = line.strip()
            lineCount += 1
        elif (lineCount == 3):
            roast2 = line.strip()
            lineCount += 1
        elif (lineCount == 4):
            roast3 = line.strip()
            lineCount += 1
        elif (lineCount == 5):
            roast4 = line.strip()
            lineCount += 1
        elif (lineCount == 6):
            roast5 = line.strip()
            gcpDataStoreCalls.BuildImageRoastDB(image, roast1, roast2, roast3, roast4, roast5)
            lineCount -= 5
