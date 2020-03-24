# Product Categorization
...just two simple ways to obtain a product category from a given product description.

# Requirements

In order to avoid uploading a 2.5 GB Docker image, I just pushed the source files and my pip-frozen *requirements.txt* file. The code has been written on Python 3.6.9, so don't use Python 2 please. To install the requirements use:

`pip3 install -f requirements.txt`

# Training

Run a jupyter notebook and open one of the *train\_\*.ipynb* files
The code is documented and self explaining. It reads the data file *testset_C.csv*, converts it to training and test data and trains a neural network (DL) or a Unigram model on it.
The models and data are saved in the *\*\_data* folders.

# Inference

To start a server providing the REST API use:

`python3 flaskapi.py`

This server listens on a certain port, which is defined in the *flaskapi.py* file. There is no need to change it.

The client side has been implemented in another python file, which sends POST requests to the server endpoints (*/request and /request_dl*) containing a JSON dict with one key *description*. The server unpacks the description text and runs one of the models to predict the category.
It sends back a JSON dict with *category* and *inf_time* as keys, which contain the predicted product category and the inference time to complete the prediction.

# Drawbacks

This is just a simple first short. In order to time issues the code is not perfect. So it doesn't handle exceptions properly. The server and client contain only simple sequential POST requests, no configuration opportunities no beautifying behind it. No web mask...this can all be done in further improvements.
