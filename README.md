# PatsakisKostas
Εργασία #3

def main():
    import requests, json
    url = "https://api.opap.gr/"
    gameid  = "1100"
    dstart = firstDayOfMonth()

    surl = url + "draws/v3.0/" + gameid + "/draw-date/" + dstart
    par = {"limit": "1"}

    resp = requests.get(surl, params=par)
    j = resp.text
    jdata = json.loads(j)
    rval = []

    for item in jdata['content']:
        t = int(item["drawId"]), list(item["winningNumbers"]["list"])
        rval.append(t)



def firstDayOfMonth():

	import datetime

	today = datetime.date.today()
	first = datetime.date(today.year, today.month, 1)
	return first

main()

Εργασία #6
def main():

    import tweepy as twt
    import string
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords

#Openning Tweeter
    consumerkey='ckey'
    consumersecret='cskey'
    accesstoken='atkey'
    accesstokensecret = 'atskey'

    auth = twt.OAuthHandler(consumerkey, consumersecret)
    auth.set_access_token(accesstoken, accesstokensecret)
    api = twt.API(auth, wait_on_rate_limit = True)

#Retrieve Users's last 10 tweets 
    usrName = input("Enter User Name = ")
    tweets = twt.Cursor(api.user_timeline, id=usrName).items(10)
    usrTweets = [tweet.text for tweet in tweets]
    txt = ' '.join(usrTweets)

#Words (all in lower case)
    tkns = word_tokenize(txt)
    tkns = [w.lower for w in tkns]

#Remove punctuations
    tbl = txt.maketrans('', '', string.punctuation)
    str = [w.translate(tbl) for w in tkns]

#Only true words
    words = [word for word in str if word.isalpha()]

#Remove stop words
    stp_w = set(stopwords.words('english')
    words = [w for w in words if not w in stop_words]

#Unique words
    unqWords = set(words)
    unqWordsList = list(unqWords)

#Printing 5 longest words
    unqWordsList.sort(reverse = True, key=myLen)
    print(unqWordsList [:4])

#Printing 5 shortest words
    unqWordsList.sort(key=myLen)
    print(unqWordsList [:4])

def myLen(a):
    return len(a)

main()

Εργασία #9

file_in = open("Texty.txt", 'r')                     #Read a file into a list
file_list = [line.rstrip() for line in file_in]
file_in.close
file_str = " ".join(file_list)                       #Join the list elements 
ltrs = list(file_ str)                               #All characters splited
oddLtrs = [x for x in ltrs if ord(x)%2==1)           #Keep all odd ASCII
totLtrs = len(oddLtrs)                               #Total number of odd ASCII 
snglLtrs = [[x, oddLtrs.count(x)] for x in set(oddLtrs)] #Single char and count
for i in range(snglLtrs)                             #Perc of each char
    stars = []                                       #A list for stars as 1%
    stars.append('*' * (snglLtrs[i][1] * 100 \\ totLtrs)) #Create the star bar
    print (snglLtrs[i][0], ''.join(stars))           #Printing char and bar


Εργασία #12

def main():
    file_in = open("Texty.txt", 'r')   #Read a file into a list
    file_list = [line.rstrip() for line in file_in]
    file_in.close
    newL = []                          #Create a new list for new lines 
    for l in file_list:                #Proses every line of the file
	words = l.split()              #Get words of the line into a list
        newWords = []                  #Create a new list for new words
        for w in words:                #Process each word
            newWord = mirrev(w)        #Get mirrored reversed word
            newWords.append(newWord)   #Add new word into new words list
	newL.append(newWords)          #Add all new words into new linwe list
    new_file = "\n".join(newL)         #Add all new lines into a new file list
    print(new_file)                    #Print the result


def mirrev(wrd):
    ltrs = list(wrd)                   #Get word letters into a list
    revLtrs = ltrs.reverse()           #Reverse the order of the list 
    mirRevLtrs = [char(255 - ord(x)) for x in revLtrs] #Get mirror ASCII 
    return "".join(mirRevLtrs)         #Retutn the new word

main()
