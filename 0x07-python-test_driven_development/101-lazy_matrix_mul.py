#!/usr/bin/python3


"101-lazy_matrix_mul.py print number mult"


import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Arguments:
    M_a: matriz integer
    M_b: matriz integer
    """
    result_mul = numpy.dot(m_a, m_b)
    return result_mul
