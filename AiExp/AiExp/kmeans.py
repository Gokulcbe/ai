import numpy as np

class KMeans:
    def __init__(self, n_clusters, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]
        for _ in range(self.max_iter):
            # Assign each data point to the nearest centroid
            labels = self._assign_clusters(X)
            # Update centroids based on the mean of data points assigned to each cluster
            new_centroids = self._update_centroids(X, labels)
            # Check for convergence
            if np.allclose(new_centroids, self.centroids):
                break
            self.centroids = new_centroids
        return self

    def _assign_clusters(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

    def _update_centroids(self, X, labels):
        new_centroids = np.empty_like(self.centroids)
        for i in range(self.n_clusters):
            new_centroids[i] = np.mean(X[labels == i], axis=0)
        return new_centroids

if __name__ == "__main__":
    # Example usage:
    # Generate some random data points
    np.random.seed(42)
    X = np.random.rand(100, 2)
    
    # Number of clusters
    k = 3
    
    # Instantiate and fit KMeans model
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    
    # Get cluster centroids and labels
    centroids = kmeans.centroids
    labels = kmeans._assign_clusters(X)
    
    print("Cluster Centroids:")
    print(centroids)
    print("\nCluster Labels:")
    print(labels)
