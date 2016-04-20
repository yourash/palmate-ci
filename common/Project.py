import hjson

class Project:
    config = None
    def __init__(self, fpath):
        try:
            with open(fpath, 'r') as f:
                self.config = hjson.loads(f.read())
        except IOError:
            print("Failed to open %s" % fpath)

