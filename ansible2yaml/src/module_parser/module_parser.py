from abc import ABCMeta, abstractmethod

## ModuleParser
#
# The interface class to parse module data
class ModuleParser(object):
    __metaclass__ = ABCMeta
    ## abstract method of parsing module data
    # @param self The object pointer
    # @param data The ansible callback data
    # @return parsed line data (type,key1,key2,...,value)
    @abstractmethod
    def parse(self, data):
        pass
