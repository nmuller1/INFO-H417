from src.stream import Stream


class StreamLine(Stream):
    """
    Implement readln and writeln by using the fgets and fputs functions from the C stdio library.
    These functions implements a buffering mechanism.
    """

    def __init__(self, filename):
        Stream.__init__(self, filename)

    def readln(self):
        """
        Read the next line from the stream
        """
        return self.readln().decode("utf-8")

    def writeln(self, string):
        """
        Write a string to the stream and terminate this stream with the newline character
        @param string: to write in the stream
        """
        res = string + "\n"
        self.writeln(res.encode("utf-8"))
