#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Monomial, another python math class, this time for operating with monomials
#  Copyright (C) 2018 Oxke
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

__author__ = "Oxke"
__contact__ = "oseaetobia@gmail.com"
__copyright__ = "Copyright (C) 2018, Oxke"
__license__ = "GNU GPLv3.0"  # Read the file LICENSE for more information
__project__ = "Monomial"
__version__ = "v0.1"
__date__ = "2018-12-24"

from random import randrange

from monomial_class import *


def main():
    a = Monomial(f"{randrange(-5, 5)}x^{randrange(-5, 5)}y")
    b = Monomial(f"{randrange(-5, 5)}x^{randrange(-5, 5)}z^{randrange(-5, 5)}")
    c = a.mul_two(b)
    d = a * b
    assert c == d, "c and d should be equal"


if __name__ == "__main__":
    main()