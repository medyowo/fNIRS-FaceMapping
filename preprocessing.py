import pandas as pd
import pathlib

def txt2csv() -> None:
    """

    Reads fNIRS text data and converts it to a CSV table
    fNIRSのテキストデータを読み取り、CSVテーブルに変換します

    """
    # témoin = 対照
    # expérience = 実験
    fname_options = {
        'names' : ['oceane', 'tristan'],
        'exp_type' : ['temoin', 'experience']
    }

    for name in fname_options['names']:
        for i in range(1,15):
            if i <= 4:
                exp_type = fname_options['exp_type'][0]
            else :
                exp_type = fname_options['exp_type'][1]

            print(f"{name}_{exp_type}{i}")

            # Typical folder name example : tristan_temoin2
            # 典型的なフォルダ名の例: tristan_temoin2
            folder = pathlib.Path(f"measurements/{name}_{exp_type}{i}/")
            cleaned_folder = pathlib.Path(f"measurements/cleaned/{name}_{exp_type}{i}/")

            for file in folder.glob('*.TXT'):
                try :
                    fname = str(file)
                    print(f"fname = {fname}")
                    df = pd.read_csv(
                        fname,
                        sep="\t",
                        skiprows=33)
                    print("successfully opened file")

                    # If the folder for cleaned data doesn't exist, create it
                    # クリーンデータのフォルダが存在しない場合、作成します
                    if not cleaned_folder.is_dir():
                        cleaned_folder.mkdir()

                    df.to_csv(fname.replace("measurements","measurements/cleaned").replace("TXT","csv"))
                    print(f"Converted {fname} successfully.")

                except FileNotFoundError:
                    print(f"File {fname} not found")

txt2csv()