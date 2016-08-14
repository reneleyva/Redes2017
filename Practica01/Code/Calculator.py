#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from Constants.Constants import *

class Calculator:
	"""
		Class of a Basic Calculator
	"""
	def evalue(self,expresion):
		res = ""
		try:
			res = str(eval(expresion))
		except Exception:
			res = ERROR

		return res

