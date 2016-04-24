
class LeafConfig:
    """Represent configuration for leaf.

    Intended to be used by both Executor and Leaf service
    """

    def __init__(self, name, host, port, maxJobs):
        self.name = name
        self.host = host
        self.port = port
        self.maxJobs = maxJobs

    def serialize(self):
        return {
            'name':self.name,
            'host':self.host,
            'port':self.port,
            'maxJobs':self.maxJobs
        }

