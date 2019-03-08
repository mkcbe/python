a=input()
ascii=ord(a)
if (65<=ascii)and(ascii<=90):
    if(a=='A')or(a=='E')or(a=='I')or(a=='O')or(a=='U'):
        print("Vowel")
    else:
        print("Consonant")
elif(97<=ascii)and(ascii<=122):
    if(a=='a')or(a=='e')or(a=='i')or(a=='o')or(a=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
