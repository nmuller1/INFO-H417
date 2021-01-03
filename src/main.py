import mmap

from streamCharacter import StreamCharacter
from streamBuffer import StreamBuffer
from streamLine import StreamLine
from streamMapping import StreamMapping
from modifiableCycle import ModifiableCycle
from extSort import ExtSort
import os
import time
import random
    
def rrmerge(numberStreamR,numberStreamW,filenameW,*files):
    # numberStreamR and numberStreamW could have values in range [0,3] depending on the chosen method 
    templist = []
    if numberStreamR == 0 :
        #reading is done using StreamCharachter
        #adding all files in list temp
         for f in files:
             temp = StreamCharacter(f)
             temp.open()
             templist.append(temp)
             
    

    if numberStreamR == 1 :
        #reading is done using  StreamLine
        #adding all files in list temp
         for f in files:
             temp = StreamLine(f)
             temp.open()
             templist.append(temp)
    if numberStreamR == 2 :
        #reading is done using StreamBuffer
        #adding all files in list temp
         for f in files:
             temp = StreamBuffer(f,4)
             temp.open()
             templist.append(temp)

             
    if numberStreamR == 3 :
        #reading is done using  StreamMapping
        B = 1 * mmap.ALLOCATIONGRANULARITY
        #adding all files in list temp
        for f in files:
             temp = StreamMapping(f,B)
             temp.open()
             templist.append(temp)
    #ModifiableCycle allows a round robin iteration  
    listfiles = ModifiableCycle(templist)

    if numberStreamW == 0 :  
        #writing is done using StreamCharachter
        output_stream = StreamCharacter(filenameW)
        
        

        
    if numberStreamW == 1 :
        #writing is done using StreamLine
        output_stream = StreamLine(filenameW)
    if numberStreamW == 2 :
        #writing is done using StreamBuffer
        output_stream = StreamBuffer(filenameW,1)
        
             
    if numberStreamW == 3 :
        #writing is done using StreamMapping
        B = 1 * mmap.ALLOCATIONGRANULARITY
        output_stream = StreamMapping(filenameW,B)

    #creting output file
    output_stream.create()
    
    for f in listfiles:  
        #read one line of each file in a round robin
        line = f.readln()
        
        if line == "":
            #deleting the file from the list, if the file is read entirely
            listfiles.delete_prev()
            #close the file
            f.close()
        else:
            #write the line if the output file
            output_stream.writeln(line)
    #close the output file
    output_stream.close()





def testReadStream(stream):
    """
    Test the read method of a stream
    @param stream:
    @return:
    """
    stream.open()
    stream.seek(0)
    while not stream.end_of_stream():
        print(stream.readln())
    stream.close()

def testWriteStream(writeStream):
    text = ["Ceci est", "un test", "pour le cours", "d'INFO-H417"]
    writeStream.create()
    for line in text:
        writeStream.writeln(line)
    writeStream.close()

    
if __name__ == "__main__":
    files = ["imdb/comp_cast_type.csv", "imdb/movie_link.csv", "imdb/aka_title.csv", "imdb/name.csv",
           "imdb/cast_info.csv"]
    B = 1 * mmap.ALLOCATIONGRANULARITY
    readFilename = "../testFiles/link_type.csv"
    readStreams = [StreamCharacter(readFilename), StreamLine(readFilename),
                   StreamBuffer(readFilename, B), StreamMapping(readFilename, B)]

    for i in range(4):
        print(readStreams[i].length())

    def length1(f):
        sum = 0
        for i in range(10):
            readStream = StreamCharacter(f)
            sum += readStream.length()[1]
        sum /= 10
        return sum

    def length2(f):
        sum = 0
        for i in range(10):
            readStream = StreamLine(f)
            sum += readStream.length()[1]
        sum /= 10
        return sum

    def length3(f,B):
        sum = 0
        for i in range(10):
            readStream = StreamBuffer(f,B)
            sum += readStream.length()[1]
        sum /= 10
        return sum

    def length4(f,B):
        sum = 0
        for i in range(10):
            readStream = StreamMapping(f, B)
            sum += readStream.length()[1]
        sum /= 10
        return sum

    def random1(f):
        sum = 0
        for i in range(10):
            readStream = StreamCharacter(f)
            sum += readStream.randomjump(200)[1]
        sum /= 10
        return sum

    def random2(f):
        sum = 0
        for i in range(10):
            readStream = StreamLine(f)
            sum += readStream.randomjump(200)[1]
        sum /= 10
        return sum

    def random3(f,B):
        sum = 0
        for i in range(10):
            readStream = StreamBuffer(f,B)
            sum += readStream.randomjump(200)[1]
        sum /= 10
        return sum

    def random3(f,B):
        sum = 0
        for i in range(10):
            readStream = StreamBuffer(f, B)
            sum += readStream.randomjump(10)[1]
        sum /= 10
        return sum

    def random4(f,B,j):
        sum = 0
        for i in range(10):
            readStream = StreamMapping(f, B)
            sum += readStream.randomjump(j)[1]
        sum /= 10
        return sum

    text = ["Ceci est", "un test", "pour le cours", "d'INFO-H417"]
    

    rrmerge(1,1,"../testFiles/test3.txt","../testFiles/foo.txt","../testFiles/be.txt")


    
    

    B = 1 * mmap.ALLOCATIONGRANULARITY
    for file in files:
        print("total en moyenne pour le fichier", file, " avec B =", B, ":", random4(file, B,100))

    B = 2 * mmap.ALLOCATIONGRANULARITY
    for file in files:
        print("total en moyenne pour le fichier", file, " avec B =", B, ":", random4(file, B,100))

    B = 3 * mmap.ALLOCATIONGRANULARITY
    for file in files:
        print("total en moyenne pour le fichier", file, " avec B =", B, ":", random4(file, B,100))

    B = 4 * mmap.ALLOCATIONGRANULARITY
    for file in files:
        print("total en moyenne pour le fichier", file, " avec B =", B, ":", random4(file, B,100))

    k = 1

    M = 50
    d = 3
    numberStreamR = 2
    numberStreamW = 2
    b = 3
    inputFile = "../testFiles/link_type.csv"
    temp = ExtSort(k, M, d, inputFile, numberStreamR, numberStreamW, b)

    print(temp.extsort())

