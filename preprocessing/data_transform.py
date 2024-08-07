import pathlib
import random
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


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


def sep_train_data() -> tuple[list, list]:
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

    base_path = pathlib.Path('train_measurements/filtered')

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

            # print(f"FOLDER NAME : {folder_name}")
            subfolder = base_path / name.upper() / folder_name
            # print(f"SUBFOLDER : {subfolder}")

            if subfolder.is_dir():
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

    return train_data, test_data


def label_data(train_data, test_data) -> dict:
    """
    
    Label each file
    各ファイルにラベルを付ける
    
    """
    # Create label options list
    # ラベルオプションリストを作成する
    label_temp = [('no_movement', 2), ('jaw', 2),('face', 1), ('eyebrows', 2), ('nose', 2), ('mouth', 4), ('tongue', 1)]
    label_options = [element for element, count in label_temp for _ in range(count)]
    # print(f"LABEL OPTIONS : {label_options}")

    # Label each file
    # 各ファイルにラベルを付ける
    train_set = {}
    test_set = {}

    for i, val in enumerate(label_options):
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
    # 正規化（スケーリング正規化）：データセットを[0;1]の範囲に収まるように変更する
    scaler = MinMaxScaler()
    scaler = scaler.fit_transform(file)
    return scaler

def label_list(dataset) -> list:
    """

    Separates the labels of the dataset into a different list
    データセットのラベルを別のリストに分ける
    
    """
    label_lst = []
    
    # Iterate over the items in the dataset
    # データセット内のアイテムを繰り返し処理する
    for label, data_list in dataset.items():

        # Append the label for each item in the data list
        # データリストの各アイテムにラベルを追加する
        label_lst.extend([label] * len(data_list))
        
    return label_lst


def labels_to_num(labels):
    """
    
    Get label and encode them into numerical values
    ラベルを取得して数値にエンコードする
    
    """
    label_encoder = LabelEncoder()
    return label_encoder.fit_transform(labels)

def modify_data(data_list):
    """

    Modify data to remove unused columns and normalize values
    データを修正して未使用の列を削除し、値を正規化する

    """
    normalized_data = []
    for file in data_list:
        for i, val in enumerate(file):
            # Open CSV file 
            # CSVファイルを開く
            df = pd.read_csv(pathlib.Path(val))

            # Drop irrelevant data
            # 無関係なデータを削除する
            df = df.drop(df.columns[0], axis=1)
            df = df.drop(df.columns[1:4], axis=1)

            # Normalize values
            # 値を正規化する
            scaler = normalise(df)
            normalized_data.append(df)
    
    return normalized_data


def pretreat_train_data():
    """
    
    Pre-treatment function on training database
    トレーニングデータベースに対する前処理機能
    
    """
    tmp_train_data, tmp_test_data = sep_train_data()
    train_set, test_set = label_data(tmp_train_data, tmp_test_data)

    # Create separate corresponding labels
    # 対応するラベルを別々に作成する
    train_label = label_list(train_set)
    test_label = label_list(test_set)

    # Encode labels to numeric values
    # ラベルを数値にエンコードする
    train_labels = labels_to_num(train_label)
    test_labels = labels_to_num(test_label)
    print(f"TRAIN LABEL : {train_labels}")

    # Create separate corresponding data
    # 対応するデータを別々に作成する
    train_list_data = list(train_set.values())
    test_list_data = list(test_set.values())

    train_data = modify_data(train_list_data)
    test_data = modify_data(test_list_data)

    print(f"NUMBER OF TRAIN SAMPLES : {len(train_data)}")
    print(f"NUMBER OF TEST SAMPLES : {len(test_data)}\n")
  
    return train_data, train_labels, test_data, test_labels


def pretreat_real_data():
    """
    
    Pre-treatment function on real data
    実データに対する前処理機能
    
    """
    data_list = list(pathlib.Path('MEASUREMENTS/filtered').glob('*'))
    normalized_data = modify_data([data_list])

    print(f"NUMBER OF SAMPLES : {len(normalized_data)}\n")
    return normalized_data, len(normalized_data), data_list


if __name__ == '__main__':
    pretreat_train_data()


