#!/usr/bin/python
# -*- coding: utf-8 -*- 

import os
import sys
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
import math

train_data_name = sys.argv[1]
test_data_name = sys.argv[2]
l_pm25 = []
t_l_pm25 = []

apped_dict = {
    "PM2.5": lambda x: l_pm25.extend(x[3:])
}
t_apped_dict = {
    "PM2.5": lambda x: t_l_pm25.extend(x[2:])
}


a0, a1, a2, b = symbols('a0 a1 a2 b')
#a, b = 1, 1
#f1 = lambda x: a * x + b
eta = 0.00001
st_a, st_b = 3,10
threshold = 1
res=dict()

def f1(X0, X1, X2):
    return a0 * X0 + a1 * X1 + a2 * X2 + b

def linear_regression(X, Y):
    global st_a, st_b, res
    global eta, eta
    a, b = symbols('a b')
    error = 0.0

    for i in range(100):
        #print X[i], Y[i+1] , f1
        error += (Y[i+3] - f1(X[i], X[i+1], X[i+2])) ** 2
        #print error
        plt.plot(X[i], Y[i+3], 'ro')

        e_a0 = diff (error, a0)
        e_a1 = diff (error, a1)
        e_a2 = diff (error, a2)
        e_b = diff (error, b)
        #print "e_a=", e_a, "e_b=", e_b, "eta=", eta
        if i % 100 == 0:
            print "Processing data[", i, "]"

        counter = 0
        last_a = last_b = 0
        last_st_a = st_a
        last_st_b = st_b

    # http://terrence.logdown.com/posts/314392-simple-linear-regressionnumpy
    # 求聯立方程式的解
    res = solve([e_a0, e_a1, e_a2, e_b], [a0, a1, a2, b])
    print "ANS ======", res[a0], res[a1], res[a2], res[b]
    print type(res)
    print type(res[a0])
    print float(res[a0])

#    while 1:
#        counter += 1
#        a_rate = e_a.subs({a: st_a, b: st_b})
#        b_rate = e_b.subs({a: st_a, b: st_b})
#        if last_a == 0:
#            last_a = a_rate
#            last_b = b_rate
#
#
#        if counter % 1000 == 0:
#            print "NewEtaTest a_rate=", a_rate, "b_rate=", b_rate, "last_a=", last_a, "last_b=", last_b, "eta=", eta, "st_a=", st_a, "st_b", st_b
#
#        if abs(a_rate) >= abs(last_a) and abs(b_rate) >= abs(last_b):
#            eta = eta / 10
#            a_rate = last_a
#            st_a = last_st_a
#            b_rate = last_b
#            st_b = last_st_b
#        #else:
#        #    if abs(a_rate) >= abs(last_a):
#        #        global eta
#        #        eta = eta / 10
#        #        a_rate = last_a
#        #        st_a = last_st_a
#
#        #    if abs(b_rate) >= abs(last_b):
#        #        global eta
#        #        eta = eta / 10
#        #        b_rate = last_b
#        #        st_b = last_st_b
#
#        last_st_a = st_a
#        last_st_b = st_b
#
#        if eta == 0:
#            break
#
#        if counter % 1000 == 0:
#            print "Fix a_rate=", a_rate, "b_rate=", b_rate, "st_a=", st_a, "st_b", st_b
#        if abs(a_rate) < threshold and abs(b_rate) < threshold:
#            break
#        else:
#            if abs(a_rate) >= threshold:
#                st_a = st_a - eta * a_rate
#            if abs(b_rate) >= threshold:
#                st_b = st_b - eta * b_rate
#        last_a = a_rate
#        last_b = b_rate
#
#    print "a_rate=", a_rate, "b_rate=", b_rate, "st_a=", st_a, "st_b", st_b
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

#print l_pm25
l_pm25 = map(int, l_pm25)
linear_regression(l_pm25, l_pm25)

with open(test_data_name, 'r') as f:
        for line in f:
            word = line.replace('\r\n', '').split(',')
            word = line.replace('\n', '').split(',')
            try:
                t_apped_dict[word[1]](word)
                #print word[2]
                #print word
                #print line
                #print t_l_pm25
            except:
                continue
        print '------------ideal equation---------------'
        t_l_pm25 = map(int, t_l_pm25)
        count = 0
        for i in range(1, 241):
            #print "target=", t_l_pm25[9*i-1]
            #print "id_", i - 1, t_l_pm25[9*i-1], int(t_l_pm25[9*i-1])*0.9518914347381807 + 2.248849145972113
            #print "id_", i - 1, ",", int(t_l_pm25[9*i-1])*0.9518914347381807 + 2.248849145972113
            tmp = "id_" + str(i-1) + "," + str(float(t_l_pm25[9*i-3]*res[a0]+ t_l_pm25[9*i-2]*res[a1]+ t_l_pm25[9*i-1]*res[a2] + res[b]))
            print tmp
        print '-----------------------------------------'
#        print '---------gradient decent equation--------'
#        count = 0
#        for i in range(1, 241):
#            #print "id_", i - 1, t_l_pm25[9*i-1], int(t_l_pm25[9*i-1])*0.9518914347381807 + 2.248849145972113
#            #print "id_", i - 1, ",", int(t_l_pm25[9*i-1])*st_a + st_b
#            tmp = "id_" + str(i) + "," + str(t_l_pm25[9*i-1]*st_a + st_b)
#            print tmp
#        print '-----------------------------------------'

#print t_l_pm25

# if line.contains('PM2.5'):
