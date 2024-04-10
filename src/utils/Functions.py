from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score


def get_metrics(y_true, y_pred):
    f1_score_class = f1_score(y_true, y_pred, average='None')
    dic_metrics = {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred, average='macro'),
        'Precision': precision_score(y_true, y_pred, average='macro'),
        'F1': f1_score(y_true, y_pred, average='macro'),
        'F1 Scores per Class': f1_score_class
    }
    return dic_metrics