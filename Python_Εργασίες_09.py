#Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII
#κειμένου και μετατρέπει τον κάθε χαρακτήρα του στον αντίστοιχο αριθμό ASCII
#και κρατάει τους μονούς. Εμφανίστε τα στατιστικά εμφάνισης του κάθε γράμματος
#με μπάρες χρησιμοποιοώντας το χαρακτήρα *, όπου κάθε * αντιστοιχεί σε 1%



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
