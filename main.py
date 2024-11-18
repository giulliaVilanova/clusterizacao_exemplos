import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

np.random.seed(42)
data = np.vstack([
    np.random.normal(loc=(2, 2), scale=0.5, size=(50, 2)),
    np.random.normal(loc=(8, 2), scale=0.5, size=(50, 2)),
    np.random.normal(loc=(5, 7), scale=0.5, size=(50, 2))
])

fig, axs = plt.subplots(2, 2, figsize=(12, 12))
axs = axs.ravel()

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(data)
axs[0].scatter(data[:, 0], data[:, 1], c=kmeans_labels, cmap='viridis', s=50)
axs[0].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=100)
axs[0].set_title("Centroid-based Clustering (K-Means)")

dbscan = DBSCAN(eps=0.8, min_samples=5)
dbscan_labels = dbscan.fit_predict(data)
axs[1].scatter(data[:, 0], data[:, 1], c=dbscan_labels, cmap='viridis', s=50)
axs[1].set_title("Density-based Clustering (DBSCAN)")

gmm = GaussianMixture(n_components=3, random_state=42)
gmm_labels = gmm.fit_predict(data)
axs[2].scatter(data[:, 0], data[:, 1], c=gmm_labels, cmap='viridis', s=50)
axs[2].set_title("Distribution-based Clustering (GMM)")

linkage_matrix = linkage(data, method='ward')
hc_labels = fcluster(linkage_matrix, t=3, criterion='maxclust')
axs[3].scatter(data[:, 0], data[:, 1], c=hc_labels, cmap='viridis', s=50)
axs[3].set_title("Connectivity-based Clustering (Hierarchical)")

plt.tight_layout()
plt.show()
