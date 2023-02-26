from argparse import Namespace
from helper_components import get_path
from PIL import Image

roc_decision_tree_path = get_path(folder_name='img', file_name='decision_tree_ROC.png')
roc_extradecision_path = get_path(folder_name='img', file_name='extra_decision_ROC.png')
roc_randomforest_path = get_path(folder_name='img', file_name='randomForest_ROC.png')
roc_logistic_path = get_path(folder_name='img', file_name='logistic_ROC.png')
roc_svclinear_path = get_path(folder_name='img', file_name='svcLinear_ROC.png')
roc_svcpoly_path = get_path(folder_name='img', file_name='svcPoly_ROC.png')
roc_svcrbf_path = get_path(folder_name='img', file_name='svcRbf_ROC.png')

acc_score_path = get_path(folder_name='img', file_name='classifiers_accuracy_score.png')
fittime_path = get_path(folder_name='img', file_name='classifiers_fittime.png')
scoretime_path = get_path(folder_name='img', file_name='classifiers_scoretime.png')

report_decision_tree_path = get_path(folder_name='img/reports', file_name='decision_tree_report.png')
report_extradecision_path = get_path(folder_name='img/reports', file_name='extra_decision_tree_report.png')
report_logistic_path = get_path(folder_name='img/reports', file_name='logistic_report.png')
report_randomforest_path = get_path(folder_name='img/reports', file_name='random_forest_report.png')
report_svclinear_path = get_path(folder_name='img/reports', file_name='svc_linear_report.png')
report_svcpoly_path = get_path(folder_name='img/reports', file_name='svc_poly_report.png')
report_svcrbf_path = get_path(folder_name='img/reports', file_name='svc_rbf_report.png')


img_decision_tree_roc = Image.open(roc_decision_tree_path)
img_extra_decision_roc = Image.open(roc_extradecision_path)
img_randomforest_roc = Image.open(roc_randomforest_path)
img_logistic_roc = Image.open(roc_logistic_path)
img_svclinear_roc = Image.open(roc_svclinear_path)
img_svcpoly_roc = Image.open(roc_svcpoly_path)
img_svcrbf_roc = Image.open(roc_svcrbf_path)

img_acc_score = Image.open(acc_score_path)
img_fittime = Image.open(fittime_path)
img_scoretime = Image.open(scoretime_path)

img_decision_tree_report = Image.open(fp=report_decision_tree_path)
img_extra_decison_report = Image.open(fp=report_extradecision_path)
img_logistic_report = Image.open(fp=report_logistic_path)
img_randomforest_report = Image.open(fp=report_randomforest_path)
img_svclinear_report = Image.open(fp=report_svclinear_path)
img_svcpoly_report = Image.open(fp=report_svcpoly_path)
img_svcrbf_report = Image.open(fp=report_svcrbf_path)







args = Namespace(
    target_variable = 'state',
    target_variable_transformed = 'state_category',
    predictor_variables = ['average_answer_time_in_hours', 'progress_percent', 'test_variable_transform'],
    numeric_features = ['progress_percent', 'average_answer_time_in_min', 'extra_time_min',
                        ],
    categorical_features = ['work_rate'],
    binary_feature = ['test_variable_transform'],
    predictors = ['progress_percent', 'average_answer_time_in_min', 'extra_time_min',
                  'work_rate', 'test_variable_transform'],
    selected_predictors = ['progress_percent', 'extra_time_min', 'work_rate',
                        ],
    selected_numeric_features = ['progress_percent', 'extra_time_min'],
    not_passed = ['waiting_for_review', 'almost_there', 
                  'not_yet', 'a_little_more'],
    model_store_path = 'model_store/model.model',
    best_model_store_path = 'model_store/best_model.model',
    img_decision_tree_roc = img_decision_tree_roc,
    img_extra_decision_roc = img_extra_decision_roc,
    img_randomforest_roc = img_randomforest_roc,
    img_logistic_roc = img_logistic_roc,
    img_svclinear_roc = img_svclinear_roc,
    img_svcpoly_roc = img_svcpoly_roc,
    img_svcrbf_roc = img_svcrbf_roc,
    img_acc_score = img_acc_score,
    img_fittime = img_fittime,
    img_scoretime = img_scoretime,
    img_decision_tree_report = img_decision_tree_report,
    img_extra_decison_report = img_extra_decison_report,
    img_logistic_report = img_logistic_report,
    img_randomforest_report = img_randomforest_report,
    img_svclinear_report = img_svclinear_report,
    img_svcpoly_report = img_svcpoly_report,
    img_svcrbf_report = img_svcrbf_report
    
)













