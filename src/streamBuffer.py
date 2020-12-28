from src.stream import Stream

class StreamBuffer(Stream):
    """
    Streams are equiped with a buffer of size B in internal memory.
    Whenever the buffer becomes empty/full the next B characters are read/written from/to the file.
    """

    def __init__(self, filename, bufferSize):
        Stream.__init__(self, filename)
        self.bufferSize = bufferSize
        self.buffer = ""

    def readln(self):
        """
        Read the next line from the stream
        @return: read line
        """
        endOfLine = False
        line = ""
        while not self.eof and not endOfLine:
            #fill the buffer
            if len(self.buffer == 0):
                self.buffer = self.file.read(self.bufferSize)
                if len(self.buffer) < self.bufferSize:
                    self.eof = True
            #read the buffer
            for i in range(len(self.buffer)):
                if self.buffer(0).decode("utf-8") == "\n":
                    self.buffer.pop(0)
                    endOfLine = True
                    break
                else:
                    line += str(self.buffer.pop(0).decode("utf-8"))
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        i = 0
        while i < len(string):
            while not self.bufferIsFull():
                self.buffer += string[i].encode("utf-8")
                i += 1
                if i == len(string):
                    break
            self.file.write(self.buffer)
            self.buffer = ""
        self.file.write("\n".encode("utf-8"))

    def bufferIsFull(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return len(self.buffer) == self.bufferSize
