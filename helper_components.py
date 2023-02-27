from dash import dcc, html
import dash_bootstrap_components as dbc
from style import cardbody_style, card_icon, cardimg_style, card_style
import plotly.express as px
import pandas as pd
from typing import List, Optional, Dict
import os



def output_card(id: str = None, card_label: str =None,
                style={"backgroundColor": 'yellow'},
                icon: str ='bi bi-cash-coin', card_size: int = 4):
    return dbc.Col(lg=card_size,
                        children=dbc.CardGroup(
                        children=[
                                    dbc.Card(
                                    children=[
                                        dcc.Loading(type='circle', children=html.H3(id=id)),
                                        html.P(card_label)
                                    ]
                                ),
                            dbc.Card(
                                    children=[
                                        html.Div(
                                            className=icon,
                                            style=card_icon
                                        )
                                    ],
                                    style=style
                            )
                        ]
                    )
                )


def create_offcanvans(id: str, title: str, is_open=False):
    return html.Div(
        [
            dbc.Offcanvas(
                id=id,
                title=title,
                is_open=is_open,
                children=[
                    dcc.Markdown('''
                                    #### Project description

                                    The aim of this project is to predict how often a hotel ad will be clicked
                                    based on certain characteristics of the hotel. The bidding team supported by
                                    data science team sought to obtain an intelligent tool that can enable them 
                                    gain insight on hotel ads clicks to help advertisers run well performing campaigns on our website.
                                    
                                    #### Features / variables used

                                    The dataset had a number of variables used as predictors and target 
                                    variable.
                                    These include the following;

                                    ##### Predictor variables
                                    __content score__ : Describes the quality of the content that is provided for 
                                                        the hotel on a scale from 0 (worst) to 100 (best)
                                    
                                    __City id__ : Describes the city the hotel is located in

                                    __n images__ : Number of images that are available for the given hotel

                                    __distance to center__ : Distance (in meters) of the hotel to the nearest city center

                                    __avg rating__ : average rating of the hotel on a scale from 0 (worst) to 100 (best)

                                    __n reviews__ : Number of reviews that are available for that hotel
                                    
                                    __avg rank__: Average position the hotel had in the list
                                    
                                    __avg price__: Average price in Euro of the hotel
                                    
                                    __avg saving percent__: Average saving users achieve on this hotel by using trivago, 
                                                            i.e. the relative difference between the cheapest and most 
                                                            expensive deal for the hotel
                                                            
                                    __stars__: Number of stars on a scale of 1 (worst) to 5 (best)

                                    ##### Target variable
                                    
                                    __n _licks__: the number of clicks the hotel has received in a specific time frame 

                                    #### Tools and method used
                                    
                                    The aim of the modelling task is to develop an accurate model that is computationally least expensive. 
                                    By this, a benchmark model was defined as a minimal standard against which the model developed is deem acceptable or not. 
                                    An exploratory analysis was undertaken to decide which algorithmn to employ. The findings of the 
                                    exploratory analysis which included predictor variables not having a linear relationship with the target 
                                    variable, potential loss of about 28% of data attributable to missing data, 
                                    absence of multicollinearity and presence of outliers among others, informed the decision to 
                                    use a non-parametric model hence decision tree based model. In other to choose a model that 
                                    handles missing data relatively well, HistGradientBoostingRegressor was used. 
                                    Various approaches to improving model performance were also demonstrated within the limited 
                                    time and computational power available. Hyperparameter tuning was undertaken with grid search cross 
                                    validation using few combinations of parameters. With the improved model from hyperparameter tuning, 
                                    bagging was employed to further reduce error and overfitting.                                    

                                    With the user interface provided here, various features describing hotel 
                                    characteristics can be selected to predict number of clicks on ads.

                                    Among others, the tools used included the following

                                    * sklearn as an ML library with Bagging and HistGradientBoostingRegressor used to
                                        develop the machine learning model
                                    * Dash and other dependencies to build this web application as the User Interface 
                                        for making predictions with the model
                                    * Plotly for interactive data visualization

                                    #### Project output

                                    The main output of this project were the following

                                    * Machine learning model developed
                                    * Data Analytic and Machine learning web application
                                '''
                                )
                    ]
            ),
        ]
    )



# function to create boxplot
def make_boxplot(data: pd.DataFrame, variable_name: str):
    """This function accepts a data and variable name and returns a boxplot

    Args:
        data (pd.DataFrame): Data to visualize
        variable_name (str): variable to visualize with boxplot
    """
    data = data[[variable_name]].dropna()
    fig = px.box(data_frame=data, y = variable_name,
                 template='plotly_dark', height=700,
                 title = f'Boxplot to visualize outliers in {variable_name}'
                 )
    return fig
    
    
def plot_histogram(data: pd.DataFrame, colname: str):
    """Plot the distribution of variable using a histogram

    Args:
        data (pd.DataFrame): Data to use for plotting
        
        colname (str): column name or name of variable to plot 
    """
    data = data[[colname]].dropna()
    fig = px.histogram(data, x=colname, histnorm='probability density',
                       title=f'Distribution of {colname}',
                       height=700,
                       template='plotly_dark'
                       )
    return fig
    
    
def plot_barplot(data: pd.DataFrame,y_colname: str, 
                x_colname: str = 'submission_status',
                    
                ):
    """ Barplot to visualize relationship between categorical and numeric variable. 
    Args:
        data (pd.DataFrame): Data which contains variables to plot
        
        y_colname (str): column name (variable) to plot on y-axis
        x_colname (str): column name (variable) to plot on x-axis
    """
    data = data[[x_colname, y_colname]].dropna()
    fig = px.bar(data, x=x_colname, y=y_colname,
                     title=f'Relation between {x_colname} and {y_colname}',
                     template='plotly_dark', height=700
                     )
    return fig    



class CorrelationMatrix:
    def __init__(self, data: pd.DataFrame, columns: List[str] = None) -> None:
        self.data = data
        self.columns = columns
        
    def create_correlation(self):
        if not self.columns:
            X = self.data.drop(columns=['hotel_id', 'n_clicks', 'city_id'])
        else:
            X = self.data[self.columns]
        self.corr = round(X.corr(), 3)
        return self.corr
    
    def plot_correlation(self, corr_matrix):
        self.corr_matrix = corr_matrix
        self.fig = px.imshow(corr_matrix, text_auto=True, aspect="auto",
                             title='Correlation among Predictor Variables',
                             template='plotly_dark',
                             height=700
                             )
        return self.fig
        
        
        
        
model_eval_dropdown_values = ['Cross Validation', 'Classification report', 'ROC Curve']        
def create_dropdown(dropdown_values: List = model_eval_dropdown_values, 
                    dropdown_id = 'model_eval_variable_select', 
                    default_value = None):
    return dbc.Col(#lg=3,
                    children=[
                        dcc.Dropdown(id=dropdown_id,
                                options=[{'label': var, 'value': var}
                                        for var in dropdown_values
                                        ],
                                value=default_value
                                )
                            ]
                )
        

def create_img_container(img_src: str, label: str, image_style: dict = None, column_width=4):
    return dbc.Col(lg=column_width,
                   children=[dbc.Label(label), html.Br(),
                            dbc.Card(
                                        [
                                        dbc.CardImg(
                                                    src=img_src,
                                                    top=True,
                                                    style=image_style,
                                                ),
                                        ],
                                    )
                            ]
                    )




def create_dropdown_with_graph_figure(label: str, dropdown_id: str, dropdown_values: List,
                                      graph_id: str, loading_type: str = 'circle',
                                      label_style: Dict = None, column_width=6, default_value = None,
                                      **kwargs
                                      ):
        """Returns a column with a label, dropdown and graph with loading status

        Args:
            label (str): Input for the label
            dropdown_id (str): Unique id for downdown component
            graph_id (str): Unique id for graph component
            loading_type (str, optional): Defaults to 'circle'. Shows progress of background process for plotting graph.
            label_style (dict, optional): Defaults to None. The css style to apply to label

        Returns:
            _type_: a column with label, dropdown and graph for plotting
        """
        return dbc.Col(id="", lg=column_width,
                        children=[dbc.Row(dbc.Label(label, style=label_style)),
                                dbc.Row(create_dropdown(dropdown_id = dropdown_id, dropdown_values = dropdown_values,
                                                        default_value=default_value
                                                        )
                                        ),
                                dbc.Row(dcc.Loading(type=loading_type,
                                                    children=[dbc.Col(#lg=9,
                                                                        children=[dcc.Graph(id=graph_id)]
                                                                        )
                                                        ]
                                                )
                                        )
                                ]
                )
        
        

# function to get the full pathname for the data file

def get_path(folder_name: str, file_name: str):
    cwd = os.getcwd()
    return f"{cwd}/{folder_name}/{file_name}"
 
 
 
 
 
        
        