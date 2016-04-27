import os, sys
import common.Project as Project

__configBasePath = os.path.expanduser('~')

def getConfigDir():
    return __configBasePath+'/.palmate/'

__configExtension = '.yml'

def checkDirs():
    configPaths = [
                getConfigDir()+'projects/',
                getConfigDir()+'leaves/',
                getConfigDir()+'builds/'
            ]
    for path in configPaths:
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as e:
                print("Failed to create %s: %s" %(path, e.strerror))
                return False
    return True

def getProjects():
    projectPath = getConfigDir()+'/projects/'
    return [projectPath+f for f in os.listdir(projectPath)
            if os.path.isfile(os.path.join(projectPath, f)) and
            f.endswith(configExtension)]

def getLeaves():
    leafPath = getConfigDir()+'/leaves/'
    return [leafPath+f for f in os.listdir(leafPath)
            if os.path.isfile(os.path.join(leafPath, f)) and
            f.endswith(__configExtension)]

