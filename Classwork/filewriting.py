#program for writing data into the file
#opening file for write operation
filev=open("firstfile.txt","w")
#writing five sentences into the file
print("Write any five sentences : ")
for x in range(5):
    #input data from the user
    sentence=input()
    #writing sentence into the file
    filev.write(sentence)
    print("-------------------")
#-----------------------------------------
print("Data Successfully written")
#closing the file
filev.close()