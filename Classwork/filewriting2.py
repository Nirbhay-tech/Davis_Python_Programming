#program for writing data into the file
#opening file for write operation
filev=open("firstfile2.txt","w")
#blank list of sentences
sentences=[]
#writing five sentences into the file
print("Write any five sentences : ")
for x in range(5):
    #input data from the user
    sentence=input()
    #writing sentence into the list
    sentences.append(sentence)
    print("-------------------")
#-----------------------------------------
#writing data into the file
filev.writelines(sentences)
print("Data Successfully written")
#closing the file
filev.close()