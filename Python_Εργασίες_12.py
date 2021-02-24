#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII
#κειμένου και μετατρέπει τον κάθε χαρακτήρα του στον “κατοπτρικό” του χαρακτήρα
#ASCII. Κατοπτρικοί χαρακτήρες είναι αυτοί των οποίων το άθροισμα είναι 255. 
#Εμφανίστε το κατοπτρικό κείμενο στο χρήστη με ανάποδη σειρά χαρακτήρων.


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