import numpy as np

import matplotlib.pyplot as plt

from tensorflow.keras.datasets import cifar10

from tensorflow.keras.applications.vgg16 import VGG16

from tensorflow.keras.applications.vgg16 import preprocess_input

from tensorflow.keras.preprocessing import image




(x_train, y_train), (x_test, y_test) = cifar10.load_data()

model = VGG16(weights='imagenet', include_top=False)

class_labels = [

   'airplane', 'automobile', 'bird', 'cat', 'deer',

   'dog', 'frog', 'horse', 'ship', 'truck'

]

patterns = [

   x_train[1], 

   x_train[3], 

]

for pattern in patterns:

   img = image.array_to_img(pattern)

   img = img.resize((224, 224))

   x = image.img_to_array(img)

   x = np.expand_dims(x, axis)
