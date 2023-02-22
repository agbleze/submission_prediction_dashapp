from dash import html, dcc
from PIL import Image
from helper_components import create_img_container


## grouped bar graph of various model report

classification_report_layout = html.Div(children=[create_img_container(img_src='',
                                                                       label='Classification Metrics of various algorithms',
                                                                       image_style=None
                                                                       )
                                                  ]
                                        )



