from flask_restful import Resource

class ProjectList(Resource):
    def get(self):
        return {'list of':'resources', 'in format':'TDB'}

class Project(Resource):
    def get(self, projectId):
        return {'project':projectId}
