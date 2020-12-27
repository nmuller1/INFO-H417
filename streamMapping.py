import mmap
import os, sys  
from stream import Stream

class StreamMapping(Stream):
    """
    Implement readln and writeln by mapping and unmapping B characters of the file into internal memory through memory mapping.
    Whenever you need to read/write outside of the mapped portion, the next B element portion of the file is mapped.
    """

    def __init__(self, filename, mmapSize):
        Stream.__init__(self, filename)
        self.mmapSize = mmapSize * mmap.ALLOCATIONGRANULARITY
        self.count = 0
        
    def open(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, 'rb')
        self.size = os.stat(self.filename).st_size
        self.modulosize = self.size % self.mmapSize
        if self.size < self.mmapSize:
            self.mmapSize = self.size
        self.map = mmap.mmap(self.file.fileno(), length=self.mmapSize, offset=0, access=mmap.ACCESS_READ)

    def create(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, 'wb')
        self.map = mmap.mmap(-1, length=self.mmapSize, access=mmap.ACCESS_WRITE)
    
    def close(self):
        """
        Close the stream
        """
        self.file.close()

    def seek(self, pos):
        """
        Move the file cursor to pos so that a subsequent readln reads from position pos to the next end of line
        @param pos: position in the file where we want to move the cursor
        """
        self.file.seek(pos, 0)

    def readln(self):
        """
        Read the next line from the stream
        """
        char = " ".encode("utf-8")
        line = ""
        while not self.endOfFile() and char.decode("utf-8") != "\n":
            while not self.mapIsFull():
                char = self.map.read(1)
                if self.endOfFile():
                    self.eof = True
                    break
                if char.decode("utf-8") == "\n":
                    break
                line += str(char.decode("utf-8"))
            if not self.endOfFile() and self.mapIsFull():
                self.count += 1
                self.mapNextPortion()
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        i = 0
        while i < len(string):
            while not self.mapIsFull():
                self.map[i:i+1] = string[i].encode("utf-8")
                i += 1
                if i == len(string):
                    break
            self.file.write(self.map[0:i])
            self.cleanMap()
        self.file.write("\n".encode("utf-8"))

    def mapIsFull(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return self.map.tell() == self.mmapSize
    
    def endOfFile(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return self.map.tell() == self.size
    
    def cleanMap(self):
        """
        Empty the buffer
        """
        self.map.flush()
    
    def mapNextPortion(self):
        """
        Empty the buffer
        """
        if self.mmapSize * (self.count+1) >= self.size:
                offset = self.mmapSize * self.count
                self.mmapSize = self.modulosize
                self.map = mmap.mmap(self.file.fileno(), length=self.mmapSize, offset=offset, access=mmap.ACCESS_READ)
                self.eof = True
        else:
                self.map = mmap.mmap(self.file.fileno(), length=self.mmapSize, offset=self.map.tell(), access=mmap.ACCESS_READ)