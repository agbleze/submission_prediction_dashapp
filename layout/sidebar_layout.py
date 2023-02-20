import dash_bootstrap_components as dbc
from dash import html
import dash_trich_components as dtc

from helper_components import (create_offcanvans, output_card, 
                               plot_histogram, plot_scatterplot, make_boxplot,
                               CorrelationMatrix
                               )
import pandas as pd

appside_layout = html.Div(
    [
        dtc.SideBar(
            [
                dtc.SideBarItem(id="id_proj_desc", label="Projection Description", 
                                icon="fas fa-chart-bar" 
                                ),
                dtc.SideBarItem(id="id_model_eval", label="Model Evaluation", 
                                icon="fas fa-chart-line"
                                ),
                dbc.Collapse(id="id_model_eval_btns", is_open=False,
                             children=[
                                dbc.Button(
                                            "Cross validation",
                                            id="id_crossval_btn",
                                            value="crossval_btn_clicked",
                                            #style=button_style,
                                            n_clicks=0,
                                        ),
                                html.Hr(),
                                dbc.Button(
                                            "Classification report",
                                            id="id_classification_btn",
                                            value="classification_btn_clicked",
                                            #style=button_style,
                                            n_clicks=0,
                                        ),
                                html.Hr(),
                                dbc.Button(
                                            "ROC Curve",
                                            id="roc_btn",
                                            value="roc_btn_clicked",
                                            #style=button_style,
                                            n_clicks=0,
                                        )#,
                                #html.Hr(),
                                
                            ],
                             ),
                
                
                dtc.SideBarItem(id="id_data_viz", label="Data Visualization", 
                                icon="fas fa-chart-area"
                                ),
                
                dtc.SideBarItem(id="id_prediction", label="Prediction", 
                                icon="fas fa-signal"
                                ),
            ],
            bg_color="#0088BC",
        ),
        html.Div([], id="page_content"),
    ]
)



