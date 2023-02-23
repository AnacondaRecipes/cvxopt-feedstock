#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cvxopt
import cvxopt.base
import cvxopt.blas
import cvxopt.cholmod
import cvxopt.lapack
import cvxopt.misc_solvers
import cvxopt.umfpack
import cvxopt.glpk
import cvxopt.fftw

import sys
import pytest

if __name__ == '__main__':
    sys.exit(pytest.main())
