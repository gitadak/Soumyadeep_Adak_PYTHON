import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

#load CIFAR-10 data
(x_train, y_train), (x_test,y_test) = cifar10.load_data()

#normalize pixel values
x_train, x_test = x_train/255.0, x_test/255.0

#one-hot encode labels
y_train = to_categorical(y_train,10)
y_test = to_categorical(y_test,10)

#define class names
class_names = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

'''
#visualize sample images
plt.figure(figsize=(10,10))
for i in range(25):
  plt.subplot(5,5,i+1)
  plt.xticks([])
  plt.yticks([])
  plt.grid(False)
  plt.imshow(x_train[i])

plt.show()
'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

#Define the CNN model
model = Sequential([
    Conv2D(32,(3,3), activation='relu', input_shape=(32,32,3)),
    MaxPooling2D((2,2)),
    Conv2D(64,(3,3),activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(64,activation='relu'),
    Dense(10,activation='softmax')
])

#Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

#Train the model
history = model.fit(x_train, y_train, epochs=1, validation_data=(x_test, y_test))

#Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}')


import numpy as np

#load and preprocess a single image
img_path = x_test[6] #Using the first image from the test set
print('image is loaded')
img = img_path
img_array = np.expand_dims(img, axis=0)

#Display the image
plt.figure(figsize=(1,1))
plt.imshow(img)
plt.axis('off')
plt.show()

#Predict the class
predictions = model.predict(img_array)
print('predicted is',predictions)
predicted_class = np.argmax(predictions)
probability = np.max(predictions)

#Display the result
print(f'The image is a {class_names[predicted_class]} with a probability of {probability:.2f}')