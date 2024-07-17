import pandas as pd
import numpy as np
import pathlib
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_score
from sklearn import tree
from ai_processing import ai_2d
from ai_processing import ai_3d

# The prints in the comments allow debugging in case of problems
# コメント内のプリントは問題が発生した場合のデバッグに役立ちます

def select_rd_file(files, percentage) -> list:
    """
    
    Selects X percentage of random files
    ランダムにXパーセントのファイルを選択する
    
    """
    sample_size = int(len(files) * percentage)
    selected_files = random.sample(files, sample_size)
    # print(f"SELECTED FILES TYPE: {type(selected_files)}")
    return selected_files

def sep_train_data() -> list:
    """

    Separate the cleaned dataset into train and test datasets (7:3 ratio)
    Associate data with their respective label
    クリーンアップされたデータセットをトレインデータセットとテストデータセットに分割する（7:3の比率）

    """
    # temoin = 対照
    # expérience = 実験
    fname_options = {
        'names': ['oceane', 'tristan'],
        'exp_type': ['temoin', 'experience']
    }

    base_path = pathlib.Path('measurements/filtered')
    # base_path = pathlib.Path('measurements/cleaned')

    train_data = []
    test_data = []
    for name in fname_options['names']:
        # print(f"{name.upper()} SELECTED")
        for i in range(1,15):
            if i<=4 :
                prefix = "_"+fname_options['exp_type'][0]
            else :
                prefix = fname_options['exp_type'][1]

            folder_name = f"{prefix}{i}"

            #print(f"FOLDER NAME : {folder_name}")
            subfolder = base_path / name.upper() / folder_name
            # print(f"SUBFOLDER : {subfolder}")

            if subfolder.is_dir():
                print(folder_name)
                # print("SUBFOLDER IS DIR")

                # Find every file in the folder
                # フォルダ内のすべてのファイルを見つける
                files = list(subfolder.glob('*'))
                # print(f"FILES : {files}")

                if files:

                    # Randomly select 70% of measurements
                    # 測定値の70%をランダムに選択する
                    selected_files = select_rd_file(files, 0.7)
                    # print(f"SELECTED FILES : {selected_files}")
                    train_data.append(selected_files)

                    # The remaining 30% are added to test_data
                    # 残りの30%はテストデータに追加される
                    remaining_files = list(set(files) - set(selected_files))
                    # print(f"REMAINING FILES : {remaining_files}")
                    test_data.append(remaining_files)
                        
    
    print(f"TRAIN DATA : {train_data}")
    counter = 0
    for train_file in train_data:
      print(train_file[0]," : ",len(train_file))
      counter += len(train_file)

    print("Counter : ", counter)

    print(f"TEST DATA : {test_data}")
    return train_data, test_data

def label_data(train_data, test_data) -> dict:
    """
    
    Label each file
    
    """
    # Create label options list
    label_temp = [('no_movement', 2), ('jaw', 2),('face', 1), ('eyebrows', 2), ('nose', 2), ('mouth', 4), ('tongue', 1)]
    label_options = [element for element, count in label_temp for _ in range(count)]
    # print(f"LABEL OPTIONS : {label_options}")

    # Label each file
    train_set = {}
    test_set = {}

    for i in range(len(label_options)):
        try:
            train_set[label_options[i]] += train_data[i]
            test_set[label_options[i]] += test_data[i]
            train_set[label_options[i]] += train_data[i+14]
            test_set[label_options[i]] += test_data[i+14]
        except KeyError:
            train_set[label_options[i]] = train_data[i]
            test_set[label_options[i]] = test_data[i]
            train_set[label_options[i]] += train_data[i + 14]
            test_set[label_options[i]] += test_data[i + 14]

    # print(f"TRAIN SET : {train_set}")
    # print(f"TEST SET : {test_set}")
    return train_set,test_set

def normalise(file) -> list:
    """

    Normalize the data for easier data exploitation
    データを正規化してデータの活用を容易にする
    
    """

    # Normalisation (Scaling Normalisation): modifies dataset to fit on a scale between [0;1]
    scaler = MinMaxScaler()
    scaler = scaler.fit_transform(file)
    # print(f"DATA NORMALISED : {scaler}")
    return scaler

def label_list(dataset) -> list:
    """

    Separates the labels of the dataset into a different list
    
    """
    label_lst = []
    
    # Iterate over the items in the dataset
    for label, data_list in dataset.items():

        # Append the label for each item in the data list
        label_lst.extend([label] * len(data_list))
        
    return label_lst

# def learn_data(train_data, train_label):
#     """
#
#     Use of the Stochastic Gradient Descent (SGD) Classifier to learn the train dataset
#
#     """
#     classifier = tree.DecisionTreeClassifier()
#     print("PREDICTING...")
#     classifier.fit(train_data, train_label)
#     # print(f"PREDICT : {classifier.predict(train_data)[0]}")
#     # print(f"Scores de décision : {classifier.decision_function(train_data)[0]}\n")
#     # print(f"Position du plus haut score : {np.argmax(classifier.decision_function(train_data)[0])}")


def pretreat_data():
    tmp_train_data, tmp_test_data = sep_train_data()
    print(f"TMP TRAIN DATA : {tmp_train_data}")

    count = 0
    for tmp_train_list in tmp_train_data:
        count += len(tmp_train_list)
        print(tmp_train_list[0], len(tmp_train_list))

    print("TOTAL COUNT TMP TRAIN : ", count)

    train_set, test_set = label_data(tmp_train_data, tmp_test_data)

    # Create separate corresponding labels
    train_label = label_list(train_set)
    test_label = label_list(test_set)
    print(f"TRAIN LABEL : {train_label}")

    # Create separate corresponding data
    train_list_data = list(train_set.values())
    test_list_data = list(test_set.values())
    print(f"TRAIN DATA : {train_list_data}")

    train_data = []
    test_data = []
    # Read train data
    for file in train_list_data:
        for i in range(len(file)):
            # Open CSV file from train data
            df = pd.read_csv(pathlib.Path(file[i]))

            # print(f"FILE READ : {pathlib.Path(file[i])}")

            # Drop irrelevant data
            df = df.drop(df.columns[0], axis=1)
            df = df.drop(df.columns[1:4], axis=1)
            # print(f"HEAD : {df.head(5)}")

            # Normalise
            scaler = normalise(df)
            # print(f"HEAD AFTER NORMALISATION : {df.head(5)}")
            train_data.append(df)
    
    # Read test data
    for file in test_list_data:
        for i in range(len(file)):
            # Open CSV file from train data
            df = pd.read_csv(pathlib.Path(file[i]))

            # print(f"FILE READ : {pathlib.Path(file[i])}")

            # Drop irrelevant data
            df = df.drop(df.columns[0], axis=1)
            df = df.drop(df.columns[1:4], axis=1)
            # print(f"HEAD : {df.head(5)}")

            # Normalise
            scaler = normalise(df)
            # print(f"HEAD AFTER NORMALISATION : {df.head(5)}")
            test_data.append(df)

    print(f"TRAIN DATA ==============\n {train_data[0]}")

    all_train_data, all_train_label = ai_2d.pre_treatment(train_data, train_label, "train")
    all_test_data, all_test_label = ai_2d.pre_treatment(test_data, test_label, "test")

    type_classifier = input("Select a classifier :\n1) DecisionTreeClassifier\n2) KNeighborsClassifier\n3) RandomForest\n4) RBF SVM\n5) Gaussian Process\n\n")
    ai_2d.train_ai(all_train_data, all_train_label, all_test_data, all_test_label, type_classifier)


if __name__ == '__main__':
    pretreat_data()


