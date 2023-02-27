from dash import html, dcc
import dash_bootstrap_components as dbc
from dashapp.arguments import args


from dashapp.helper_components import create_img_container


roc_curve_layout = html.Div(children=[dbc.Row(children=[
                                                        create_img_container(img_src=args.img_extra_decision_roc,
                                                                             label='ROC curve of test set for Extra Decision tree'
                                                                             ),
                                                        create_img_container(img_src=args.img_decision_tree_roc,
                                                                             label='ROC Curve of test set for Decision tree'
                                                                             ),
                                                        create_img_container(img_src=args.img_randomforest_roc,
                                                                             label='ROC Curve of test set for Random Forest'
                                                                             )
                                                        ]
                                                ),

                                        dbc.Row(children=[
                                                            create_img_container(img_src=args.img_logistic_roc,
                                                                                 label='ROC Curve of test set for Logistic Regression'
                                                                                 ),
                                                            create_img_container(img_src=args.img_svclinear_roc,
                                                                                 label='ROC Curve of test set for Support Vector Classifier (Linear)'
                                                                                 ),
                                                            create_img_container(img_src=args.img_svcpoly_roc,
                                                                                 label='ROC Curve of test set for Support Vector Classifier (Polynomial)'
                                                                                 )
                                                        ]
                                                ),
                                        dbc.Row(children=[create_img_container(img_src=args.img_svcrbf_roc,
                                                                               label='ROC Curve of test set for Support Vector Classifier (Radial)'
                                                                               )
                                                          ]
                                                )
                                    ]
                            )






