## Dash app package powered by machine learning as POC for an online education provider

## Project description

The aim of this project is to predict the status of assignments submitted by students which could be either pass or not pass. The client is an online education provider who sought to obtain an intelligent tool that can enable the prediction of whether a student will pass an assignment submitted or not and by this pre-emptively develop guidelines and procedures that enable students graduate on time while also plan resources to student class occupany requirements.

The data exploration and development of machine learning models to satisfy the use case is captured in detail in a different repo. If you are interested in the details of the modelling procedure then please refer to the repository [here](https://github.com/agbleze/modeling_submission_pass)


This repository is essentially a package that can be run to obtain a web application with a user interface for visualizing the various features and using the model developed to make prediction in production when deployed.


## How to run the code (python package)

1. First create a virtual environment and activate the environment to create an isolated environment for running the code. 
 
This can be done using python from the terminal as follows (The commands are for MacOs. Please run the equivalent of your operating system in case that differs);

- I. Create a virtual environment called env or specify path to directory where you want it to be created (choose a name of your choice)

``` python3 -m venv env```

- II. Activate virtual environment (Navigate to where you created the virtual env and activate as location/virtual_env/bin/activate as demonstrated as follows

``` source env/bin/activate ```

2. Clone this repository using the code below;

```git clone https://github.com/agbleze/submission_prediction_dashapp.git ```

3. Install the packahe cloned with the commands below;

```pip install . ```

4. Run the application

```python -m dashapp```


## Expected result

When the app is run, the result is a dash application with the url to access it provided in your terminal. It will be running at port 8666 by default. This port is chosen as it is unlikely to be in use at your end. The url to access the app is expected to be similar to: http://127.0.0.1:8666/. Once the app is running locally, you can copy and paste the url produced in your browser to access the app and play around it.


## Note:

The model used for the prediction can be improved and more data and the user interface is another area to be attended to. This is meant to be a Proof of Concept to inspire how to handle a project from ideation to serving a product powered by machine learning in a production.


