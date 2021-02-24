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