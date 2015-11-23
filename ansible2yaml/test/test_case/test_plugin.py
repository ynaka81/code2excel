import sys
sys.path.append("../../src")

import unittest
import subprocess
import yaml

## TestDirectoryResource
#
# The test case for directory resource
class TestDirectoryResource(unittest.TestCase):
    ## test for one directory
    # @param self The object pointer
    def testOneDir(self):
        cdata = {
            '/data': {
                'attirbutes': {
                    'path': '/data',
                    'owner': 'vagrant',
                    'group': 'vagrant',
                    'mode': '0755'
                },
                'values': {
                    'node1': True
                }
            }
        }
        cmd = "ansible-playbook -i hosts -t testOneDir directory.yml"
        self.assertEqual(subprocess.check_call(cmd.split(" "), cwd="../test_workspace"), 0)
        self.assertEqual(yaml.load(open("../test_workspace/output/directory.yml")), cdata)
    ## test for many directories
    # @param self The object pointer
    def testManyDir(self):
        cdata = {
            '/data': {
                'attirbutes': {
                    'path': '/data',
                    'owner': 'vagrant',
                    'group': 'vagrant',
                    'mode': '0755'
                },
                'values': {
                    'node1': True
                }
            },
            '/data/data1': {
                'attirbutes': {
                    'path': '/data/data1',
                    'owner': 'vagrant',
                    'group': 'vagrant',
                    'mode': '0700'
                },
                'values': {
                    'node1': True
                }
            },
            '/data/data2': {
                'attirbutes': {
                    'path': '/data/data2',
                    'owner': 'vagrant',
                    'group': 'vagrant',
                    'mode': '0750'
                },
                'values': {
                    'node1': True
                }
            },
            '/data/data3': {
                'attirbutes': {
                    'path': '/data/data3',
                    'owner': 'vagrant',
                    'group': 'vagrant',
                    'mode': '0750'
                },
                'values': {
                    'node1': True
                }
            }
        }
        cmd = "ansible-playbook -i hosts -t testManyDir directory.yml"
        self.assertEqual(subprocess.check_call(cmd.split(" "), cwd="../test_workspace"), 0)
        self.assertEqual(yaml.load(open("../test_workspace/output/directory.yml")), cdata)
    ## test for two hosts
    # @param self The object pointer
    def testTwoHosts(self):
        cdata = {
            '/data': {
                'attirbutes': {
                    'path': '/data',
                    'owner': 'vagrant',
                    'group': 'vagrant',
                    'mode': '0755'
                },
                'values': {
                    'node1': True,
                    'node2': True
                }
            },
            '/data/data1': {
                'attirbutes': {
                    'path': '/data/data1',
                    'owner': 'vagrant',
                    'group': 'vagrant',
                    'mode': '0700'
                },
                'values': {
                    'node1': True
                }
            },
            '/data/data2': {
                'attirbutes': {
                    'path': '/data/data2',
                    'owner': 'vagrant',
                    'group': 'vagrant',
                    'mode': '0750'
                },
                'values': {
                    'node2': True
                }
            }
        }
        cmd = "ansible-playbook -i hosts -t testTwoHosts directory.yml"
        self.assertEqual(subprocess.check_call(cmd.split(" "), cwd="../test_workspace"), 0)
        self.assertEqual(yaml.load(open("../test_workspace/output/directory.yml")), cdata)

if __name__ == "__main__":
    unittest.main()
