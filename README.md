[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/guiwitz/BIAPy/master)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/guiwitz/BIAPy)

# BIAPy: *B*io*I*mage *A*nalysis with *Py*thon

This course is an introduction to bioimage processing with Python and Jupyter. It is composed of a series of Jupyter notebooks that can be simply [read](https://nbviewer.jupyter.org/github/guiwitz/BIAPy/tree/master/) or run interactively using either the [binder](#On-Binder) service, the [Google Colab](#On-Colab) service or via a [local installation](#Local-installation). The course covers basics, such as handling images as Numpy arrays, as well as a few more advanced topics such as tracking, registration etc. While some content presents fundamental concepts in image processing, this is *NOT* an image processing course. The goal of this cours is to give people with image processing background (e.g. in Fiji) the opportunity to discover how image processing is done in the Python world. In particular this course is not *exhaustive* as it only covers *selected* topics.

## Static notebooks

GitHub usually renders notebooks when browsing through the repository. If rendering fails you should use the [more stable rendering](https://nbviewer.jupyter.org/github/guiwitz/BIAPy/tree/master/) provided through nbviewer.

## Running the notebooks interactively

### On Binder

This is the preferred solution. This repository has been set-up to be run interactively without any installation required thanks to the [binder](https://mybinder.org/) service. An interactive Jupyter session can be started by clicking on the binder badge in the top left corner of this document. All the necessary packages and data are already pre-installed. If you want to explore this course via this method, you can stop reading here.

### On Colab

Alternatively, you can run these notebooks via Google Colab. To do that, click on the Colab badge in the top left corner of this document. This will bring you to the Colab service where you will be able to select a notebook to open.

The dataset cannot be "pre-installed" for you on Colab, so you will have to donwload it to Google Drive either directly using [this link](https://zenodo.org/record/3786307/files/Data.zip?download=1) or by visiting the [Zendo repository](https://zenodo.org/record/3786307/#.XrEx4tP7RTY) of the course.

In order to access Google Drive from Colab, you will need to connect to it from each notebook. For that, execute the cell at the top of each notebook named ```#Colab install``` and follow instructions. The path to access the file is then different from the default used via Binder (see above). If you unzip the Data.zip folder at the top of your Google Drive folder structure, you will have access to data when replacing the import path ```../Data/``` by ```/content/drive/My Drive/Data``` every time it appears in the code e.g.:

```python
skimage.io.imread('../Data/neuron.tif)
```
should become

```python
skimage.io.imread('/content/drive/My Drive/Data/neuron.tif)
```

Finally, as it is not possible to permanently install additional packages in Colab, the necessary packages to run a notebook are also installed when executing the ```#Colab install``` cell.

### Local installation

In order to run this course on your own computer you will have to:

1. Download this GitHub repository by using the "Clone or Download" button at the top right of this page.
2. Download the dataset for the course either directly using [this link](https://zenodo.org/record/3786307/files/Data.zip?download=1) or by visiting the [Zendo repository](https://zenodo.org/record/3786307/#.XrEx4tP7RTY) of the course.
3. Adjust your folders so that the Data folder is at the same level as the folder containing the notebooks:
   ```
   Mainfolder
    ├── BIAPy
    │   ├── 01-Python_bare_minimum.ipynb
    │   ├── 02-Numpy_images.ipynb
    │   └── ...
    ├── Data
    │   ├── neuron.tif
    │   ├── Klee.jpg
    │   └── ...
    └── ...
    ```
4. Install Jupyter and all necessary packages. We strongly recommend to install [Anaconda](https://docs.anaconda.com/anaconda/install/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (a light-weight Anaconda) to facilitate package management. If you install Anaconda, you can install all necessary packages by using the environment_minimal.yml file available in ```BIAPy/installation``` and following [these instructions](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-environments/#importing-an-environment). If you use miniconda or prefer to install packages via command line, open a terminal and:
   
   1. Move to the BIAPy/installation folder e.g.
   ```bash
   cd Mainfolder/BIAPy/installation
   ```
   2. Use the environment_minimal.yml file to install all packages in one go:
   ```bash
   conda env create -f environment_minimal.yml
   ```
   3. Now you have a specific environment called biapy that has all packages (including Jupyter) installed. **Everytime** you want to use it, open a terminal and start Jupyter:
   ```bash
   conda activate biapy
   ```
   4. To start a Jupyter session, activate your environment biapy (see 3.) and then start Jupyter:
   ```bash
   jupyter notebook
   ```
   Note that the Jupyter browser will open from *your current location in the terminal*. So don't start jupyter from within e.g. the installation folder as you won't be able to move higher.

Note that this procedure installs all packages *except* for [13-ML_based_segmentation.ipynb](13-ML_based_segmentation.ipynb). That notebook requires [Cellpose](https://github.com/mouseland/cellpose) and [StarDist](https://github.com/mpicbg-csbd/stardist). As installation of these packages might depend on your local configuration, we do not include them in the default installation. Consult their documentation on how to install them if you want to explore that notebook.


