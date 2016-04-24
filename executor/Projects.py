from flask_restful import Resource

class ProjectStorage:
    def __init__(self, projects):
        self.__projects = dict()
        self.__currentId = 1

        for p in projects:
            self.addProject(p)

    def addProject(self, project):
        if self.checkProject(project):
            self.__projects[self.__currentId] = project
            self.__currentId += 1

    def removeProject(self, projectId):
        p = self.__projects.get(projectId)
        if p is not None:
            del self._projects[projectId]

    def numProjects(self):
        return len(self.__projects)

    def getProjectIds(self):
        return self.__projects.keys()

storage = ProjectStorage([])

class ProjectIndex(Resource):
    def get(self):
        return {}

class ProjectResource(Resource):
    def get(self, projectId):
        return {}


