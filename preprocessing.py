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
    cleaned_folder = []
    subfolders = []

    for name in fname_options['names']:
        # Create cleaned directory
        cleaned_folder = pathlib.Path(f"measurements/cleaned/{name.upper()}/")
        to_clean_folder = pathlib.Path(f"measurements/to_clean/{name.upper()}/")

        if not cleaned_folder.is_dir():
            cleaned_folder.mkdir()

        for i, subfolder in enumerate(to_clean_folder.iterdir()):
            print(f"{'-' * 50}\nCLEANING SUBFOLDER : " + str(subfolder).split("\\")[-1] + f"\n{'-' * 50}")
            for exp in fname_options['exp_type']:
                if exp in str(subfolder):
                    for file in subfolder.glob('*.TXT'):
                        try :
                            fname = str(file)
                            print(f"[CLEANING FILE : " + fname.split("\\")[-1] + "]")
                            df = pd.read_csv(
                                fname,
                                sep="\t",
                                skiprows=33)
                            print("successfully opened file")

                            # If the folder for cleaned data doesn't exist, create it
                            # クリーンデータのフォルダが存在しない場合、作成します
                            current_cleaned_folder = pathlib.Path(f"{str(cleaned_folder)}\\" + fname.split('\\')[-2] + "\\")
                            if not current_cleaned_folder.is_dir():
                                current_cleaned_folder.mkdir()
                                print(f"CREATED FOLDER : {str(cleaned_folder)}\\" + fname.split('\\')[-2] + "\\")

                            df.to_csv(fname.replace(str(to_clean_folder), str(cleaned_folder)).replace("TXT","csv"))
                            print(f"Converted {fname} successfully.\n")

                        except FileNotFoundError:
                            print(f"File {fname} not found\n")
                    break
                else:
                    print("Experience type unrecognized - SKIPPING FOLDER\n")


if __name__ == '__main__':
    txt2csv()