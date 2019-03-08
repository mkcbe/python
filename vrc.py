a=input()
ascii=ord(a)
if (65<=ascii)and(ascii<=90):
    if(ascii==65)and(ascii==69)and(ascii==73)and(ascii==79)and(ascii==85):
        print("Vowel")
    else:
        print("Consonant")
elif(97<=ascii)and(ascii<=117):
    if(ascii==97)and(ascii==101)and(ascii==105)and(ascii==111)and(ascii==117):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
