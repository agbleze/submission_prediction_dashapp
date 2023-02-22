import dash_bootstrap_components as dbc
from dash import html, dcc
from numpy import place
from style import homepage_icon_style, page_style, input_style, button_style
import dash_trich_components as dtc
from helper_components import (create_offcanvans, output_card, create_dropdown,
                               plot_histogram, plot_scatterplot, make_boxplot,
                               CorrelationMatrix
                               )
import pandas as pd




#progress_percent	extra_time_min	work_rate

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
                                                dbc.Col(children=[output_card(id="prediction_output",
                                                                                card_label="Prediction",
                                                                                card_size=2,
                                                                                icon = 'fa-solid fa-check'
                                                                            )
                                                                ]
                                                        ),
                                                ]
                                            ),
                                        
                                        dbc.Row(
                                            dbc.Col(lg=4,
                                                    children=[
                                                        #html.Br(),
                                                        dbc.Label(''),
                                                        dbc.Button(id='submit_parameters',
                                                                    children='Predict Assignment status',
                                                                    style=button_style
                                                                )
                                                    ]
                                                    )
                                        )
                                    ]
                    )



