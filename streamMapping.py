import mmap

class StreamMapping:
    """ Read and write is performed by mapping and unmapping B characters of the file into internal memory through memory mapping. Whenever you need to read/write outside of the mapped portion, the next B element portion of the file is mapped. """
    def __init__(self, filename, buffer):
        self.filename = filename
        self.eof = False
        pass

    def open(self):
        """
        Open an existing file for reading
        """
        self.file = open(self.filename, "r")
        pass

    def readln(self):
        """
        Read the next line from the stream
        """
        self.map = mmap.mmap(self.file.fileno(), 0)
        pass

    def seek(self, pos):
        """
        Move the file cursor to pos so that a subsequent readln reads from position pos to the next end of line
        @param pos: position in the file where we want to move the cursor
        """
        self.map.seek(pos)
        pass

    def end_of_stream(self):
        """
        Checks if the end of stream has been reached
        @return: True if the end of stream has been reached and False otherwise
        """
        return self.eof

    def create(self):
        """
         Create a new file
         """
        self.file = open(self.filename, "x")

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        for char in string:
            self.map.write(char)
        self.map.write("\n")

    def close(self):
        """
        Close the stream
        """
        self.file.close()