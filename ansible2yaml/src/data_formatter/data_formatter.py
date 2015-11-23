## DataFormatter
#
# The data formatter of ansible data
class DataFormatter(object):
    ## constructor
    def __init__(self):
        ## formatted data
        self.__data = {}
    ## get data
    # @param self The object pointer
    # @return the formatted data
    def get(self):
        return self.__data
    ## add parsed data
    # @param self The object pointer
    # @param host The host name
    # @param data The parsed data
    def add(self, host, data):
        # when the resource type is new
        resource_type = data["resource"]
        if resource_type not in self.__data:
            resource_data = {}
            self.__data[resource_type] = resource_data
        else:
            resource_data = self.__data[resource_type]
        # when parsed data has new key, add to the formatted data
        key = data["key"]
        if key not in resource_data:
            resource_data[key] = {
                "attirbutes": {k: v for k, v in data.items() if k not in ("key", "resource")},
                "values": {}
            }
        # when parsed data has the key that already exists, add to values
        resource_data[key]["values"][host] = True
