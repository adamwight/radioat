class Daemon(object):
    main = None

    def run(self):
        self.main()

    def progress(self, job):
        pass

    def log(self, txt):
        print txt
