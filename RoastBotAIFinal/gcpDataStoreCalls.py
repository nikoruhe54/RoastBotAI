# Imports the Google Cloud client library
from google.cloud import datastore

# Instantiates a client
datastore_client = datastore.Client()

def BuildImageRoastDB(image, r1, r2, r3, r4, r5):
    entry = datastore.Entity(datastore_client.key('RoastedImages', image))
    entry.update({
        'r1': r1,
        'r2': r2,
        'r3': r3,
        'r4': r4,
        'r5': r5
    })
    datastore_client.put(entry)
    print("put image with roasts in db")

def UpdateFunnyIndex(attribute, confidence, fi):
    bracket = str(int(confidence*20)/20)
    with datastore_client.transaction():
        key = datastore_client.key(attribute, bracket)
        entry = datastore_client.get(key)
        funny = float(float(float(fi-5)/10) + float(entry['fi']))
        entry['fi'] = funny
        datastore_client.put(entry)
        print("updated funny index")

def GetRoast(attribute, confidence, roast):
    bracket = str(int(confidence*20)/20)
    with datastore_client.transaction():
        key = datastore_client.key(attribute, bracket)
        entry = datastore_client.get(key)
        if not entry:
            print ("no roast here")
            return False
        else:
            return (entry[roast])

def GetFunnyIndex(attribute, confidence):
    bracket = str(int(confidence*20)/20)
    with datastore_client.transaction():
        key = datastore_client.key(attribute, bracket)
        entry = datastore_client.get(key)
        if not entry:
            print ("no roast here")
            return False
        else:
            return (entry['fi'])

def GetImageRoasts(image, roast):
    key = datastore_client.key('RoastedImages', image)
    entry = datastore_client.get(key)
    if not entry:
        print("no image with roast")
    else:
        return(entry[roast])

def CompareEntryAndUpdate(attribute, confidence, r1, r2, r3, r4, r5):
    bracket = str(int(confidence*20)/20)
    with datastore_client.transaction():
        key = datastore_client.key(attribute, bracket)
        entry = datastore_client.get(key)
        if not entry:
            entry = datastore.Entity(key=key)
            entry['confidence'] = confidence
            entry['r1'] = r1
            entry['r2'] = r2
            entry['r3'] = r3
            entry['r4'] = r4
            entry['r5'] = r5
            entry['fi'] = 1
            datastore_client.put(entry)
            print("no entry, making new one")
        else:
            if (entry['confidence'] < confidence):
                entry = datastore.Entity(key=key)
                entry['confidence'] = confidence
                entry['r1'] = r1
                entry['r2'] = r2
                entry['r3'] = r3
                entry['r4'] = r4
                entry['r5'] = r5
                entry['fi'] = 1
                datastore_client.put(entry)
                print("entry had lower confidence, updating")
            else:
                print("entry had higher confidence, reject the update")