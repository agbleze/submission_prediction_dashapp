
import dash_bootstrap_components as dbc
from dash import html, dcc

def create_markdown():
    return html.Div(
                children=[
                    dcc.Markdown('''
                                    ## Project description

                                    The aim of this project is to predict the status of assignments submitted 
                                    by students which could be either pass or not pass. 
                                    The client is an online education provider who sought to obtain
                                    an intelligent tool that can enable the prediction of whether a student 
                                    will pass an assignment submitted or not and by this pre-emptively develop guidelines and 
                                    procedures that enable students graduate on time while also plan resources 
                                    to student class occupany requirements. 
                                    
                                    This proof of concept is a uses available data to build this tool to be used by 
                                    both teachers and students.

                                    ### Variables used

                                    The dataset had a number of variables used as predictors for
                                    predicting whether a student will pass an assignment submitted or not. Some of the variables 
                                    captured in the dataset includes the following
                                    
                                    * Minimum time required for the task (minutes)
                                    * Maximum time required for the task (minutes)
                                    * Percentage of course completed as progress
                                    * Average answer time (hours)
                                    * Assignment status with values as 'approved', 'almost_there', 'waiting_for_review', 'a_little_more' and 'not_yet'.
                                    This is the target variable.
                                    
                                    
                                    ### Data exploration and transformation
                                    
                                    #### Target variable
                                    __Assignment status__: as a binary target variable has 5 classes are present contrary to only two classes 
                                                            expected. The variable was transformed to a binary one by reclassifying all submissions 
                                                            that were not approved as not passed and those approved as passed. 
                                                            The target variable is then converted into numeric values of 0 and for not pass and pass respectively.

                                    
                                    
                                    #### Predictor variables selected
                                    
                                    All time variables were converted into minutes to have a common unit. New features were created with interpretatbility
                                    and recourse to business logic in mind.
                                    Chi-squared test was used to determine and select features that had strong influence on the target variable and 
                                    correlation analysis was used to handle multicollinearity. The selected predictors for the modelling task are as follows;
                                    
                                    __Progress Percent__: Describes the percentage of course work completed at the time of undertaking the assignment.
                                    
                                    __ Work rate__: is a predictor with values 'slow', 'normal' and 'fast'. This feature was engineered from average answer time,
                                    minimum and maximum task time. Where the time spent for a student's submission is higher than maximum task time, work rate 
                                    is defined as slow. Where time used to complete an assignment by a student is within the range of minimum and maximum 
                                    task time required then work rate is define as 'normal'. Work rate is 'fast' when student uses less time than the required 
                                    minimum to complete the assignment.
                                     
                                    __Extra time__: Is the excess amount of minutes above the maximum task time required used by a student to complete the assignment.
                                    By this, a student with a normal or fast work rate for an assignment completed will have 0 extra time. 
                                    
                                    ### Tools and method used
                                    
                                    Binary classification as a supervised machine learning techniqued was employed with several models developed and evaluated. 
                                    For the development of the model, class weight was set to balance to cater for the unbalance data.
                                    
                                    Selection of final model was based on 10 fold cross validation with the evaluation metric defined as Accuray. There is still
                                    room for improvement of model performance to be achived by hyperparameter tuning and gradient boosting.
                                    
                                    The selected model is used to create an API that receives request, makes and send prediction as response
                                    to this web application.

                                    With the user interface provided here, various features a students assignment submission can be selected to make a prediction.

                                    Among others, the tools used included the following

                                    * Scikit-learn as the machine learning library to develop the machine learning models
                                    * Plotly for interactive visualization
                                    * Pandas, numpy, scipy and statistic packages were used for exploratory analysis and statistical test  
                                    * Dash to build this web application as the User Interface
                                    * Flask to develop the API for the machine learning model


                                    #### Project output

                                    The main output of this project were the following

                                    * Machine learning API deployed
                                    * Machine learning package
                                    * Machine learning web application
                                '''
                                )
                    ]
        
    )
    
        
    
project_descrip_layout = dbc.Row(dbc.Col(children=[create_markdown()
                                                ]
                                    )
                                )    
 
 
    