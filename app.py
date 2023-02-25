
#%%
from dash import html, Input, Output, State, dcc, callback_context
import dash_bootstrap_components as dbc
import pandas as pd
from dash.exceptions import PreventUpdate
from helper_components import ( 
                               plot_histogram, 
                               plot_scatterplot, 
                               make_boxplot, plot_barplot,
                               CorrelationMatrix, plot_histogram, 
                               plot_scatterplot, make_boxplot
                               )
import dash
from style import homepage_icon_style
from builders import (main_layout, app_description, explore_layout, 
                      histogram_layout, boxplot_layout, histogram_layout, 
                      scatter_layout, prediction_layout, 
                      multicoll_layout, intro_layout                      
                      )
import builders
import logging
from urllib.parse import unquote
import joblib
import functools
import plotly.express as px



from layout.sidebar_layout import appside_layout
#from layout.ui.project_description_ui import create_offcanvans
from layout.ui.data_viz_ui import data_viz_layout
from layout.ui.project_description_ui import project_descrip_layout
from layout.ui.prediction_ui import prediction_layout

#loaded_model = joblib.load(filename='bagging.model')
#data = pd.read_csv(r"Data/train_set.csv")



boxplot_features = ['extra_time_min', 'average_answer_time_in_min', 'progress_percent']

barplot_features = ['state_category', 'work_rate', 'extra_time_min', 'average_answer_time_in_min', 'progress_percent'] 
## add numeric features to it. When selected group by state category and find mean of numeric feature
# then plot bar graph


data = pd.read_csv(r'data/selected_data_features.csv')

best_model_loaded = joblib.load('model_store/best_model.model')

#%%
app = dash.Dash(__name__, external_stylesheets=[
                                                dbc.themes.SOLAR,
                                                dbc.icons.BOOTSTRAP,
                                                dbc.icons.FONT_AWESOME
                                            ],
                suppress_callback_exceptions=True,
                )

app.layout = appside_layout

app.validation_layout = html.Div(
                                [#main_layout,
                                appside_layout, 
                                project_descrip_layout, 
                                data_viz_layout,
                                prediction_layout #, 
                                # histogram_layout,
                                #scatter_layout, boxplot_layout, 
                                # multicoll_layout, intro_layout
                                ]
                            )


# %%
# @app.callback(
#     Output(component_id="main_content", component_property="children"),
#     Input(component_id="location", component_property="href"),
# )
# def show_page_display(href):
#     site_page = href
#     site_to_view = site_page.split("/")[-1]
#     if site_to_view == "explore":
#         return explore_layout 
#     elif site_to_view == 'predict':
#         return prediction_layout
#     else:
#         return app_description


@app.callback(
                Output("page_content", "children"),
                [
                    Input("id_proj_desc", "n_clicks_timestamp"),
                    #Input("id_model_eval", "n_clicks_timestamp"),
                    Input("id_data_viz", "n_clicks_timestamp"),
                    Input("id_prediction", "n_clicks_timestamp"),
                ],
            )
def sidebar_display(hist: str, boxplot: str, scatter: str, corr: str):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if not ctx.triggered:
        return project_descrip_layout #create_offcanvans()
    elif button_id == "id_proj_desc":
        return project_descrip_layout
    # elif button_id == "id_model_eval":
    #     return boxplot_layout
    elif button_id == "id_data_viz":
        return data_viz_layout
    elif button_id == "id_prediction":
        return prediction_layout
    else:
        return project_descrip_layout #intro_layout

@functools.lru_cache(maxsize=None)    
@app.callback(Output(component_id='missing_para_popup', component_property='is_open'),
              Output(component_id='desc_popup', component_property='children'),
              Output(component_id='prediction_output', component_property='children'),
              Input(component_id='submit_parameters', component_property='n_clicks'),
              Input(component_id='id_input_progress_percent', component_property='value'),
              Input(component_id='id_input_work_rate', component_property='value'),
              Input(component_id='id_input_extratime', component_property='value')
              )    
def make_prediction(button_click, progress_percent, work_rate, extratime):
    inputs = [progress_percent, work_rate, extratime]
    if not any(inputs):
        PreventUpdate
        
    ctx = dash.callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'submit_parameters':
        
        if not all(inputs):
            message = ('All parameters must be provided. Either some values have not \
                        been provided or invalid values were provided. Please select the \
                       right values for all parameters from the dropdown. \
                        Then, click on predict submission status button for \
                        prediction'
                       )
            return True, message, dash.no_update
        
        if all(inputs):
            input_data_dict = {'progress_percent': progress_percent, 'extra_time_min': extratime, 'work_rate': work_rate}
            prediction_input_data = pd.DataFrame(data=input_data_dict, index=[0])
            res = best_model_loaded.predict(prediction_input_data).item()
            prediction = "Pass" if res == 1 else 'Not pass'
            return False, dash.no_update, prediction


@functools.lru_cache(maxsize=None)                
@app.callback(Output(component_id='bar_graph', component_property='figure'),
              Input(component_id='id_bargraph_variable_select', component_property='value')
              )
def render_graph(variable_selected):
    if not variable_selected:
        PreventUpdate
    data_grouped_mean = data.groupby('submission_status')[variable_selected].mean().reset_index()
    return plot_barplot(data=data_grouped_mean, y_colname=variable_selected)

@functools.lru_cache(maxsize=None)
@app.callback(Output(component_id='boxplot_graph', component_property='figure'),
              Input(component_id='id_boxplot_variable_select', component_property='value')
              )
def render_boxplot_graph(boxplot_variable_selected):
    if not boxplot_variable_selected:
        PreventUpdate
    return make_boxplot(data=data, variable_name=boxplot_variable_selected)


## show dropdown ofvarious model metrics when model eval is clicked
@app.callback(Output(component_id='id_collapse_model_eval', component_property='is_open'),
              Input(component_id='id_model_eval', component_property='n_clicks'),
              State(component_id='id_collapse_model_eval', component_property='is_open')
            )
def toggle_sidebar_buttons(input_value, state_value):
    if input_value:
        state_value = not state_value
        return state_value
    state_value = state_value
    return state_value


# function to show evaluation page when an evaluation metric in collapse section is clicked
@app.callback(Output(component_id='', component_property=''),
              Input(component_id='id_crossval_btn', component_property='n_clicks_timestamp'),
              Input(component_id='id_classification_btn', component_property='n_clicks_timestamp'),
              Input(component_id='id_roc_btn', component_property='n_clicks_timestamp')
              )
def show_model_evaluation_page():
    button_id = callback_context.triggered[0]["prop_id"].split(".")[0]
    if not callback_context.triggered:
        button_id = 'No clicks yet'
    






@callback(
    Output("page_content", "children"),
    [
        Input("id_1", "n_clicks_timestamp"),
        Input("id_2", "n_clicks_timestamp"),
        Input("id_3", "n_clicks_timestamp"),
        Input("id_4", "n_clicks_timestamp"),
        Input("id_5", "n_clicks_timestamp"),
    ],
)
def sidebar_display(id1: str, id2: str, id3: str, id4: str, id5: str):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if not ctx.triggered:
        button_id = "No clicks yet"
    elif button_id == "id_1":
        return asset_portfolio.portfolio
    elif button_id == "id_2":
        return asset_portfolio.client_dashboard
    elif button_id == "id_3":
        return asset_portfolio.content_3
    elif button_id == "id_4":
        return asset_portfolio.content_4
    else:
        return asset_portfolio.content_5






# @app.callback(Output(component_id='project_canvans', component_property='is_open'),
#               Input(component_id='proj_desc', component_property='n_clicks'),
#               State(component_id='project_canvans', component_property='is_open')
#               )
# def toggle_project_description(proj_desc_button_clicked: str, is_open: bool) -> bool:
#     """
#     This function accepts click event input and the state of canvas component,
#     and change the state of the canvans component when a click occurs

#     Parameters
#     ----------
#     proj_desc_button_clicked : str
#         This parameter is a count of each click made on a button.
#     is_open : bool
#         Has the values True or False that specifies whether the canvas component is opened or not.

#     Returns
#     -------
#     bool
#         Has values True or False that determines whether the canvans component should be open.

#     """
#     if proj_desc_button_clicked:
#         return not is_open
#     else:
#         return is_open
    
    

if __name__=='__main__':
    app.run_server(port=8040, debug=False, use_reloader=False)


