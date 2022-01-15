#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

try:
    shutil.rmtree('dist')
except Exception as e:
    pass
os.system('pyinstaller -i icon.ico -n test --clean -y  --add-data "templates;templates" --add-data "cores.json;." --add-data "config.json;." --add-data "static;static" --add-data "openvgdb.sqlite;."  test.py')
shutil.make_archive(os.path.join("release","test"), 'zip', "dist/test")
shutil.rmtree('dist')
os.system('pyinstaller -i icon.ico -n MiSTerDash --clean -y -F --add-data "templates;templates" --add-data "static;static"  main.py')
shutil.copyfile('cores.json', 'dist/cores.json')
shutil.copyfile('config.json', 'dist/config.json')
shutil.copyfile('openvgdb.sqlite', 'dist/openvgdb.sqlite')
shutil.make_archive(os.path.join("release","MiSTerDash"), 'zip', "dist")
