#to open file for reading operation
filev=open("vowel.txt","r")
#list containing vowel
vowel="aeiouAEIOU"
count=0
#to check file is open or not
if(filev):
    #to read data from file
    data=filev.read()
    if(data):
      for char in data:
          if char in vowel:
              count+=1
      print("there are",count,"vowels")
      #closing the file
      filev.close()
    else:
        print("File is empty")
else:
    print("Unable to open the file")