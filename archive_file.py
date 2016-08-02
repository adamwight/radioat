import datetime

# TODO:
# - song metadata and optionally allow stream ripper to cut
class ArchiveFile(object):
    '''
    Create a new file and open for writing, with a path based on the program
    title and today's date.
    '''

    # TODO:
    root = "/tmp"

    def __init__(self, program):
        self.program = program

        # TODO: other formats
        self.path = "{root}/{timestamp}-{title}.mp3".format(
            root=self.root,
            timestamp=datetime.date.today().isoformat(),
            title=program.title
        )
        print "Creating " + self.path

        # TODO: append
        self.output = open(self.path, "w")

    def __del__(self):
        if self.output:
            self.output.close()

    def write(self, chunk):
        self.output.write(chunk)
