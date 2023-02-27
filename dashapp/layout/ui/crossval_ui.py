from dash import html, dcc
import dash_bootstrap_components as dbc

from dashapp.arguments import args
from dashapp.helper_components import create_img_container


crossval_layout = html.Div(
                            children=[dbc.Row(children=[create_img_container(img_src=args.img_acc_score, 
                                                                             label='Cross Validation Accuracy Score', 
                                                                             image_style=None
                                                                            ),
                                                        create_img_container(img_src=args.img_fittime,
                                                                             label='Fit time for the various models'
                                                                             ),
                                                        create_img_container(img_src=args.img_scoretime,
                                                                             label='Score time for the various models',
                                                                             image_style=None
                                                                             )
                                                        ]
                                              )
                                    ]
                        )







