# -*- coding: utf-8 -*-
"""
    Copyright © 2017 - Alexandre Machado <axmachado@gmail.com>

    This file is part of Simple POS Compiler.

    Simnple POS Compiler is free software: you can redistribute it
    and/or modify it under the terms of the GNU General Public License
    as published by the Free Software Foundation, either version 3
    of the License, or (at your option) any later version.

    Simple POS Compiler is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Simple POS Compiler. If not, see <http://www.gnu.org/licenses/>.


    @author: Alexandre Machado <axmachado@gmail.com>
"""

import unittest
from simplepos.api import findApiFunction


class ApiFinderTest(unittest.TestCase):

    def setUp(self):
        pass

    def testFindSomeFunctions(self):
        for fname in ['waitkey', 'displaybitmap', 'crc', 'time_operation',
                      'crc_ccitt', 'xor', 'cipher_block', 'dbread',
                      'downloadfile', "iso8583_get_int", "receive",
                      "hexdecode"]:
            f1 = findApiFunction(fname)
            self.assertIsNotNone(f1)
