import skimage.morphology
import skimage.filters
import numpy as np
from skimage.measure import label, regionprops_table
import matplotlib

def detect_nuclei(image, size = 200):
    
    # filtering
    image = skimage.filters.median(image,selem=np.ones((2,2)))
    # local thresholding
    image_local_threshold = skimage.filters.threshold_local(image,block_size=51)
    image_local = image > image_local_threshold
    # remove tiny features
    image_local_open = skimage.morphology.binary_opening(image_local, selem=skimage.morphology.disk(2))
    # label image
    image_labeled = label(image_local_open)
    # analyze regions
    our_regions = regionprops_table(image_labeled, properties = ('label','area','coords'))
    # create a new mask with constraints on the regions to keep
    newimage = np.zeros(image.shape)
    # fill in using region coordinates
    for x in range(len(our_regions['area'])):
        if our_regions['area'][x] > size:
            newimage[our_regions['coords'][x][:,0],our_regions['coords'][x][:,1]] = 1
            
    return newimage

def random_cmap():
    np.random.seed(42)
    cmap = matplotlib.colors.ListedColormap (np.random.rand(256,4))
    # value 0 should just be transparent
    cmap.colors[:,3] = 0.5
    cmap.colors[0,:] = 1
    cmap.colors[0,3] = 0
    
    # if image is a mask, color (last value) should be red
    cmap.colors[-1,0] = 1
    cmap.colors[-1,1:3] = 0
    return cmap

def myfun_in_script():
    a = 2
    print(f'final defintion: {a}')
    
def myfun_in_script2():
    print(f'final defintion: {a}')