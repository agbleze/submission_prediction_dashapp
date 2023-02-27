import dash_bootstrap_components as dbc
from dash import html
import dash_trich_components as dtc
from dashapp.style import page_style
import pandas as pd

appside_layout = html.Div(
                            [
                                dtc.SideBar(
                                    [
                                        dtc.SideBarItem(id="id_proj_desc", label="Projection Description", 
                                                        icon="bi bi-body-text" 
                                                        ),
                                        dtc.SideBarItem(id="id_model_eval", label="Model Evaluation", 
                                                        icon="bi bi-bezier"
                                                        ),
                                        dbc.Collapse(id="id_collapse_model_eval", is_open=False,
                                                   # children=[dtc.SideBar(
                                                                            children=[dtc.SideBarItem(label="Cross validation",
                                                                                                      id="id_crossval_btn", 
                                                                                                      icon="fa-solid fa-caret-up",
                                                                                                      n_clicks=0,
                                                                                                    ),
                                                                                    dtc.SideBarItem(label="Classification report",
                                                                                                    id="id_classification_btn", icon="fa-brands fa-intercom",
                                                                                                    #value="classification_btn_clicked",
                                                                                                    #style=button_style,
                                                                                                    n_clicks=0,
                                                                                                ),
                                                                                    dtc.SideBarItem(label="ROC Curve",
                                                                                                    id="id_roc_btn", icon="bi bi-graph-up-arrow",
                                                                                                    #value="roc_btn_clicked",
                                                                                                    #style=button_style,
                                                                                                    n_clicks=0,
                                                                                                )
                                                                                ]
                                                                    #    )
                                                             # ]
                                                    ),
                                        
                                        
                                        dtc.SideBarItem(id="id_data_viz", label="Data Visualization", 
                                                        icon="bi bi-bar-chart"
                                                        ),
                                        
                                        dtc.SideBarItem(id="id_prediction", label="Prediction", 
                                                        icon="bi bi-plus-slash-minus"
                                                        ),
                                    ],
                                    bg_color="#0ca678",
                                ),
                                html.Div([], id="page_content", style=page_style)
                            ]
                        )



