#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import sys
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import math

train_data_name = sys.argv[1]
l_pm25 = []

apped_dict = {
    "PM2.5": lambda x: l_pm25.extend(x[3:28])
}


a, b = symbols('a b')
#a, b = 1, 1
#f1 = lambda x: a * x + b
eta_a = 0.00001
eta_b = 0.00001
threshold = 1

def f1(X):
    return a * X + b

def linear_regression(X, Y):
    a, b = symbols('a b')
    st_a, st_b = 3,10
    error = 0.0

    for i in range(100):
        #print X[i], Y[i+1] , f1
        error += (Y[i+1] - f1(X[i])) ** 2
        #print error
        plt.plot(X[i], Y[i+1], 'ro')

        e_a = diff (error, a)
        e_b = diff (error, b)
        print "e_a=", e_a, "e_b=", e_b, "eta_a=", eta_a, "eta_b=", eta_b
        if i % 100 == 0:
            print "Processing data[", i, "]"

        counter = 0
        last_a = last_b = 0
        last_st_a = st_a
        last_st_b = st_b

    # http://terrence.logdown.com/posts/314392-simple-linear-regressionnumpy
    # 求聯立方程式的解
    res = solve([e_a, e_b], [a, b])
    print "ANS ======", res[a], res[b]

    while 1:
        counter += 1
        a_rate = e_a.subs({a: st_a, b: st_b})
        b_rate = e_b.subs({a: st_a, b: st_b})
        if last_a == 0:
            last_a = a_rate
            last_b = b_rate


        if counter % 1000 == 0:
            print "NewEtaTest a_rate=", a_rate, "b_rate=", b_rate, "last_a=", last_a, "last_b=", last_b, "eta_a=", eta_a, "eta_b=", eta_b , "st_a=", st_a, "st_b", st_b

        if abs(a_rate) >= abs(last_a) and abs(b_rate) >= abs(last_b):
            global eta_a, eta_b
            eta_a = eta_a / 10
            eta_b = eta_b / 10
            a_rate = last_a
            st_a = last_st_a
            b_rate = last_b
            st_b = last_st_b
        #else:
        #    if abs(a_rate) >= abs(last_a):
        #        global eta_a
        #        eta_a = eta_a / 10
        #        a_rate = last_a
        #        st_a = last_st_a

        #    if abs(b_rate) >= abs(last_b):
        #        global eta_b
        #        eta_b = eta_b / 10
        #        b_rate = last_b
        #        st_b = last_st_b

        last_st_a = st_a
        last_st_b = st_b

        if eta_a == 0 and eta_b == 0:
            break

        if counter % 1000 == 0:
            print "Fix a_rate=", a_rate, "b_rate=", b_rate, "st_a=", st_a, "st_b", st_b
        if abs(a_rate) < threshold and abs(b_rate) < threshold:
            break
        else:
            if abs(a_rate) >= threshold:
                st_a = st_a - eta_a * a_rate
            if abs(b_rate) >= threshold:
                st_b = st_b - eta_b * b_rate
        last_a = a_rate
        last_b = b_rate

    print "a_rate=", a_rate, "b_rate=", b_rate, "st_a=", st_a, "st_b", st_b
    LR_X = X
    #a = 3
    #b = 2
    #h = lambda x: a*x + b
    h = lambda x: st_a*x + st_b
    H = np.vectorize(h)
    LR_Y = H(LR_X)

    plt.plot(X, Y, 'b') # render blue line

    plt.plot(LR_X, LR_Y, 'g') # render green line

    #plt.plot(data_X, data_Y, 'ro')
    plt.show()


with open(train_data_name, 'r') as f:
        for line in f:
            word = line.replace('\r\n', '').split(',')
            try:
                apped_dict[word[2]](word)
                #print word[2]
                #print word
                #print line
                #print l_pm25
            except:
                continue
print l_pm25
l_pm25 = map(int, l_pm25)
linear_regression(l_pm25, l_pm25)

# if line.contains('PM2.5'):
