from dash import html, dcc
import dash_bootstrap_components as dbc
from PIL import Image
from helper_components import create_img_container
from arguments import args


## grouped bar graph of various model report

classification_report_layout = html.Div(children=[dbc.Row(children=[create_img_container(img_src=args.img_decision_tree_report,
                                                                                        label='Classification report on test set for Decision tree',
                                                                                        image_style=None
                                                                                        ),
                                                                    create_img_container(img_src=args.img_extra_decison_report, 
                                                                                         label='Classification report on test set for Extra Decision tree',
                                                                                         image_style=None
                                                                                         ),
                                                                    create_img_container(img_src=args.img_logistic_report,
                                                                                         label='Classification report on test set for Logistic Regression',
                                                                                         image_style=None
                                                                                         )
                                                                    ]
                                                        ),
                                                  dbc.Row(children=[create_img_container(img_src=args.img_randomforest_report,
                                                                                        label='Classification report on test set for Random Forest',
                                                                                        image_style=None
                                                                                        ),
                                                                    create_img_container(img_src=args.img_svclinear_report, 
                                                                                         label='Classification report on test set for Support Vector Classifier (Linear)',
                                                                                         image_style=None
                                                                                         ),
                                                                    create_img_container(img_src=args.img_svcpoly_report,
                                                                                         label='Classification report on test set for Support Vector Classifier (Polynomial)',
                                                                                         image_style=None
                                                                                         )
                                                                    ]
                                                        ),
                                                  dbc.Row(children=[create_img_container(img_src=args.img_svcrbf_report,
                                                                                         label='Classification report on test set for Support Vector Classifier (Radial)',
                                                                                         image_style=None
                                                                                         )
                                                                    ]
                                                          )
                                                  
                                                  ]
                                        )



