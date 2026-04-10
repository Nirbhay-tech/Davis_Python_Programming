#to open file for read operation
filev=open("firstfile.txt","r")
#to check file is open or not
if(filev):
    #to read data from file
    data=filev.readline()
    if(data):
        print("Content of a file : ")
        while(data):
            print(data)
            data=filev.readline()
    else:
        print("File is empty")
#closing the file
filev.close()
