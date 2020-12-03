from stream import Stream


class StreamBuffer:
    """
    Streams are equiped with a buffer of size B in internal memory.
    Whenever the buffer becomes empty/full the next B characters are read/written from/to the file.
    """

    def __init__(self, filename):
        Stream.__init__(self, filename)

    def readln(self):
        """
        Read the next line from the stream
        """
        pass

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        pass
