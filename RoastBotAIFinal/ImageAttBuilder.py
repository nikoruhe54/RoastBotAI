import io
import os
import sys

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import json

# Instantiates a client
client = vision.ImageAnnotatorClient()

directory = os.fsencode("images")
with open('ImageTrainer.txt', 'w+') as outfile:
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        print(filename)
        if filename.endswith(".jpg") or filename.endswith(".png"):
            outfile.write("@NEWFILE@")
            outfile.write("\n")
            outfile.write(filename)
            outfile.write("\n")
            file_name = "images/" + filename
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            response = client.label_detection(image=image)
            labels = response.label_annotations

            data = {}
            for label in labels:
                print(label.description)
                outfile.write(label.description)
                outfile.write("\n")
                outfile.write(str(label.score))
                outfile.write("\n")
                print(label.score)
                #data[label.description] = label.score
            #json_data = json.dumps(data)
            #json.dump(data, outfile)
            #outfile.write("\n")
        else:
            print("no images left")