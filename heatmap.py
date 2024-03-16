import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
# Load data from file
data = np.loadtxt('file.txt')

# Extract x, y, and z data from columns
x = data[:, 0] * np.pi
y = data[:, 1]
z = data[:, 2] 

# Define number of bins for heatmap

n_bins_x = 24
n_bins_y = 500

# Create 2D histogram of x and y with z as weights
#heatmap, xedges, yedges = np.histogram2d(x, y, bins=n_bins, weights=z)
heatmap, xedges, yedges = np.histogram2d(x, y, bins=[n_bins_x, n_bins_y], weights=z)


#mask = heatmap.T < 0.1

# Apply the mask to the heatmap
#heatmap_masked = np.ma.masked_array(heatmap.T, mask)

#norm = colors.LogNorm(vmin=np.min(z), vmax=np.max(z))
# Set up plot
fig, ax = plt.subplots()

# Plot heatmap with colorbar
im = ax.imshow(heatmap.T, origin='lower', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], \
               cmap='plasma', aspect='auto',vmin=np.min(z), vmax=np.max(z), \
               interpolation='none')   #norm=norm # 
               


cbar = plt.colorbar(im)
cbar.ax.tick_params(labelsize=12,width=2) 
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.tick_params(axis='y', labelsize=12,width=2)  # Adjust labelsize as desired
ax.tick_params(axis='x', labelsize=12,width=2)  # Adjust labelsize as desired
ax.set_title('heatmap',fontsize=14)
#plt.savefig('Figure_2.png', dpi=300, bbox_inches='tight')
# Show plot
plt.show()
