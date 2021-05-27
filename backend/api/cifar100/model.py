# from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, MaxPooling2D, Conv2D, Dropout, Flatten
from tensorflow.keras.constraints import MaxNorm
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.utils import to_categorical
from PIL import Image
import numpy as np
import os


fine_labels = ['apple', 'aquarium_fish', 'baby', 'bear', 'beaver', 'bed', 'bee', 'beetle', 'bicycle', 'bottle', 'bowl', 'boy', 'bridge', 'bus', 'butterfly', 'camel', 'can', 'castle', 'caterpillar', 'cattle', 'chair', 'chimpanzee', 'clock', 'cloud', 'cockroach', 'couch', 'crab', 'crocodile', 'cup', 'dinosaur', 'dolphin', 'elephant', 'flatfish', 'forest', 'fox', 'girl', 'hamster', 'house', 'kangaroo', 'keyboard', 'lamp', 'lawn_mower', 'leopard', 'lion', 'lizard', 'lobster', 'man', 'maple_tree', 'motorcycle', 'mountain',
               'mouse', 'mushroom', 'oak_tree', 'orange', 'orchid', 'otter', 'palm_tree', 'pear', 'pickup_truck', 'pine_tree', 'plain', 'plate', 'poppy', 'porcupine', 'possum', 'rabbit', 'raccoon', 'ray', 'road', 'rocket', 'rose', 'sea', 'seal', 'shark', 'shrew', 'skunk', 'skyscraper', 'snail', 'snake', 'spider', 'squirrel', 'streetcar', 'sunflower', 'sweet_pepper', 'table', 'tank', 'telephone', 'television', 'tiger', 'tractor', 'train', 'trout', 'tulip', 'turtle', 'wardrobe', 'whale', 'willow_tree', 'wolf', 'woman', 'worm']
coarse_labels = ['aquatic_mammals', 'fish', 'flowers', 'food_containers', 'fruit and vegetables', 'vehicles', 'household furniture', 'insects', 'large carnivores', 'large man-made_outdoor_things',
                 'large_natural_outdoor_scenes', 'large_omnivores_and_herbivores', 'medium_mammals', 'non-insect_invertebrates', 'people', 'reptiles', 'small_mammals', 'trees', 'household electrical devices', 'vehicles_2']
# def train():
#     # load dataset
#     (train_X, train_Y), (test_X, test_Y) = cifar10.load_data()

#     train_x = train_X.astype('float32')
#     test_X = test_X.astype('float32')

#     train_X = train_X/255.0
#     test_X = test_X/255.0

#     train_Y = to_categorical(train_Y)
#     test_Y = to_categorical(test_Y)

#     num_classes = test_Y.shape[1]

#     # model
#     model = Sequential()
#     model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3),
#                      padding='same', activation='relu',
#                      kernel_constraint=MaxNorm(3)))
#     model.add(Dropout(0.2))
#     model.add(Conv2D(32, (3, 3), activation='relu',
#                      padding='same', kernel_constraint=MaxNorm(3)))
#     model.add(MaxPooling2D(pool_size=(2, 2)))
#     model.add(Flatten())
#     model.add(Dense(512, activation='relu', kernel_constraint=MaxNorm(3)))
#     model.add(Dropout(0.5))
#     model.add(Dense(num_classes, activation='softmax'))

#     sgd = SGD(lr=0.01, momentum=0.9, decay=(0.01/25))

#     model.compile(loss='categorical_crossentropy',
#                   optimizer=sgd,
#                   metrics=['accuracy'])

#     model.fit(train_X, train_Y,
#               validation_data=(test_X, test_Y),
#               epochs=15, batch_size=32)

#     _, acc = model.evaluate(test_X, test_Y)
#     print(acc*100)

#     model.save("model1_cifar_10epoch.h5")


def pred_cifar_100(img_path):
    path = os.path.join("./api/cifar100", 'model1_cifar_100epoch_15.h5')
    path = os.path.abspath(path)
    model = load_model(path)
    results = {
        1: 'aquatic mammals',
        2: 'fish',
        3: 'flowers',
        4: 'food',
        5: 'fruit',
        6: 'household electrical devices',
        7: 'household furniture',
        8: 'insects',
        9: 'large carnivores',
        10: 'large man-made outdoor things',
        11: 'large natural outdoor scenes',
        12: 'large omnivores and herbivores',
        13: 'medium-sized mammals',
        14: 'non-insect invertebrates',
        15: 'people',
        16: 'reptiles',
        17: 'small mammals',
        18: 'trees',
        19: 'vehicles 1',
        20: 'vehicles 2'
    }

    im = Image.open(img_path)

    im = im.resize((32, 32))
    im = np.expand_dims(im, axis=0)
    im = np.array(im)
    pred = model.predict_classes([im])[0]
    print(pred, results[pred], coarse_labels[pred])
    return coarse_labels[pred]
