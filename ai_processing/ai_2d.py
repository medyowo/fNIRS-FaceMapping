import pandas as pd
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import ConfusionMatrixDisplay,confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

def pre_treatment(train_data, train_label, type_data):
    """

    Pretreat data before AI learning

    """
    all_data = pd.DataFrame()
    all_label = []
    tmp = []

    # Add all data back to back
    for sample in train_data:
        # Drop time channel
        sample = sample.drop(sample.columns[0], axis=1)

        # print(f"SAMPLE : {sample.head(5)}")
        all_data = pd.concat([all_data,sample])

    for label in train_label:
        tmp = [label] * 666
        # print(f"LABEL : {tmp}")
        # all_label.append(tmp)
        all_label.extend(tmp)
    
    print(f"ALL {type_data.upper()} DATA : {len(all_data)}")
    print(f"ALL {type_data.upper()} LABEL : {len(all_label)}\n")
    return all_data, all_label

def train_ai(train_data, train_label, test_data, test_label, type_classifier):
    """

    Use of different classifiers to predict test data

    """
    type_classifier = type_classifier.upper()

    if type_classifier in ("DECISIONTREECLASSIFIER", "1"):
        model = "Decision Tree Classifier"
        classifier = tree.DecisionTreeClassifier()

    elif type_classifier in ("KNEIGHBORSCLASSIFIER", "2"):
        model = "K Neighbors Classifier"
        classifier = KNeighborsClassifier()

    elif type_classifier in ("RANDOMFOREST", "3"):
        model = "Random Forest"
        classifier = RandomForestClassifier()

    elif type_classifier in ("RBF SVM", "4"):
        model = "RBF SVM"
        classifier = SVC()

    elif type_classifier in ("GAUSSIAN PROCESS", "5"):
        model = "Gaussian Process"
        classifier = GaussianProcessClassifier()

    else:
        print("There was an issue. Please try again.")

    print("\nPREDICTING...\n")
    classifier.fit(train_data, train_label)
    # TESTING PRINTS

    # print(f"PREDICT : {classifier.predict(train_data)[0]}")
    # print(f"Decision scores : {classifier.predict_proba(train_data)[0]}\n")
    # print(f"Classes : {classifier.classes_}")
    # print(f"Highest score position : {np.argmax(classifier.predict_proba(train_data)[0])}")

    # EVALUATING MODEL
    print(f"===== Model : {model} =====")
    # Evaluating on training data without cross-validation
    train_accuracy = classifier.score(train_data, train_label)
    print(f"Accuracy on train data: {round(train_accuracy * 100, 2)} %")
    test_accuracy = classifier.score(test_data, test_label)
    print(f"Accuracy on test data: {round(test_accuracy * 100, 2)} %")
    print("===========================================")

    # CONFUSION MATRIX
    style = 'PuRd'

    conf_matrix = confusion_matrix(test_label, classifier.predict(test_data), labels=classifier.classes_,normalize='true')
    mat_conf = ConfusionMatrixDisplay(conf_matrix, display_labels=classifier.classes_)
    mat_conf.plot(cmap = style)
    mat_conf.ax_.set_title("Confusion Matrix")
    mat_conf.plot(cmap= style, values_format = ".0%")
    mat_conf.ax_.set_title("Confusion Matrix (Normalised)")
    plt.show()