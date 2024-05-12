#!/usr/bin/env python3

from ipdb_debugging import plus_two

class TestIpdbDebugging:
    '''Test cases for ipdb_debugging.py'''

    def test_adds_two(self):
        '''Test that plus_two() adds 2 to input argument.'''
        assert plus_two(3) == 5
