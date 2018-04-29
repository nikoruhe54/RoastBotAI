import io
import os
from random import randint
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import gcpDataStoreCalls
# Instantiates a client
client = vision.ImageAnnotatorClient()

directory = os.fsencode("RoastThisImage")
attArray = []
conArray = []
fiArray = []
lotteryArray = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    if filename.endswith(".jpg") or filename.endswith(".png"):
        file_name = "RoastThisImage/" + filename

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations

        for label in labels:
            if (gcpDataStoreCalls.GetRoast(label.description, label.score, 'r1') != False):
                attArray.append(label.description)
                conArray.append(label.score)
                fiArray.append(gcpDataStoreCalls.GetFunnyIndex(label.description, label.score))
                print(label.description)
                print(label.score)

        for i in range(0, len(attArray)):
            lotteryArray.append(0.0)

        for x in range(0, len(lotteryArray)):
            if (x != 0):
                lotteryArray[x] = int((conArray[x]*10)*fiArray[x]) + lotteryArray[x-1]
            else:
                lotteryArray[x] = int((conArray[x]*10)*fiArray[x])

        print(lotteryArray)
        LotteryTicket = randint(0, lotteryArray[-1])
        print(LotteryTicket)
        for y in range(1, len(lotteryArray)):
            if (LotteryTicket < lotteryArray[y]):
                RoastIndex = y - 1
                break

        RoastNum = randint(1, 5)
        if (RoastNum == 1):
            roast = 'r1'
        elif (RoastNum == 2):
            roast = 'r2'
        elif (RoastNum == 3):
            roast = 'r3'
        elif (RoastNum == 4):
            roast = 'r4'
        else:
            roast = 'r5'

        RoastString = gcpDataStoreCalls.GetRoast(attArray[RoastIndex], conArray[RoastIndex], roast)
        print("\n")
        print("\n")
        print(attArray[RoastIndex])
        print(conArray[RoastIndex])
        print(roast)
        print(RoastString)
        img = Image.open(file_name)
        RList = list(RoastString)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("calibri",36)
        letters = 0
        for x in range(0, len(RList)):
            letters += 1
            if (letters > 25 and (RList[x] == ' ' or RList[x] == '\t')):
                RList[x] = '\n'
                letters = 0
        newStr = ''.join(RList)
        draw.multiline_text((0,0),newStr,(255,255,255),font=font,spacing=18,align="left")
        if(file_name.endswith(".jpg")):
            newFile = file_name+"NEW.jpg"
        if(file_name.endswith(".png")):
            newFile = file_name+"NEW.png"
        else:
            newFile = file_name+"NEW.jpg"
        img.save(newFile)
        imageDisplay = Image.open(newFile)
        imageDisplay.show()

        fi = input("What is the funny index? 0-10")
        while (fi != '0' and fi != '1' and fi != '2' and fi != '3' and fi != '4' and fi != '5' and
                       fi != '6' and fi != '7' and fi != '8' and fi != '9' and fi != '10'):
            print("invalid funny index")
            fi = input("What is the funny index? 0-10")
        gcpDataStoreCalls.UpdateFunnyIndex(attArray[RoastIndex], conArray[RoastIndex], int(fi))



