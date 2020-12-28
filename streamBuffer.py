from stream import Stream


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
        char = " "
        line = ""
        while char != "\n":
            self.buffer = self.file.read(self.bufferSize)
            if len(self.buffer) < self.bufferSize: #end of file
                self.eof = True
                break
            line += self.buffer
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        i = 0
        while i < len(string):
            while not self.bufferIsFull():
                self.buffer += string[i]
                i += 1
                if i == len(string):
                    break
            self.file.write(self.buffer)
            self.buffer = ""
        self.file.write("\n")

    def bufferIsFull(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return len(self.buffer) == self.bufferSize
