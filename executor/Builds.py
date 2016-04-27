from flask_restful import Resource, reqparse
import pymongo as mongo

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
    # TODO: implement BuildDAO with sqlite backend
    def __init__(self, mongoBuildsDb):
        self.__builds = dict()
        self.__currentId = 1
        self.__db = mongoBuildsDb

    def addBuild(self, build):
        if self.checkBuild(build):
            self.__builds[self.__currentId] = build

    def getBuildIds(self):
        return self.__builds.keys()

    def getBuild(self, buildId):
        return self.__builds.get(buildId)

    def checkBuild(self, build):
        return True

storage = None

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
    def get(self, buildId):
        build = storage.getBuild(buildId)
        if build is not None:
            return build.serialize()
        else:
            return {"error":"Build with id %d does not exist" %buildId}, 404

