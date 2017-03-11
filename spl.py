#!/usr/bin/env python3
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

    spl is the Simple POS Linker runner..
"""

import sys
from simplepos import Linker
import logging


if __name__ == '__main__':

    logging.basicConfig (format = '%(asctime)s %(levelname)s %(name)s : %(message)s', level=logging.DEBUG)

    logger = logging.getLogger("link")
    logger.info ("Iniciando linker")
    link = Linker (*sys.argv)
    link.run()