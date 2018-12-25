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

import string
from random import randrange
from typing import Dict

__author__ = "Oxke"
__contact__ = "oseaetobia@gmail.com"
__copyright__ = "Copyright (C) 2018, Oxke"
__license__ = "GNU GPLv3.0"  # Read the file LICENSE for more information
__project__ = "Monomial"
__version__ = "v0.1.1"
__date__ = "2018-12-25"


class Monomial:
    powers: Dict[str, int]

    def __init__(self, monom, coefficient=None, powers=None):
        """
        Write monom (the monomial in string format) using the '^' character
        as power.
        For example: '3a^2b^5'
        :type monom: {str, Nonetype}
        """
        if coefficient is None and powers is None:
            monom = list(monom)
            self.powers = {}  # power for each letter in the monomial
            self.coefficient = 0  # coefficient of the monomial
            monom_let_index = []
            for char in monom:
                if char in string.ascii_letters:
                    assert char not in monom_let_index, 'Each letter should ' \
                                                        'appear only once'
                    monom_let_index.append(monom.index(char))
            if monom_let_index[0] > 0:
                self.coefficient = int(''.join(monom[0:monom_let_index[0]]))
            else:
                self.coefficient = 1
            for i in range(len(monom_let_index)):
                if monom_let_index[i] == monom_let_index[-1]:
                    if monom_let_index[i] + 1 != len(monom):
                        self.powers[monom[monom_let_index[i]]] = \
                            int(''.join(monom[monom_let_index[i] + 2:]))
                    else:
                        self.powers[monom[monom_let_index[i]]] = 1
                else:
                    self.powers[monom[monom_let_index[i]]] = \
                        int(''.join(monom[monom_let_index[i] +
                                          2:monom_let_index[i + 1]]))
        else:
            if coefficient is None:
                self.coefficient = 1
            else:
                self.coefficient = coefficient
            self.powers = powers

        self.powers = Monomial.powers0(self.powers) if self.coefficient != 0 \
            else {}

    @staticmethod
    def powers0(powers):
        def generator():
            for power in powers:
                if powers[power] != 0:
                    yield (power, powers[power])

        return dict(generator())

    def __repr__(self):
        result = 'coeff:\t' + str(self.coefficient) + '\n'
        result += 'powers:\t' + str(self.powers)
        return result

    def __str__(self):
        def sup(n: int):
            n_str = str(n)
            n_sup = ""
            for char in n_str:
                if char == "-":
                    n_sup += "\u207B"
                elif char == "1":
                    n_sup += "\u00B9"
                elif 2 <= int(char) <= 3:
                    n_sup += chr(176 + int(char))
                else:
                    n_sup += chr(8304 + int(char))
            return n_sup

        result = str(self.coefficient) if self.coefficient != 1 else ""
        for letter in self.powers:
            if self.powers[letter] != 1:
                result += f"{letter}{sup(self.powers[letter])}"
            else:
                result += letter
        return result

    def __int__(self):
        """return the coefficient as an integer"""
        return int(self.coefficient)

    def __float__(self):
        """return the coefficient as a floating number"""
        return float(self.coefficient)

    def __eq__(self, other):
        return str(self) == str(other)

    def __len__(self):
        return len(self.powers)

    @staticmethod
    def rand_monom(length=None):
        if isinstance(length, int):
            assert 0 < length < len(string.ascii_letters), "I don't know " \
                                                           "enough letters"
        else:
            length = randrange(5)
        coefficient = randrange(-10, 10)
        powers = {}
        for i in range(length):
            powers[string.ascii_letters[i]] = randrange(-10, 10)
        return Monomial(None, coefficient, powers)

    def __neg__(self):
        return Monomial(None, -self.coefficient, self.powers)

    def inverse(self):
        coefficient = 1 / self.coefficient
        powers = {power: -self.powers[power] for power in self.powers}
        return Monomial(None, coefficient, powers)

    def degree(self):
        return sum(self.powers.values())

    def mul_two(self, other):
        """Return product of two Monomials"""
        if isinstance(other, Monomial):
            coefficient = self.coefficient * other.coefficient
            powers = {power: self.powers[power] for power in self.powers}
            for letter in other.powers:
                if letter in powers:
                    powers[letter] += other.powers[letter]
                else:
                    powers[letter] = other.powers[letter]
        else:
            coefficient = self.coefficient * other
            powers = self.powers
        return Monomial(None, coefficient, powers)

    def __mul__(self, *args):
        result = self
        for arg in args:
            result = result.mul_two(arg)
        return result

    def __truediv__(self, other):
        return self * other.inverse()
