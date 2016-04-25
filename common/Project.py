import yaml

class ProjectConfig:
    config = None
    def __init__(self, fpath):
        try:
            with open(fpath, 'r') as f:
                self.config = yaml.load(f.read())
        except IOError:
            print("Failed to open %s" % fpath)

