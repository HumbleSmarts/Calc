count=0
print ("Enter a string: ")
humble= input()
for letter in humble:
    if (letter in ['A','E','I','O','U','a','e','i','o','u']):
         count=count+1
print("There are ", count, " vowels in the string.")