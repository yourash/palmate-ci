
class NodeConfig:
    """Represent configuration for node.

    Intended to be used by both Executor and Node service
    """

    def __init__(self, name, host, port, maxJobs):
        self.name = name
        self.host = host
        self.port = port
        self.maxJobs = maxJobs

