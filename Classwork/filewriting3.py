#program to write 20 sentences in different lines
#opening file for written operation
f=open("firstfile3.txt","w") 
#blank list of sentences
sentences=[]
#writing 20 sentences into the file
print("Write any 20 sentences : ")
for x in range(20):
    #input data from the user
    sentence=input()
    #inserting the sentences into the list
    sentences.append(sentence+"\n")
    print("--------------------------")
#------------------------------------------------
#writing data into the file
f.writelines(sentences)
#closing the file
f.close()
