import pandas as pd
import pathlib


def transform_measurements():
    """
    
    Chooses the dataset to transform to CSV table
    CSVテーブルに変換するデータセットを選択
    
    """
    print(f"{'=' * 50}\nCONVERT MEASUREMENTS TO CSV\nt : training dataset, r : real dataset\n{'=' * 50}")
    answer = input("Choose used dataset\n>")

    if answer == "t":
        txt2csv_train()
    elif answer == "r":
        txt2csv_real()
    else:
        print("Unrecognized answer")

def txt2csv_real() -> None:
    """

    Reads fNIRS text data and converts it to a CSV table (real data)
    fNIRSのテキストデータを読み取り、CSVテーブルに変換します (実データ)

    """
    cleaned_folder = pathlib.Path("MEASUREMENTS/cleaned/")
    to_clean_folder = pathlib.Path("MEASUREMENTS/to_clean/")

    # Create cleaned directory is it doesn't exist
    # クリーンなディレクトリが存在しない場合は作成します
    if not cleaned_folder.is_dir():
        cleaned_folder.mkdir()

    for file in to_clean_folder.glob('*.TXT'):
        fname = str(file)
        print("[CLEANING FILE :" + fname.rsplit('\\', maxsplit=1)[-1] + "]")

        try:
            df = pd.read_csv(
                fname,
                sep="\t",
                skiprows=33)
            print("successfully opened file")

            # Convert data to CSV file
            # データをCSVファイルに変換
            df.to_csv(fname.replace(str(to_clean_folder), str(cleaned_folder)).replace("TXT","csv"))
            print(f"Converted {fname} successfully.\n")

        except FileNotFoundError:
            print(f"File {fname} not found\n")

def txt2csv_train() -> None:
    """

    Reads fNIRS text data and converts it to a CSV table (train)
    fNIRSのテキストデータを読み取り、CSVテーブルに変換します (訓練)

    """
    # temoin = 対照
    # expérience = 実験
    fname_options = {
        'names': ['oceane', 'tristan'],
        'exp_type': ['temoin', 'experience']
    }

    for name in fname_options['names']:

        cleaned_folder = pathlib.Path(f"train_measurements/cleaned/{name.upper()}/")
        to_clean_folder = pathlib.Path(f"train_measurements/to_clean/{name.upper()}/")

        # Create cleaned directory is it doesn't exist
        # クリーンなディレクトリが存在しない場合は作成します
        if not cleaned_folder.is_dir():
            if not pathlib.Path(f"train_measurements/cleaned").is_dir():
                pathlib.Path(f"train_measurements/cleaned").mkdir()
            cleaned_folder.mkdir()

        # Check each subfolder of the data directory to get data
        # データディレクトリの各サブフォルダーを確認してデータを取得します
        for subfolder in to_clean_folder.iterdir():
            print(f"{'-' * 50}\nCLEANING SUBFOLDER : " + str(subfolder).split("\\")[-1] + f"\n{'-' * 50}")

            # Get if experience type is correctly categorized
            # エクスペリエンス タイプが正しく分類されているかどうかを取得する
            for exp in fname_options['exp_type']:
                if exp in str(subfolder):

                    # Get all data files from a subfolder
                    # サブフォルダーからすべてのデータ ファイルを取得します
                    for file in subfolder.glob('*.TXT'):
                        fname = str(file)
                        print(f"[CLEANING FILE : " + fname.split("\\")[-1] + "]")

                        try:
                            df = pd.read_csv(
                                fname,
                                sep="\t",
                                skiprows=33)
                            print("successfully opened file")

                            # If the subfolder for cleaned data doesn't exist, create it
                            # クリーンデータのフォルダが存在しない場合、作成します
                            current_cleaned_folder = pathlib.Path(f"{str(cleaned_folder)}\\" + fname.split('\\')[-2] + "\\")
                            if not current_cleaned_folder.is_dir():
                                current_cleaned_folder.mkdir()
                                print(f"CREATED FOLDER : {str(cleaned_folder)}\\" + fname.split('\\')[-2] + "\\")

                            # Convert data to CSV file
                            # データをCSVファイルに変換
                            df.to_csv(fname.replace(str(to_clean_folder), str(cleaned_folder)).replace("TXT","csv"))
                            print(f"Converted {fname} successfully.\n")

                        except FileNotFoundError:
                            print(f"File {fname} not found\n")
                    break
                else:
                    print("Experience type unrecognized - SKIPPING FOLDER\n")


if __name__ == '__main__':
    transform_measurements()
