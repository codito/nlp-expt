import pandas as pd
from sklearn.metrics import label_ranking_average_precision_score

y_true = [[1, 1, 0]]
y_score = [[0, 0.9, 0]]

__import__('ipdb').set_trace()
label_ranking_average_precision_score(y_true, y_score)
