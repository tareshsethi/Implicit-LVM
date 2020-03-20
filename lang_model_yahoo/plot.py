import umap 
# import umap.plot
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='white', context='notebook', rc={'figure.figsize':(14,10)})
# colors = {'happy.wav':1, 'sad.wav':2, 'angry.wav':3, 'disgust.wav':4, 'ps.wav':5, 'fear.wav':6, 'neutral.wav':7}

with open('test_path/embeddings.pickle', 'rb') as x:
    dictionary = pickle.load(x)
    X = dictionary['embeddings']
    Y = dictionary['sentences']

# with open('Y.pickle', 'rb') as y:
#     Y = np.asarray(pickle.load(y))

# mapping = umap.UMAP(
#                 n_neighbors=3,
#                 min_dist=0.0,
#                 metric='euclidean', 
#                 # n_components=3
#             )

# print(Y.shape)
reducer = umap.UMAP()
embedding = reducer.fit_transform(X)


colors = [0,1,2,3,4] + [5]*45

# plt.scatter(embedding[:, 0], embedding[:, 1], label=[x for x in Y.squeeze()], c=[sns.color_palette()[colors[x]] for x in Y.squeeze()])
plt.scatter(embedding[:, 0], embedding[:, 1], c=[x for x in colors], cmap='Spectral')
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP projection of the Iris dataset', fontsize=24)
plt.colorbar(boundaries=np.arange(8)-0.5).set_ticks(np.arange(7))
plt.savefig('test_path/umap.png')

print (Y[:5]) 

# umap.plot.points(mapper)
