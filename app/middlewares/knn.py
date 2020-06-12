from sklearn.neighbors import NearestNeighbors
import cv2
import pickle
import tensorflow as tf
import numpy as np

extractModel = tf.keras.models.load_model('static/extractModel.h5')

def get_neighbors(category, imagePath):

    with open('static/feature-vector/FV_{}.pkl'.format(category),'rb') as f:
        featureVector = pickle.load(f)

    # with open('static/knn/{}KNN.pkl'.format(category),'rb') as f:
    #     neigh = pickle.load(f)

    # X = featureVector.reshape((len(featureVector),-1))
    featureVectors = []
    for i in featureVector.values:
        featureVectors.append(i[0])
    featureVectors = np.array(featureVectors)

    print('knn1')

    neigh = NearestNeighbors(n_neighbors = 5) #len(featureVector)
    neigh.fit(featureVectors)
    
    print('knn2')

    image = cv2.imread(imagePath)
    print('knn3')
    print(image.shape)
    image = tf.image.resize(image, [299, 299])
    print('knn4')
    image = image[:,:,:3]
    image = tf.expand_dims(image, 0)
    image = image/255.0

    return neigh.kneighbors(extractModel.predict(image))

# def get_neighbors(category, imagePath):

#     with open('static/feature-vector/FV_{}.pkl'.format(category),'rb') as f:
#         featureVector = pickle.load(f)

#     # with open('static/knn/{}KNN.pkl'.format(category),'rb') as f:
#     #     neigh = pickle.load(f)

#     # X = featureVector.reshape((len(featureVector),-1)) 

#     neigh = NearestNeighbors(n_neighbors = 5) #len(featureVector)

#     neigh.fit(featureVector)

#     image = cv2.imread('static/' + imagePath)
#     image = tf.image.resize(image, [299, 299])
#     image = image[:,:,:3]
#     image = tf.expand_dims(image, 0)
#     image = image/255.0

#     return neigh.kneighbors(extractModel.predict(image))
