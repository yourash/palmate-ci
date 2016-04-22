from ..common.Node import NodeConfig

class NodeStorage:
    """ Stores list of nodes and their configuration.

    """

    def __init__(self, nodes):
        """ Initialises storage with nodes array

        """
        self.__currentNodeId = 1
        for node in nodes:
            self.addNode(node)

    def getNode(self, nodeId):
        return self.__nodes.get(nodeId)

    def addNode(self, node):
        """ Tries to register new node and adds it on successful registering

        """
        registeredNode = self.registerNode(node)
        if registeredNode == None:
            print "Faile dot register node: {}" % node
            return False
        else:
            self.__nodes.[self.__currentNodeId] = registeredNode
            self.__currentNodeId += 1
        return True

    def numNodes(self):
        return len(self.__nodes)

    def getNodeIds(self):
        return self.__nodes.keys()

    def registerNode(self, node):
        """ Checks if node is not registered yet, retrieves node configuration.

        """
        # TODO
        return NodeConfig(name="fakenode",host="fakehost", port=12345, maxJobs=0)

# Executor is responsible for populating node storage
nodeStorage = NodeStorage([])

class NodeList:
    def get(self):
        return {nodeStorage.getNodeIds()}

class Node:
    def get(self, nodeId):
        node = nodeStorage.getNode(nodeId)
        if node == None:
            return {"error": "Node with id %d does not exist" % int(nodeId)}, 404
        else:
            return node
