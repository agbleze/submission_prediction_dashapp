import dash_bootstrap_components as dbc
from dash import html, dcc
from dashapp.style import input_style, button_style
from dashapp.helper_components import (output_card, create_dropdown
                               )
import pandas as pd


prediction_layout = html.Div(children=[dbc.Row([
                                                dbc.Col([
                                                        dbc.Modal(id='missing_para_popup', is_open=False,
                                                                    children=[
                                                                            dbc.ModalBody(id='desc_popup')
                                                                        ]
                                                                )
                                                        ]
                                                        )
                                                ]
                                                ),
                                    
                                        dbc.Row(
                                                [dbc.Col(children=[
                                                                    dbc.Label('Describes progress (%)',
                                                                            style=input_style
                                                                            ),
                                                                    html.Br(),
                                                                    dcc.Input(id='id_input_progress_percent',
                                                                            placeholder="Progess",
                                                                            min=0, max=100, type='number',
                                                                            debounce=True
                                                                        )
                                                                ]
                                                        ),
                                                dbc.Col(children=[
                                                                    dbc.Label('Describes work rate (%)',
                                                                            style=input_style
                                                                            ),
                                                                    html.Br(),
                                                                    create_dropdown(dropdown_values = ['slow', 'normal', 'fast'],
                                                                                    dropdown_id = 'id_input_work_rate'
                                                                                    )
                                                                ]
                                                        ),
                                                dbc.Col(children=[
                                                                    dbc.Label('Extra time, selecting fast or normal for work rate means 0 extra time used to be appropriately selected',
                                                                            style=input_style
                                                                            ),
                                                                    html.Br(),
                                                                    dcc.Input(id='id_input_extratime',
                                                                            placeholder="Extra time in minutes used beyond the allowed time for assignment",
                                                                            min=0, max=200, type='number',
                                                                            debounce=True
                                                                        )
                                                                ]
                                                        ),
                                                ]
                                            ),
                                        
                                        dbc.Row(
                                            children=[dbc.Col(lg=4,
                                                                children=[
                                                                        dbc.Label(''),
                                                                        dbc.Button(id='submit_parameters',
                                                                                children='Predict Assignment status',
                                                                                style=button_style
                                                                                )
                                                                ]
                                                        ),
                                                      dbc.Col(children=[output_card(id="prediction_output",
                                                                                card_label="Prediction",
                                                                                card_size=4,
                                                                                icon = 'fa-solid fa-check'
                                                                            )
                                                                ]
                                                        )
                                                ]
                                        )
                                    ]
                    )



