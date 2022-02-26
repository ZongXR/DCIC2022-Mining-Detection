import matplotlib.pyplot as plt
import pandas as pd
import time
from datetime import datetime
from tqdm import tqdm
from time import strftime, localtime
from scipy import stats
from scipy.spatial import distance
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.utils.class_weight import compute_class_weight
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import GridSearchCV
from lightgbm import LGBMClassifier
from joblib import dump, load
from tensorflow.keras.backend import epsilon
from itertools import combinations
from imblearn.over_sampling import SMOTE, ADASYN
from tsfresh import extract_relevant_features