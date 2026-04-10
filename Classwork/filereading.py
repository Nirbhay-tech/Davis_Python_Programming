#to open file for reading operation
filev=open("firstfile3.txt","r")
#to check file is open or not
if(filev):
    #to read data from file
    data=filev.read()
    print(data)
    print("--------------------")
    print("NO. of characters : ",len(data))
    #closing the file
    filev.close()
else:
    print("Unable to open the file")