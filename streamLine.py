from stream import Stream


class StreamLine:
    """ Implement readln and writeln by using the fgets and fputs functions from the C stdio library. These functions implements a buffering mechanism. """

    def __init__(self, filename):
        Stream.__init__(self, filename)

    def readln(self):
        """
        Read the next line from the stream
        """
        line = "test"
        return line

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        pass
