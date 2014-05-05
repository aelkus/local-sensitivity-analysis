#!/usr/bin/env python

"""
Basic command-line tool for doing quick local sensitivity analysis.

Implements basic local sensitivity analysis equation:

    Splus = (Cplus - C)/(dP/P)

    Sminus = (C - Cminus)/(dP/P)

where Splus = upper sensitivity, Sminus = lower sensitivity, Cplus = model currency with upper value, Cminus = model currency with lower value,
C is reference currency value, P is default parameter, dP is range to vary parameter.

Take user command line arguments and returns parameter name, default parameter value, upper sensitivity, and lower sensitivity.

See Steven F. Railsback and Volker Grimm, Agent-Based and Individual-Based Modeling, Princeton: Princeton University Press, 2012, 293 for more.
"""

from __future__ import division #enforces mathematical division, not integer division
import sys
import argparse

class SensitivityEquation(object):
    """
    Class for calculating sensitivity values
    """
    def __init__(self, pn, p, dp, cref, cplus, cminus):

        #passed-in numbers
        self.pn = pn
        self.p = p
        self.dp = dp
        self.cref = cref
        self.cplus = cplus
        self.cminus = cminus

        #upper and lower sensitivity values

        self.splus = 0
        self.sminus = 0

    def calculate(self):
        """
        calculates following equations:
            Splus = (Cplus - C)/(dP/P)
            Sminus- = (C - Cminus)/(dP/P)
        """
        self.splus = (self.cplus - self.cref)/(self.dp/self.p)
        self.sminus = (self.cref - self.cminus)/(self.dp/self.p)

        return self.splus, self.sminus

if __name__ == '__main__':

    #parser object
    parser = argparse.ArgumentParser(description='Enter parameter name, parameter value, parameter variance, reference currency value, upper currency value, lower currency value, and name of output file.')

    #input arguments
    #if left on defaults, will return errors

    parser.add_argument('--Pn', '--parameter_name', type=str, default="insert string", help='name of parameter', metavar='pn', dest='pn')
    parser.add_argument('--P','--parameter_value', type=float, default=0.0, help='parameter value', metavar='p', dest='p')
    parser.add_argument('--Dp', '--parameter_variance', type=float, default=0.0, help='amount parameter is varied', metavar='dp', dest='dp')
    parser.add_argument('--Cr', '--currency_reference', type=float, default=0.0, help='reference value for model currency', metavar='cr', dest='cref')
    parser.add_argument('--Cp', '--currency_plus', type=float, default=0.0, help='currency value for upper region of parameter', metavar= 'cp', dest='cplus')
    parser.add_argument('--Cm', '--currency_minus', type=float, default=0.0, help='currency value for lower region of parameter', metavar='cm', dest='cminus')

    #argument parsing
    args = parser.parse_args()

    #intialize an equation
    eq = SensitivityEquation(args.pn, args.p, args.dp, args.cref, args.cplus, args.cminus)

    #calculate

    eq.calculate()

    #output
    print "Parameter name  = ",
    print eq.pn

    print "Parameter value = ",
    print eq.p

    print "Parameter variance = ",
    print eq.dp

    print "Upper Sensitivity = ",
    print eq.splus

    print "Lower Sensitivity = ",
    print eq.sminus
