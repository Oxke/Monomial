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
#
#  If you want to contact me, -> oseaetobia@gmail.com

__author__ = "Oxke"
__contact__ = "oseaetobia@gmail.com"
__copyright__ = "Copyright (C) 2018, Oxke"
__license__ = "GNU GPLv3.0"  # Read the file LICENSE for more information
__project__ = "Monomial"
__version__ = "v0.1"
__date__ = "2018-12-24"

import argparse

from monomial_class import *

parser = argparse.ArgumentParser()
parser.add_argument("action", type=str)
args = parser.parse_args()


def init_repr():
    print(Monomial(input()))


def mul():
    a = Monomial.rand_monom(2)
    b = Monomial.rand_monom(3)
    e = Monomial.rand_monom()
    c = a.mul_two(b)
    f = c.mul_two(e)
    d = a * b * e
    assert f == d, "c and d should be equal"


def div():
    a = Monomial.rand_monom(2)
    b = Monomial.rand_monom(3)
    c = Monomial.rand_monom()
    d = a / b
    e = b / c
    f = c / a
    assert f * d == e.inverse(), "NO"


if __name__ == "__main__":
    if args.action == "init&repr":
        init_repr()
    elif args.action == "mul":
        mul()
    elif args.action == "div":
        div()
