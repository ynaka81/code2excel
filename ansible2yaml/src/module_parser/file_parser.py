from module_parser import ModuleParser

## FileParser
#
# The parser class of file module
class FileParser(ModuleParser):
    ## constructor
    def __init__(self):
        pass
    ## parse file module data
    # @param self The object pointer
    # @param data The ansible callback data
    # @return parsed line data
    def parse(self, data):
        state = data["state"]
        # when resrouce is directory
        if state == "directory":
            # parse data
            resource = "directory"
            path = data["path"]
            owner = data["owner"]
            group = data["group"]
            mode = data["mode"]
            key = path
            # make parsed data
            return {"resource": resource, "key": key, "path": path, "owner": owner, "group": group, "mode": mode}
        # when resource is file, no output is made
        elif state == "file":
            return None
        # others raise error
        else:
            raise NotImplementedError, "resource types expect for directory or file in file module is not implemented."
