#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from Constants.Constants import *

from Calculator import Calculator

"""
	Class of a Scientific Calculator
"""
class ScientificCalculator(Calculator):
	
	def sc_evalue(self,expresion):
		res = ""
		exponent = False
		for i in expresion:
			if i == '^':
				exponent = True
			if i is not [ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,ZERO,SUM,MOD,MULT,EXP,MINUS,DIV,DOT]:
				res = ERROR
		if exponent:
			flag = True
			spl = expresion.split("^",len(expresion))
			try:
				num = int(spl[0])
			except Exception:
				res = ERROR
				flag = False
			try:
				exp = int(spl[1])
			except Exception:
				res = ERROR
				flag = False
			if(flag):
				res = str(pow(num,exp))
		else:	
			res = self.evalue(expresion)
		return res

def main():
	c = ScientificCalculator()
	d1 = c.sc_evalue("1+2")
	d2 = c.sc_evalue(" 1 11 {+12")
	d3 = c.sc_evalue("1^1")
	d4 = c.sc_evalue("11^3")
	print d1
	print d2
	print d3
	print d4

if __name__ == '__main__':
	main()