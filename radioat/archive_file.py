import datetime
import os

import radioat.ui


# TODO:
# - song metadata and optionally allow stream ripper to cut
class ArchiveFile(object):
    '''
    Create a new file and open for writing, with a path based on the program
    title and today's date.

    TODO: avoid overwriting accidental simultaneous or same-day stuff, get a
    new filename.
    '''

    # TODO:
    root = os.getenv("HOME") + "/radio"

    def __init__(self, program):
        self.program = program

        # TODO: other formats
        self.path = "{root}/{timestamp}-{title}.mp3".format(
            root=self.root,
            timestamp=datetime.date.today().isoformat(),
            title=program.title
        )
        radioat.ui.get().log("Creating " + self.path)

        # TODO: append
        self.sink = open(self.path, "w")

    def __del__(self):
        if self.sink:
            self.sink.close()
