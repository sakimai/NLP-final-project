import numpy as np
import matplotlib.pyplot as plt
import os

print(os.path.splitext('clipscore_matrix.npy'))

# Load the matrix from the .npz file
clipscore_matrix = np.load('clipscore_matrix.npy') # Typically the key is 'arr_0' if no name was specified during saving

print(clipscore_matrix.shape)

# Visualize the matrix
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

im1 = axs[0].imshow(clipscore_matrix[:200, :200])
axs[0].set_title("Matrix slice 0")
fig.colorbar(im1, ax=axs[0])

plt.tight_layout()

# Save the plot to a PNG file
plt.savefig("clipscore_matrix.png", format="png", dpi=300)

# Show the plot
plt.show()
