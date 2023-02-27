
#%%
from dash import html, Input, Output, State, dcc, callback_context
import dash_bootstrap_components as dbc
import pandas as pd
from dash.exceptions import PreventUpdate
from dashapp.helper_components import (make_boxplot, plot_barplot, get_path,
                               )
import dash
import joblib
import functools
import plotly.express as px


from .layout.sidebar_layout import appside_layout
from .layout.ui.data_viz_ui import data_viz_layout
from .layout.ui.project_description_ui import project_descrip_layout
from .layout.ui.prediction_ui import prediction_layout
from .layout.ui.classification_report_ui import classification_report_layout
from .layout.ui.crossval_ui import crossval_layout
from .layout.ui.roc_curve_ui import roc_curve_layout


data_path = get_path(folder_name='dashapp/data', file_name='selected_data_features.csv')

model_path = get_path(folder_name='dashapp/model_store', file_name='best_model.model')
data = pd.read_csv(data_path)

best_model_loaded = joblib.load(model_path)


app = dash.Dash(__name__, external_stylesheets=[
                                                dbc.themes.SOLAR,
                                                dbc.icons.BOOTSTRAP,
                                                dbc.icons.FONT_AWESOME
                                            ],
                suppress_callback_exceptions=True,
                )

app.layout = appside_layout

app.validation_layout = html.Div(
                                [
                                appside_layout, 
                                project_descrip_layout, 
                                data_viz_layout,
                                prediction_layout, 
                                classification_report_layout, 
                                crossval_layout, roc_curve_layout
                                ]
                            )



@app.callback(Output(component_id="page_content", component_property="children"),
              Input(component_id="id_proj_desc", component_property="n_clicks_timestamp"),
              Input(component_id="id_data_viz", component_property="n_clicks_timestamp"),
              Input(component_id="id_prediction", component_property="n_clicks_timestamp"),
              Input(component_id='id_crossval_btn', component_property='n_clicks_timestamp'),
              Input(component_id='id_classification_btn', component_property='n_clicks_timestamp'),
              Input(component_id='id_roc_btn', component_property='n_clicks_timestamp')
            )
def sidebar_display(id_proj_desc: str, id_data_viz: str, id_pred: str, id_crossval: str, id_classification, id_roc):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if not ctx.triggered:
        return project_descrip_layout
    elif button_id == "id_proj_desc":
        return project_descrip_layout
    elif button_id == "id_data_viz":
        return data_viz_layout
    elif button_id == "id_prediction":
        return prediction_layout
    elif button_id == 'id_crossval_btn':
        return crossval_layout
    elif button_id == 'id_classification_btn':
        return classification_report_layout
    elif button_id == 'id_roc_btn':
        return roc_curve_layout
    else:
        return project_descrip_layout
    
        

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
                        Then, click on predict Assignment status button for \
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

if __name__=='__main__':
    app.run_server(port=8040, debug=True, use_reloader=True)


