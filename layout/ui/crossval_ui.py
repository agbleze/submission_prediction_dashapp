from dash import html, dcc
import dash_bootstrap_components as dbc
from PIL import Image

from helper_components import create_img_container


crossval_layout = html.Div(
                            children=[create_img_container(img_src='', label='Cross Validation Accuracy', 
                                                           img_style=None
                                                           )
                                    ]
                        )







