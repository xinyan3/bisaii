import os
import random as rd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import unicodecsv as csv
import pylab as pl
from draw import prettyPicture

import csv
import re
s1=['嗯嗯','的的']
print(type(s1[0]))
print(s1)
data_tpye1=[[1.],[''], [1.],[""], [1.], [1.],[1.], [1.], [1.], [1.], [1.], [1.],[1.], [1.], [1.], [1.], [1.], [1.],[1.], [1.], [1.], [1.], [1.], [1.],[1.], [1.], [1.], [1.], [1.], [1.],[1.], [1.], [1.], [1.], [1.], [1.],[1.], [1.], [1.], [1.], [1.],[1.]]
data_tpye=type(data_tpye1)
data_tpye2=str(data_tpye)
my_matrix = np.loadtxt(open("../data/d_train_20180102.csv","rb"),dtype=data_tpye,delimiter=",",skiprows=0)


filename_queue = tf.train.string_input_producer(
    ["../data/d_train_20180102.csv",])
# 每次一行
print(my_matrix[0][41])
reader = tf.TextLineReader(skip_header_lines=1)
key, value = reader.read(queue=filename_queue)
key, value = reader.read(filename_queue)
# 解析每次的一行，默认以逗号分开
record_defaults =list(data_tpye1)
col1, col2, col3, col4, col5,ol6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18, col19, col20, col21, col22, col23, col24,col25, col26, col27, col28, col29, col30, col31, col32, col33, col34, col35, col36, col37, col38, col39, col40, col41,col42 = tf.decode_csv(value, record_defaults=record_defaults)
features = tf.stack([col1])

init_op = tf.global_variables_initializer()
local_init_op = tf.local_variables_initializer()

number_1=[]
age_1=[]
number_2=[]
tang_1=[]
for i in range(30):
    ii=rd.randint(1,5642)
    number_1 = number_1+[my_matrix[ii][0]]
    print(number_1)
    age_1=age_1+[my_matrix[ii][2]]
    number_2=number_2+[my_matrix[ii][8]]
    tang_1=tang_1+[my_matrix[ii][41]]



print(age_1)


# initial visualization

with tf.Session() as sess:
    writer = tf.summary.FileWriter("logs/", sess.graph)
    sess.run(init_op)
    sess.run(local_init_op)

    # Start populating the filename queue.
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    try:

        for i in range(30):
            example, label = sess.run([features,col42])
            print(example)
            print(label)
    except tf.errors.OutOfRangeError:
        print
        'Done !!!'

    finally:
        coord.request_stop()
        coord.join(threads)
