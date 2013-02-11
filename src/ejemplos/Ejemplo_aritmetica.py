'''
Created on 10/02/2013

@author: infest48
'''
# Arithmetic expressions - numbers, operators, expressions


# numbers - imprimir floats e intergers

print 3, -1, 3.14159, -2.8


# convertir interger a float y viceversa

print int(3.1), int(3.7), int(-3.1), int(-3.7)

print float(3), float(-7)



# el tama–o de float que solo alcanza 15 digitos.
print 3.1415926535897932384626433832795028841971

print 1.4142135623730950488016887242096980785696



# operators
# +        plus        addition
# -        minus        subtraction
# *        times        multiplication
# /        divided by     division
# **    power        exponentiation

print 1 + 2, 3 - 4, 5 * 6, 2 ** 5


# note that division computes floating point approximation to exact answer

print 1 / 3, 5 / 2, -7 / 3


# consistent with Javascript and Python 3, but not Python 2.6
# integer division in CodeSkulptor is //

print 1 // 3, 5 // 2, -7 // 3



# expressions - number or a binary operator applied to two expressions
# minus is also a unary operator and can be applied to a single expression

print 1 + 2 ** 3, 4 - 5 / 6, 7 * 8 + 9 * 10


# expressions are entered as sequence of numbers and operations
# how are the number and operators grouped to form expressions?
# operator precedence - "please excuse my dear aunt sallie" = (), **, *, /, +,-

print 1 * 2 + 3 * 4
print 2 + 12



# always manually group using parentheses when in doubt

print 1 * (2 + 3) * 4
print 1 * 5 * 4