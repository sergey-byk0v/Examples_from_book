from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils

(X_train, y_train), (X_test, y_test) = mnist.load_data()
# prepare data
batch_size, img_rows, img_cols = 64, 28, 28
X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)
# model initialization
model = Sequential()
model.add(Convolution2D(32,5,5,border_mode = "same", input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2), strides = (2,2), border_mode = "same"))
model.add(Convolution2D(64,5,5,border_mode = "same", input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size = (2,2), strides = (2,2), border_mode = "same"))
# fully connected layers
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(10))
model.add(Activation('softmax'))
# compilation and start learning process
model.compile(loss='categorical_crossentropy',optimizer ='adam', metrics=['accuracy'])
model.fit(X_train, Y_train, batch_size=batch_size, epochs= 10, verbose = 1, validation_data = (X_test, Y_test))
score = model.evaluate(X_test, Y_test, verbose = 1)

print("Test  score: \n", score[0])
print("Test accuracy score: \n", score[1])

