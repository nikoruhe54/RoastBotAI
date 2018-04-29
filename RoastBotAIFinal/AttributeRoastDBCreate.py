import gcpDataStoreCalls

with open('ImageTrainer.txt', 'r') as AttributeList:
    image = ""
    att = ""
    score = ""
    lineCount = 1
    r1= ""
    r2 = ""
    r3 = ""
    r4 = ""
    r5 = ""
    for line in AttributeList:
        if (line.strip() != '@NEWFILE@'):
            if (lineCount == 1):
                image = line.strip()
                print(image)
                r1 = gcpDataStoreCalls.GetImageRoasts(image, "r1")
                print(r1)
                r2 = gcpDataStoreCalls.GetImageRoasts(image, "r2")
                print(r2)
                r3 = gcpDataStoreCalls.GetImageRoasts(image, "r3")
                print(r3)
                r4 = gcpDataStoreCalls.GetImageRoasts(image, "r4")
                print(r4)
                r5 = gcpDataStoreCalls.GetImageRoasts(image, "r5")
                print(r5)
                lineCount += 1
            elif (lineCount == 2):
                att = line.strip()
                lineCount += 1
            elif (lineCount == 3):
                score = line.strip()
                gcpDataStoreCalls.CompareEntryAndUpdate(att, float(score), r1, r2, r3, r4, r5)
                lineCount -= 1
        else:
            lineCount = 1