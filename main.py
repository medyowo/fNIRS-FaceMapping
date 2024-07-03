import pandas as pd
import pathlib
import random
from sklearn.preprocessing import MinMaxScaler

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
    クリーンアップされたデータセットをトレインデータセットとテストデータセットに分割する（7:3の比率）

    """
    # temoin = 対照
    # expérience = 実験
    fname_options = {
        'names': ['oceane', 'tristan'],
        'exp_type': ['temoin', 'experience']
    }

    base_path = pathlib.Path('measurements/cleaned')
    train_data = []
    test_data = []

    for name in fname_options['names']:
        # print(f"{name.upper()} SELECTED")

        for exp in fname_options['exp_type']:
            for i in range(1,15):
                if i<=4 :
                    prefix = "_"+exp
                else :
                    prefix = fname_options['exp_type'][1]

                
                folder_name = f"{prefix}{i}"
                #print(f"FOLDER NAME : {folder_name}")
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
                        remaining_files = set(files) - set(selected_files)
                        # print(f"REMAINING FILES : {remaining_files}")
                        test_data.append(remaining_files)

    # print(f"TRAIN DATA : {train_data}")
    # print(f"TEST DATA : {test_data}")
    return train_data, test_data

def data_transform(file) -> list:
    """

    Normalize the data for easier data exploitation
    データを正規化してデータの活用を容易にする
    
    """
    # Normalisation (Scaling Normalisation): modifies dataset to fit on a scale between [0;1]
    scaler = MinMaxScaler()
    scaler = scaler.fit_transform(file)
    print(f"DATA NORMALISED : {scaler}")

train_data, test_data = sep_train_data()

# Read train data
for file in train_data:
    for i in range(len(file)):

        # Open CSV file from train data
        df = pd.read_csv(pathlib.Path(file[i]))
        print(f"FILE READ : {pathlib.Path(file[i])}")

        # Drop irrelevant data
        df = df.iloc[2:]
        df.drop(df.columns[0], axis=1)

        print(f"HEAD : {df.head()}")
        data_transform(df)