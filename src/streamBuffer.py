from stream import Stream
import time
import random

class StreamBuffer(Stream):
    """
    Streams are equiped with a buffer of size B in internal memory.
    Whenever the buffer becomes empty/full the next B characters are read/written from/to the file.
    """

    def __init__(self, filename, bufferSize):
        Stream.__init__(self, filename)
        self.bufferSize = bufferSize
        self.buffer = ""

    def open(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, "rb", buffering=self.bufferSize)

    def readln(self):
        """
        Read the next line from the stream
        @return: read line
        """
        line = self.file.readline().decode("latin-1")
        if line == "":
            self.eof = True
        return line.strip("\n")

    def create(self):
        """
        Create a new file
        """
        self.file = open(self.filename, "xb", buffering=self.bufferSize)

    def writeln(self, string):
        res = string + "\n"
        self.file.write(res.encode("latin-1"))

    def bufferIsFull(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return len(self.buffer) == self.bufferSize

    def length(self):
        """
        Sequential reading
        @return: sum of the length of each line
        """
        startTime = time.time()
        self.open()
        sum = 0
        while not self.end_of_stream():
            sum += len(self.readln())
        finalTime = time.time()
        timeTotal = finalTime - startTime
        print("StreamBuffer : time =", timeTotal)
        return sum, timeTotal

    def randomjump(self, j):
        startTime = time.time()
        self.open()
        sum = 0
        length = len(self.file.read())
        for i in range(j):
            p = random.randint(0, length)
            self.seek(p)
            line = self.readln()
            sum += len(line)
        finalTime = time.time()
        timeTotal = finalTime - startTime
        print("StreamBuffer : time =", timeTotal)
        return sum, timeTotal