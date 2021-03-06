import inspect
import os
import importlib

def getModule(path):
    return [module.replace(".py", "")
            for module in filter(lambda x : x.find("__init__") == -1 and x.endswith(".py"),
                                 [path.strip("./").replace("/", ".") + "." + module for module in os.listdir(path)])]

def getFunctions(module):
    if isinstance(module, basestring):
        module = importlib.import_module(module)
    return inspect.getmembers(module, inspect.isfunction)
    
def getArgs(function):
    return inspect.getargspec(function)
    
if __name__ == "__main__":
    import os
    print getFunctions(os)
