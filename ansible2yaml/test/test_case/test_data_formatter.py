import sys
sys.path.append("../../src")

import unittest

from data_formatter import DataFormatter

## TestDataFormatter
#
# The test case for DataFormatter
class TestDataFormatter(unittest.TestCase):
    ## init test case
    # @param self The object pointer
    def setUp(self):
        ## data formatter
        self.__formatter = DataFormatter()
    ## test DataFormatter.add(host, data), data is one set
    # @param self The object pointer
    def testAddOne(self):
        parsed_data = {
            'resource': 'directory',
            'key': '/var/lib/jenkins/updates',
            'path': '/var/lib/jenkins/updates',
            'owner': 'jenkins',
            'group': 'jenkins',
            'mode': '0755'
        }
        cdata = {
            'directory': {
                '/var/lib/jenkins/updates': {
                    'attirbutes': {
                        'path': '/var/lib/jenkins/updates',
                        'owner': 'jenkins',
                        'group': 'jenkins',
                        'mode': '0755'
                    },
                    'values': {
                        'node1': True
                    }
                }
            }
        }
        self.__formatter.add("node1", parsed_data)
        self.assertEqual(self.__formatter.get(), cdata)
    ## test DataFormatter.add(host, data), data has two diretory
    # @param self The object pointer
    def testAddTwoData(self):
        parsed_data1 = {
            'resource': 'directory',
            'key': '/data1',
            'path': '/data1',
            'owner': 'sysadm',
            'group': 'wheel',
            'mode': '0755'
        }
        parsed_data2 = {
            'resource': 'directory',
            'key': '/data2',
            'path': '/data2',
            'owner': 'sysadm',
            'group': 'wheel',
            'mode': '0700'
        }
        cdata = {
            'directory': {
                '/data1': {
                    'attirbutes': {
                        'path': '/data1',
                        'owner': 'sysadm',
                        'group': 'wheel',
                        'mode': '0755'
                    },
                    'values': {
                        'node1': True
                    }
                },
                '/data2': {
                    'attirbutes': {
                        'path': '/data2',
                        'owner': 'sysadm',
                        'group': 'wheel',
                        'mode': '0700'
                    },
                    'values': {
                        'node1': True
                    }
                }
            }
        }
        self.__formatter.add("node1", parsed_data1)
        self.__formatter.add("node1", parsed_data2)
        self.assertEqual(self.__formatter.get(), cdata)
    ## test DataFormatter.add(host, data), data for two hosts
    # @param self The object pointer
    def testAddHosts(self):
        parsed_data = {
            'resource': 'directory',
            'key': '/var/lib/jenkins/updates',
            'path': '/var/lib/jenkins/updates',
            'owner': 'jenkins',
            'group': 'jenkins',
            'mode': '0755'
        }
        cdata = {
            'directory': {
                '/var/lib/jenkins/updates': {
                    'attirbutes': {
                        'path': '/var/lib/jenkins/updates',
                        'owner': 'jenkins',
                        'group': 'jenkins',
                        'mode': '0755'
                    },
                    'values': {
                        'node1': True,
                        'node2': True
                    }
                }
            }
        }
        self.__formatter.add("node1", parsed_data)
        self.__formatter.add("node2", parsed_data)
        self.assertEqual(self.__formatter.get(), cdata)

if __name__ == "__main__":
    unittest.main()
