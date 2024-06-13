import pandas as pd
import pathlib


def txt2csv() -> None:
    """

    Reads fNIRS text data and converts it to a CSV table
    fNIRSのテキストデータを読み取り、CSVテーブルに変換します

    """
    # temoin = 対照
    # expérience = 実験
    fname_options = {
        'names': ['oceane', 'tristan'],
        'exp_type': ['temoin', 'experience']
    }

    for name in fname_options['names']:

        cleaned_folder = pathlib.Path(f"measurements/cleaned/{name.upper()}/")
        to_clean_folder = pathlib.Path(f"measurements/to_clean/{name.upper()}/")

        # Create cleaned directory is it doesn't exist
        # クリーンなディレクトリが存在しない場合は作成します
        if not cleaned_folder.is_dir():
            if not pathlib.Path(f"measurements/cleaned/").is_dir : pathlib.Path(f"measurements/cleaned/").mkdir()
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
    txt2csv()
