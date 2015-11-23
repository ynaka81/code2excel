import sys
sys.path.append("../../src")

import unittest

from module_parser import *

## TestFileParser
#
# The test case for FileParser
class TestFileParser(unittest.TestCase):
    ## init test case
    # @param self The object pointer
    def setUp(self):
        ## file parser
        self.__parser = FileParser()
    ## test FileParser.parse(data), data is directory
    # @param self The object pointer
    def testParseDirectory(self):
        data = {
            u'group': u'jenkins',
            u'uid': 997,
            u'changed': False,
            'invocation': {
                'module_name': u'file',
                'module_complex_args': {
                    'owner': 'jenkins',
                    'path': '/var/lib/jenkins/updates',
                    'state': 'directory',
                    'group': 'jenkins',
                    'mode': 493
                },
                'module_args': ''
            },
            u'state': u'directory',
            u'gid': 996,
            u'secontext': u'unconfined_u:object_r:var_lib_t:s0',
            u'mode': u'0755',
            u'owner': u'jenkins',
            u'path': u'/var/lib/jenkins/updates',
            u'size': 25
        }
        cdata = {
            'resource': 'directory',
            'key': '/var/lib/jenkins/updates',
            'path': '/var/lib/jenkins/updates',
            'owner': 'jenkins',
            'group': 'jenkins',
            'mode': '0755'
        }
        self.assertEqual(self.__parser.parse(data), cdata)
    ## test FileParser.parse(data), data is file
    # @param self The object pointer
    def testParseFile(self):
        data = {
            u'group': u'jenkins',
            u'uid': 997,
            u'changed': False,
            'invocation': {
                'module_name': u'file',
                'module_complex_args': {
                    'owner': 'jenkins',
                    'path': '/var/lib/jenkins/updates/default.json',
                    'group': 'jenkins',
                    'mode': 493
                },
                'module_args': ''
            },
            u'state': u'file',
            u'gid': 996,
            u'secontext': u'system_u:object_r:var_lib_t:s0',
            u'mode': u'0755',
            u'owner': u'jenkins',
            u'path': u'/var/lib/jenkins/updates/default.json',
            u'size': 969299
        }
        self.assertIsNone(self.__parser.parse(data))

    ## test FileParser.parse(data) fails because data is not directory or file
    # @param self The object pointer
    def testFailParse(self):
        data = {
            u'group': u'jenkins',
            u'uid': 997,
            u'changed': False,
            'invocation': {
                'module_name': u'file',
                'module_complex_args': {
                    'owner': 'jenkins',
                    'path': '/var/lib/jenkins/updates',
                    'state': 'directory',
                    'group': 'jenkins',
                    'mode': 493
                },
                'module_args': ''
            },
            u'state': u'fail',
            u'gid': 996,
            u'secontext': u'unconfined_u:object_r:var_lib_t:s0',
            u'mode': u'0755',
            u'owner': u'jenkins',
            u'path': u'/var/lib/jenkins/updates',
            u'size': 25
        }
        with self.assertRaises(NotImplementedError):
            self.__parser.parse(data)

if __name__ == "__main__":
    unittest.main()
