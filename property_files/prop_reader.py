# -*- coding: utf-8 -*-

import codecs
import os


def property_reader(file_name) -> dict:
    directory = os.path.dirname(__file__)
    file = "%s/%s.txt" % (directory, file_name)
    return dict(line.strip().split('=') for line in codecs.open(file, 'r', 'utf-8') if '=' in line)
