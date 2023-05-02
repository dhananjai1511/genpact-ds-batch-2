import numpy as np

# assume we have a dataset X with shape (n_samples, n_features)
X = ...

# compute the mean of X
mean_X = np.mean(X, axis=0)

# center X around the mean
X_centered = X - mean_X

# compute the covariance matrix of X
cov_X = np.cov(X_centered, rowvar=False)

# perform SVD on the covariance matrix
eig_vals, eig_vecs = np.linalg.eigh(cov_X)

# sort the eigenvectors in descending order of their corresponding eigenvalues
eig_vecs = eig_vecs[:, ::-1]

# select the top k eigenvectors to reduce the dimensionality of X
k = ...

# compute the lower-dimensional representation of X
X_reduced = np.dot(X_centered, eig_vecs[:, :k])

# reconstruct the original data from the lower-dimensional representation
X_reconstructed = np.dot(X_reduced, eig_vecs[:, :k].T) + mean_X






fig, ax = plt.subplots()
ax.plot(np.arange(len(eigvals)) + 1, eigvals, 'bo-', linewidth=2)
ax.set_xlabel('Principal Component')
ax.set_ylabel('Eigenvalue')
ax.set_title('Scree Plot')
plt.show()