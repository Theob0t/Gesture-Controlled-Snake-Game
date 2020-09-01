import tensorflow.keras
import numpy as np
from PIL import Image, ImageOps

def pred(model):

    
    labels = {0: 'up',
    1: 'down',
    2: 'left',
    3: 'right',
    4: 'neutral'
         }

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    # Replace this with the path to your image
    image = Image.open('frame.jpg')
    
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    
    #turn the image into a numpy array
    image_array = np.asarray(image)
    
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    
    # Load the image into the array
    data[0] = normalized_image_array
    
    # run the inference
    prediction = model.predict(data)
    move = np.argmax(prediction)
    #print(labels[move])

    return labels[move]