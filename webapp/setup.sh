#!/bin/bash
rm -rf venv
virtualenv -p /usr/bin/python2 venv
source venv/bin/activate
pip2 install -r requirements.txt
