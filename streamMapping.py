import mmap
from stream import Stream

class StreamMapping(Stream):
    """
    Implement readln and writeln by mapping and unmapping B characters of the file into internal memory through memory mapping.
    Whenever you need to read/write outside of the mapped portion, the next B element portion of the file is mapped.
    """

    def __init__(self, filename, mmapSize):
        Stream.__init__(self, filename)
        self.mmapSize = mmapSize
        self.open()
        self.map = mmap.mmap(self.file.fileno(), length=self.mmapSize, access=mmap.ACCESS_READ)
        

    def readln(self):
        """
        Read the next line from the stream
        """
        char = " ".encode("utf-8")
        line = ""
        while char and char.decode("utf-8") != "\n":
            while not self.mapIsFull():
                char = self.map.read(1)
                if not char:
                    self.eof = True
                    break
                if char.decode("utf-8") == "\n":
                    break
                line += str(char.decode("utf-8"))
            #self.mapNextPortion()
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
    
        i = 0
        self.map = mmap.mmap(self.file.fileno(), self.mmapSize, access=mmap.ACCESS_WRITE)
        while i < len(string):
            while not self.mapIsFull():
                self.map.write(i)
                i += 1
                if i == len(string):
                    break
            self.cleanMap()
            self.map = mmap.mmap(self.file.fileno(), self.mmapSize, access=mmap.ACCESS_WRITE)
        self.file.write("\n")

    def mapIsFull(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return self.map.tell() == self.mmapSize
    
    def cleanMap(self):
        """
        Empty the buffer
        """
        self.map.flush()
    
    def mapNextPortion(self):
        """
        Empty the buffer
        """
        self.map = mmap.mmap(self.file.fileno(), mmap.PAGESIZE, offset=self.map.tell()*mmap.PAGESIZE, access=mmap.ACCESS_READ)