# write the cnn code from the scratch using tensorflow and keras 

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, datasets, utils
import matplotlib.pyplot as plt

# Load and preprocess the dataset
(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0


# Define the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),  #in one epoch 60000 images are trained in 469 sets 
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


# Train the model
model.fit(X_train, y_train, epochs=10)

# Evaluate the model
model.evaluate(X_test, y_test)


# Save the model
model.save('mnist_cnn.h5')


# Load the saved model
model = models.load_model('mnist_cnn.h5')

# Make predictions
y_pred = model.predict(X_test)

# Plot the first 10 test images and their predicted labels
for i in range(10):
    plt.imshow(X_test[i], cmap='gray')
    plt.title(f'Predicted: {np.argmax(y_pred[i])}')
    plt.show()