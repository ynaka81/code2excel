import os
import shutil
import yaml

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from module_parser import *
from data_formatter import DataFormatter

## CallbackModule
#
# ansible callback class
class CallbackModule(object):
    ## constructor
    def __init__(self):
        ## yaml output directory
        self.__output_dir = os.path.join(os.getcwd(), "output")
        # initialize output directory
        if os.path.exists(self.__output_dir):
            shutil.rmtree(self.__output_dir)
        os.makedirs(self.__output_dir)
        ## module parser
        self.__parser = {}
        self.__parser["file"] = FileParser()
        ## data formatter
        self.__formatter = DataFormatter()
    ## output design informations
    # @param The object pointer
    # @param host The host name
    # @param data The ansible callback data
    def __output(self, host, data):
        # convert data to design info
        data_type = data["invocation"]["module_name"]
        if data_type in self.__parser:
            parsed_data = self.__parser[data_type].parse(data)
            self.__formatter.add(host, parsed_data)
    ## ansible callback function when the result is ok
    # @param self The object pointer
    # @param host The host name
    # @param res The ansible responce
    def runner_on_ok(self, host, res):
        self.__output(host, res)
    ## ansible callback function at the end
    # @param self The object pointer
    # @param stats The ansible statistics
    def playbook_on_stats(self, stats):
        data = self.__formatter.get()
        for k, v in data.items():
            file_name = os.path.join(self.__output_dir, k + ".yml")
            with open(file_name, "w") as f:
                f.write(yaml.safe_dump(v))
    # default methods
    def on_any(self, *args, **kwargs):
        pass
    def runner_on_failed(self, host, res, ignore_errors=False):
        pass
    def runner_on_skipped(self, host, item=None):
        pass
    def runner_on_unreachable(self, host, res):
        pass
    def runner_on_no_hosts(self):
        pass
    def runner_on_async_poll(self, host, res, jid, clock):
        pass
    def runner_on_async_ok(self, host, res, jid):
        pass
    def runner_on_async_failed(self, host, res, jid):
        pass
    def playbook_on_start(self):
        pass
    def playbook_on_notify(self, host, handler):
        pass
    def playbook_on_no_hosts_matched(self):
        pass
    def playbook_on_no_hosts_remaining(self):
        pass
    def playbook_on_task_start(self, name, is_conditional):
        pass
    def playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
        pass
    def playbook_on_setup(self):
        pass
    def playbook_on_import_for_host(self, host, imported_file):
        pass
    def playbook_on_not_import_for_host(self, host, missing_file):
        pass
    def playbook_on_play_start(self, name):
        pass
