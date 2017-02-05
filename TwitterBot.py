import tweepy, time, sys
from States import *

kconsumer_key = '' #your consumer key here
kconsumer_secret = '' #your consumer secret here
kaccess_key = '' #your access key here
kaccess_secret = '' #your access secret here

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

    


