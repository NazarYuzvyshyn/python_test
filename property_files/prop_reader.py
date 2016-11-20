# -*- coding: utf-8 -*-

import os
import codecs


def property_reader(file_name) -> dict:
    directory = os.path.dirname(__file__)
    file = os.path.join(directory, file_name + '.txt')

    return dict(line.strip().split('=') for line in codecs.open(file, 'r', 'utf-8') if '=' in line)
