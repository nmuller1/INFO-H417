from streamCharacter import StreamCharacter
from streamBuffer import StreamBuffer
from streamLine import StreamLine
from streamMapping import StreamMapping

import os,queue
import mmap

class ExtSort():
    def __init__(self,k,M,d,inputFile,numberStreamR,numberStreamW,b):

        #M is the buffersize
        self.bufferSize = M
        # k is k th column in a line of the file
        self.column_k = k-1
        #d is the number of files merge simultaneously 
        self.numberInputStreams_d = d
        # numberStreamR and numberStreamW could have values in range [0,3] depending on the chosen method 

        self.numberStreamR = numberStreamR
        self.numberStreamW = numberStreamW
        # iputFile is the path of the input file
        self.inputFile = inputFile

        
    def streamMethod(self,fileRecordPath,numberStream,b):
        if numberStream == 0 :
            #reading or writing is done using  StreamCharachter
            return StreamCharacter(fileRecordPath)         
        if numberStream == 1 :
            #reading or writing is done using  StreamLine
            return StreamBuffer(fileRecordPath,b)
        if numberStream == 2 :
            #reading or writing is done using  StreamBuffer    
            return StreamLine(fileRecordPath)
        if numberStream == 3 :
            #reading or writing is done using StreamMap
            B = b* mmap.ALLOCATIONGRANULARITY
            return StreamMapping(fileRecordPath,B)
        

    def writing(self,counter,q,records,b):
        
            fileRecordPath="../recordsFiles/record"+str(counter)+".csv"
            #put the record file path is the queue
            q.put(fileRecordPath)
            #chosing the stream method to use 
            fileRecord = self.streamMethod(fileRecordPath,self.numberStreamW,b)
            #creating the file
            fileRecord.create()
            for record in records:
                #writing a record in the file 
                fileRecord.writeln(record )
            #close the file
            fileRecord.close()
            
    def merge(self,d,Opened_files,filesPath,priority_queue,records):
        c=d
        #read a line in each d files and store them in a priority_queue
        for i in range (d):
            line = Opened_files[i].readln()
            if line == "":
                c-=1
            else:
                #checking if the k_th column is a digit
                #storing in priority_queue as first parameter the k_th column
                #then the number of the file used to get the line
                #then the line
                if line.split(",")[self.column_k].isdigit():
                    priority_queue.put((int(line.split(",")[self.column_k]),i,line))
                else: priority_queue.put((line.split(",")[self.column_k],i,line))
        while c!= 0 and not priority_queue.empty() : 
            # get the line having smallest value on the k_th column using priority_queue
            temp = priority_queue.get()
            #storing in records the line
            records.append(temp[2])
            #reading a line from the same file as the previous one
            line = Opened_files[temp[1]].readln()
            if line == "":
                #decrease the number of c, if the file is read entirely
                c-=1
            else:
                #checking if the k_th column is a digit
                #storing in priority_queue as first parameter the k_th column
                #then the number of the file used to get the line
                #then the line
                if line.split(",")[self.column_k].isdigit():
                    priority_queue.put((int(line.split(",")[self.column_k]),i,line))
                else: priority_queue.put((line.split(",")[self.column_k],i,line))
        
        for i in range(d):
            #delete the files already used
            Opened_files[0].close()
            Opened_files.pop(0)
            filesPath.pop(0)
            #os.remove(filesPath)
        return records
        
    def extsort (self):
        #check if k and M and d are positive (self.column_k = k-1 )
        if self.column_k <0 or self.bufferSize<=0 or self.numberInputStreams_d  <=0 :
            return "Error : k,d and M must be positive numbers"
        else:
            #chosing the stream method to use 
            streamReadInput = self.streamMethod(self.inputFile,self.numberStreamR,self.bufferSize)
            #open the stream
            streamReadInput.open()
            #create a queue
            q = queue.Queue()
            counter=0
            if not os.path.exists('../recordsFiles'):
                os.makedirs('../recordsFiles')
            
            records=[]
            records_size=0
            eof = False
            
            while True:
                #checking if size of the records (lines) read < bufferSize 
                if records_size < self.bufferSize and eof== False : 
                    line = streamReadInput.readln()
                    if line =="":
                        #end of file = True if the file is read entirely
                        eof = True
                    else:
                        #add the line to records list
                        records.append(line)
                        #checking that k_th column exist in the file
                        if(len(line.split(",")) < self.column_k):
                            return "the {}-th column doesn't exist in the file".format(self.column_k)
                    #updating the the size of records
                    records_size+= len(line)
                else :
                    if records_size>0:
                        #checking if k_th column is a digit then sort the records on the k_th column
                        if records[0].split(",")[self.column_k].isdigit():
                            records = sorted(records,key=lambda x:int(x.split(",")[self.column_k]))
                        else: 
                            records =sorted(records,key=lambda x:x.split(",")[self.column_k])
                        #write the records in a file
                        self.writing(counter,q,records,self.bufferSize)
                        counter+=1
                        records.clear()
                        records_size=0
                    else: break
                
            
            priority_queue = queue.PriorityQueue(maxsize=self.numberInputStreams_d)
            Opened_files = []
            filesPath=[]
            for i in range(q.qsize()):
                #get the path of record files from the queue and opening the files
                fileRecordPath = q.get()
                temp = self.streamMethod(fileRecordPath,self.numberStreamR,self.bufferSize )
                temp.open()
                #store the stream in a list
                Opened_files.append(temp)
                #store the path of the stream in a list
                filesPath.append(fileRecordPath)
      
            while len(Opened_files) >1:
                d=self.numberInputStreams_d
                if len(Opened_files) <self.numberInputStreams_d and len(Opened_files)>1:
                    d=len(Opened_files)
                #merge the d files or less if the number of the remaining files < d
                records = self.merge(d,Opened_files,filesPath,priority_queue,records)
                #write the result of the merge in a file
                self.writing(counter,q,records,self.bufferSize)
                fileRecordPath = q.get()
                temp = self.streamMethod(fileRecordPath,self.numberStreamR,self.bufferSize )
                temp.open()
                Opened_files.append(temp)
                filesPath.append(fileRecordPath)
                counter+=1
                records.clear()
                
            if len(Opened_files) == 1:
                #print the file path of the final file that contains the sorted input file
                Opened_files[0].close()
                return filesPath[0]
            
            
            
        
    
            
        
            
                
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
            
            
            
            
            
            
            
            
            
            
            
        
            
         
         