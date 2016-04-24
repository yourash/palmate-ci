from common.Leaf import LeafConfig
from flask_restful import Resource

class LeafStorage:
    """ Stores list of leaves and their configuration.

    """

    def __init__(self, leaves):
        """ Initialises storage with leaves array

        """
        self.__leaves = dict()
        self.__currentId = 1
        for leaf in leaves:
            self.addLeaf(leaf)

    def getLeaf(self, id):
        return self.__leaves.get(id)

    def addLeaf(self, leaf):
        """ Tries to register new leaf and adds it on successful registering

        """
        registeredLeaf = self.registerLeaf(leaf)
        if registeredLeaf == None:
            print("Faile dot register leaf: {}" % leaf)
            return False
        else:
            self.__leaves[self.__currentId] = registeredLeaf
            self.__currentId += 1
            print(self.__leaves[self.__currentId-1].serialize())
        return True

    def numLeaves(self):
        return len(self.__leaves)

    def getLeafIds(self):
        return list(self.__leaves.keys())

    def registerLeaf(self, leaf):
        """ Checks if leaf is not registered yet, retrieves leaf configuration.

        """
        # TODO
        return LeafConfig(name="fakeleaf",host="fakehost", port=12345, maxJobs=0)

# Executor is responsible for populating leaf storage
storage = LeafStorage([])

class LeafIndex(Resource):
    def get(self):
        return {"leaves":storage.getLeafIds()}

class LeafResource(Resource):
    def get(self, leafId):
        leaf = storage.getLeaf(leafId)
        if leaf == None:
            return {"error": "Leaf with id %d does not exist" % int(leafId)}, 404
        else:
            return leaf.serialize()
