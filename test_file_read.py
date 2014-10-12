"""
Tests for file_read.py
"""

import file_read

def test_manage_line() :
    assert(file_read.manage_line('Matthew 34234 934') != None)
    assert(file_read.manage_line('Camille 2 435')==None)
    assert(file_read.manage_line('Person 34 0')=='Person 34 0')
    assert(file_read.manage_line('Person 0 0')==None)

test_manage_line()
