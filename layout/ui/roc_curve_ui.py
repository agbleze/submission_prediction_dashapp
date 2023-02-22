from dash import html, dcc
import dash_bootstrap_components as dbc
from PIL import Image

logit_roc = Image.open()

from helper_components import create_img_container


roc_curve_layout = html.Div(children=[dbc.Row(children=[
                                                        create_img_container(),
                                                        create_img_container(),
                                                        create_img_container()
                                                        ]
                                                        ),

                                        dbc.Row(children=[
                                                            create_img_container(),
                                                            create_img_container(),
                                                            create_img_container()
                                                        ]
                                                )
                                    ]
                            )






