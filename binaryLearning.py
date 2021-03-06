import tensorflow as tf
from tensorflow import keras

# first neural network with keras tutorial
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
# load the dataset
dataset = loadtxt('data_binary_1000.csv', delimiter=',')
# split into input (X) and output (y) variables
X = dataset[:,0:10]
y = dataset[:,10]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=10, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))
# compile the keras model
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse'])
# fit the keras model on the dataset
model.fit(X, y, epochs=1500, batch_size=10)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

#print(model.predict([7607]))