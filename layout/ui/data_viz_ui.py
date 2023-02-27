import dash_bootstrap_components as dbc
from dash import html, dcc
from helper_components import create_dropdown_with_graph_figure
from typing import List, Dict


boxplot_features = ['extra_time_min', 'average_answer_time_in_min', 'progress_percent']

barplot_features = ['extra_time_min', 'average_answer_time_in_min', 'progress_percent'] 

data_viz_layout = dbc.Row([create_dropdown_with_graph_figure(label='Select variable for boxplot', 
                                                             dropdown_values=boxplot_features,
                                                             dropdown_id='id_boxplot_variable_select',
                                                             graph_id='boxplot_graph',
                                                             default_value='progress_percent'),
                           create_dropdown_with_graph_figure(label='Select Variable to visualize how it related with target - submission status',
                                                             dropdown_values=barplot_features,
                                                             dropdown_id='id_bargraph_variable_select', 
                                                             graph_id='bar_graph', default_value='extra_time_min'
                                                        )
                        ]
                        )





