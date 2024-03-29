import tensorflow as tf 
import numpy as np 

x_inp = tf.placeholder(tf.float32, [4,4])
x = tf.reshape(x_inp, [1,4,4,1])

x_valid = tf.nn.max_pool(x, ksize = [1,2,2,1], strides = [1,1,1,1], padding = 'VALID')
x_valid_half = tf.nn.max_pool(x, ksize = [1,2,2,1], strides = [1,2,2,1], padding = 'VALID')

X = np.array([[0,1,2,1],[4,1,0,1],[2,0,1,1],[1,2,3,1]])
sess = tf.Session()
y_valid, y_valid_half = sess.run([x_valid, x_valid_half], feed_dict = {x_inp: X})

print("x_valid: \n", y_valid[0,:,:,0])
print("x_valid_half: \n", y_valid_half[0,:,:,0])
