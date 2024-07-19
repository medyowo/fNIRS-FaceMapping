import pickle as pk
import sys
from ai_processing import ai_2d
from ai_processing import ai_3d
from preprocessing import data_transform


def train():
    """
    
    train choosen model for facial muscle detection
    顔面筋検出のために選択されたモデルを訓練する

    """
    print(f"{'=' * 50}\nLOADING DATABASE\n{'=' * 50}")
    train_data, train_labels, test_data, test_labels = data_transform.pretreat_train_data()

    while 1:
        print(f"{'=' * 50}\nGENERATING MODELS\na : all, b : neural network (3D), c : classifier (2D), q : quit\n{'=' * 50}")
        models = input("Choose which model you want to generate\n>")

        if models.lower() == "b" or models.lower() == "a":
            print("\nGenerating neural network (3D) model...")
            nn_train(train_data, train_labels, test_data, test_labels)

        if models.lower() == "c" or models.lower() == "a":
            print("\nGenerating classifier algorithm (2D) model...")
            alg_train(train_data, train_labels, test_data, test_labels)

        elif models.lower() == "q":
            sys.exit()
        else:
            print("Unrecognized answer\n")


def alg_train(train_data, train_labels, test_data, test_labels):
    """
    
    train classifier algorithm with 2D data (no time dimension)
    時間次元なしの2Dデータで分類アルゴリズムを訓練する

    """
    all_train_data, all_train_label = ai_2d.pre_treatment(train_data, train_labels, "train")
    all_test_data, all_test_label = ai_2d.pre_treatment(test_data, test_labels, "test")

    type_classifier = input("Select a classifier :\n1) DecisionTreeClassifier\n2) KNeighborsClassifier\n3) RandomForest\n4) RBF SVM\n\n")
    trained_model, model_name = ai_2d.train_ai(all_train_data, all_train_label, all_test_data, all_test_label, type_classifier)

    select_save(trained_model, "ML_"+model_name)


def nn_train(train_data, train_labels, test_data, test_labels):
    """
    
    train neural network with 3D data (time dimension)
    時間次元を含む3Dデータでニューラルネットワークを訓練する

    """
    trained_model = ai_3d.train_ai(train_data, train_labels)
    ai_3d.test_ai(trained_model, test_data, test_labels)

    select_save(trained_model, "ML_NN")


def select_save(trained_model, name):
    """

    Select if user want to save model or not
    ユーザーがモデルを保存するかどうかを選択
    
    """
    answer = input("Save the model ? (y for yes, n for no)\n>")

    if answer == "y":
        print("\nSaving model...")
        if not save_model(trained_model, name):
            print("Model saved !\n")
        else:
            print("Error while saving model\n")

def save_model(model, name):
    """
    
    Save computed model to .sav file
    計算されたモデルを.savファイルに保存する
    
    """
    try:
        filename = name+'.sav'
        pk.dump(model, open("models/"+filename, 'wb'))
    except [FileExistsError, FileNotFoundError]:
        return 1

    return 0

if __name__ == "__main__":
    train()
