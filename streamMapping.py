import mmap
from stream import Stream

class StreamMapping(Stream):
    """
    Implement readln and writeln by mapping and unmapping B characters of the file into internal memory through memory mapping.
    Whenever you need to read/write outside of the mapped portion, the next B element portion of the file is mapped.
    """

    def __init__(self, filename):
        Stream.__init__(self, filename)

    def readln(self):
        """
        Read the next line from the stream
        """
        self.map = mmap.mmap(self.file.fileno(), 0)

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        for char in string:
            self.map.write(char)
        self.map.write("\n")