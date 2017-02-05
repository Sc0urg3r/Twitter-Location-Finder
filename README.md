# Twitter-Location-Finder
Provides a CSV file that contains the spread of location data for a given key word and sample size.

# Install
In order to use this script you must first install Tweepy. More information can be found below: https://github.com/tweepy/tweepy

# Usage
Ensure that both TwitterBot.py and States.py are in the same directory. Then simply run the script and call main() with a key word and sample size as parameters. To export the data, call exportData() and specify a file name with the extension .csv

i.e main(myKeyWord, mySampleSize)

i.e exportData("myFileName.csv")
