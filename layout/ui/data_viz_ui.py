import dash_bootstrap_components as dbc
from dash import html, dcc
from style import input_style


variables = ['progress_percent', 'extra_time_min', 'work_rate', 'average_answer_time_in_min', 'state_category']

data_viz_layout = dbc.Row([
    dbc.Col(id="",
            children=[dbc.Row(dbc.Label('Select variable for boxplot', style=input_style)),
                      dbc.Row(dcc.Dropdown(id='boxplot_variable_select',
                                            options=[{'label': var, 'value': var}
                                                    for var in variables
                                                    ]
                                            )
                              ),
                      dbc.Row(dcc.Loading(type='circle',
                                            children=[dbc.Col(#lg=9,
                                                            children=[dcc.Graph(id='boxplot_graph')]
                                                        )
                                                    ]
                                        )
                              )
                      ]
        
        ),
    dbc.Col(id='',
            children=[dbc.Row(dbc.Label('Select Variable to plot scatterplot with submission status', style=input_style)),
                      dbc.Row(dcc.Dropdown(id='variable_select',
                                            options=[{'label': var, 'value': var}
                                                    for var in variables
                                                    ]
                                        )
                              ),
                      dbc.Row(dcc.Loading(type='circle',
                                            children=[dbc.Col(#lg=9,
                                                            children=[
                                                                dcc.Graph(id='scatter_graph')
                                                            ]
                                                
                                                        )
                                                    ]
                                            )
                              )
                      ]
            ),
    dbc.Col(id='',
            children=[dbc.Row(dbc.Label('Select variable for boxplot', style=input_style)),
                      #dbc.Row(),
                      dbc.Row(dcc.Loading(type='circle',
                                            children=[dbc.Col(id='corr_graph',
                                                        children=[dcc.Graph(id='multicorr_graph',
                                                                            #figure=corr_fig
                                                                            )
                                                                ]
                                                    )
                                                    ]
                                        )
                              )
                      ]
            )
])





