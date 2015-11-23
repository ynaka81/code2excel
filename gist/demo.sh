#!/bin/bash

ansible-playbook -i hosts test_data/demo.yml
python yaml2excel.py
