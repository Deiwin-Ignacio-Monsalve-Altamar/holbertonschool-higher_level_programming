#!/usr/bin/python3
"""[summary]"""
 
 
def matrix_mul(m_a, m_b):
    """[summary]
 
    Arguments:
        m_a {[type]} -- [description]
        m_b {[type]} -- [description]
 
    Raises:
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        TypeError: [description]
        ValueError: [description]
        ValueError: [description]
        TypeError: [description]
        TypeError: [description]
        ValueError: [description]
    """
    m_c = []
    m_temp = []
    if type(m_a) is not (list):
        raise TypeError("m_a must be a list")
 
    if type(m_b) is not (list):
        raise TypeError("m_b must be a list")
 
    for row in m_a:
        if type(row) is not (list):
            raise TypeError("m_a must be a list of lists")
        elif len(row) == 0:
            raise ValueError("m_a can't be empty")
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
 
    for row in m_b:
        if type(row) is not (list):
            raise TypeError("m_b must be a list of lists")
        elif len(row) == 0:
            raise ValueError("m_b can't be empty")
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
 
    if len(m_a) is 0 or m_a is None:
        raise ValueError("m_a can't be empty")
 
    if len(m_b) is 0 or m_b is None:
        raise ValueError("m_b can't be empty")
 
    if len(set([len(row) for row in m_a])) is not 1:
        raise TypeError("each row of m_a must be of the same size")
 
    if len(set([len(row) for row in m_b])) is not 1:
        raise TypeError("each row of m_b must be of the same size")
 
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
 
    for d in range(len(m_a)):
        m_temp = []
        for g in range(len(m_b[0])):
            m_temp.append(0)
        m_c.append(m_temp)
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return(m_c)