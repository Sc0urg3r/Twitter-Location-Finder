import tweepy, time, sys
from States import *

kconsumer_key = "NqM0x5BrkkYwOACBLLGenMkjf"
kconsumer_secret = 'oTTFX8UB3DFo4YAmISw96tvdPVb97MtMZEZzhgKU4BbWyWmqgl'
kaccess_key = '827725922572840961-L9oct69EU4FDQjNXkHDvCdqtcF9Kh7z'
kaccess_secret = 'ZSYZJwFVgu54vlJYIYzjZE6cdIruc2yZtGAOZmUBXwWo7'

auth = tweepy.OAuthHandler(kconsumer_key, kconsumer_secret)
auth.set_access_token(kaccess_key, kaccess_secret)
api = tweepy.API(auth)

readTweets = []

def updateLocationCount(location):
    location = location.split()
    for i in location:
        for (k,v) in states.items():
            if i == k or i == v:
                stateCount[k] += 1

def main(keyWord, sampleSize):
    query = keyWord
    maxTweets = sampleSize

    searchedTweets = [status for status in tweepy.Cursor(api.search, q=query).items(maxTweets)]
    
    for status in searchedTweets:        
        if status.id in readTweets:
            break
        try:
            readTweets.append(status.id)
            rawLocation = status.author.location
            cleanLocation = ""
            for char in rawLocation:
                if str.isspace(char) or str.isalpha(char):
                    cleanLocation += char
            if cleanLocation != "":
                updateLocationCount(cleanLocation)
        except:
            continue

def exportData(fileName):
    outputFile = open(fileName, "a")
    
    outputFile.write("State Name, State Code, Latitude, Longitude, Number of Tweets \n")
    for (key, value) in states.items():
        latitude = stateCoordinates[key][0]
        longitude = stateCoordinates[key][1]
        outputFile.write(value + ',' + key + ',' + str(latitude) + ',' +
                         str(longitude) + ',' + str(stateCount[key]) + "\n")

    


