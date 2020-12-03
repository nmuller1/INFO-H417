from stream import Stream


class StreamBuffer(Stream):
    """
    Streams are equiped with a buffer of size B in internal memory.
    Whenever the buffer becomes empty/full the next B characters are read/written from/to the file.
    """

    def __init__(self, filename, bufferSize):
        Stream.__init__(self, filename)
        self.bufferSize = bufferSize
        self.buffer = []

    def readln(self):
        """
        Read the next line from the stream
        @return: read line
        """
        char = " "
        line = ""
        while char and char != "\n":
            while not self.bufferIsFull():
                char = self.file.read(1)
                if not char:
                    self.eof = True
                    break
                if char == "\n":
                    break
                self.buffer.append(char)
            for i in self.buffer:
                line += i
            self.cleanBuffer()
        for i in self.buffer:
            line += i
        self.cleanBuffer()
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        i = 0
        while i < len(string):
            while not self.bufferIsFull():
                self.buffer.append(string[i])
                i += 1
                if i == len(string):
                    break
            for j in self.buffer:
                self.file.write(j)
            self.cleanBuffer()
        self.file.write("\n")

    def bufferIsFull(self):
        """
        Checks if the buffer is full
        @return: True if the buffer is full and False if not
        """
        return len(self.buffer) == self.bufferSize

    def bufferIsEmpty(self):
        """
        Checks if the buffer is empty
        @return: True is the buffer is empty and False if not
        """
        return len(self.buffer) == 0

    def cleanBuffer(self):
        """
        Empty the buffer
        """
        self.buffer = []
