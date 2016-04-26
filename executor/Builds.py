from flask_restful import Resource, reqparse

class BuildDTO:
    def __init__(self, timestamp, projectId, leafId, artifactId):
        self.timestamp = timestamp
        self.projectId = projectId
        self.leafId = leafId
        self.artifactId = artifactId

    def serialize(self):
        return {
            "timestamp":self.timestamp,
            "leafId":self.leafId,
            "artifactId":self.artifactId
        }

class BuildDAO:
    def __init__(self):
        self.__builds = dict()
        self.__currentId = 1

    def addBuild(self, build):
        if self.checkBuild(build):
            self.__builds[self.__currentId] = build

    def getBuildIds(self):
        return self.__builds.keys()

    def getBuild(self, buildId):
        pass

    def checkBuild(self, build):
        return True

storage = BuildDAO()

class BuildIndex(Resource):
    def __init__(self):
        self.__parser = reqparse.RequestParser()
        self.__parser.add_argument('projectId',required=True, type=int)

    def get(self):
        args = self.__parser.parse_args()
        print(args)
        ids = [b for b in storage.getBuildIds() and
               storage.getBuild(b).projectId == args['projectId']]
        print(ids)
        return {"builds":ids}

class BuildRecentIndex(Resource):
    pass

class BuildResource(Resource):
    pass
