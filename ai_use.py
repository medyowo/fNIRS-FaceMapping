import pickle as pk
from collections import Counter
from preprocessing import data_transform
from ai_processing import ai_2d


def use():
    """
    
    Usage function for AI trained models. It predicts values from data in MEASUREMENTS/filtered/
    AI訓練モデルの使用機能。MEASUREMENTS/filtered/ 内のデータから値を予測します。
    
    """
    print(f"{'=' * 50}\nLOADING DATABASE\n{'=' * 50}")
    normalized_data, nb_sample, sample_names  = data_transform.pretreat_real_data()

    print(f"{'=' * 50}\nUSE GENERATED MODELS\nenter the name ONLY\n{'=' * 50}")
    model = input(">")

    print(f"Reading {model}.sav in [models/] folder...\n")

    # Open AI model with pickle
    # ピクルでAIモデルを開く
    with open("models/" + model + ".sav", 'rb') as mdl:
        trained_model = pk.load(mdl)

    print(f"{'=' * 50}\nPREDICTED VALUES\n{'=' * 50}")
    # Each sample needs to have a different prediction
    # 各サンプルは異なる予測を持つ必要があります
    if nb_sample > 1:
        for i, sample in enumerate(normalized_data):
            if model != "ML_NN":
                sample = sample.drop(sample.columns[0], axis=1)

            prediction = trained_model.predict(sample)
            print_predict(prediction, model == "ML_NN", i+1, str(sample_names[i]).split("\\")[2])
    else:
        if model != "ML_NN":
            normalized_data = ai_2d.compile_data(normalized_data)
        prediction = trained_model.predict(normalized_data)
        print_predict(prediction, model == "ML_NN", 1, str(sample_names[0]).split("\\")[2])


def print_predict(prediction, is_nn, nb_sample, sample_name):
    """
    
    Console display function (color change in function of predicted area)
    コンソール表示機能（予測された領域に応じた色の変更）
    
    """
    # Color table for console
    # コンソール用カラーテーブル
    colors = {
        'NO MOVEMENT':'\033[91m', 
        'JAW':'\033[92m', 
        'FACE':'\033[95m', 
        'EYEBROWS':'\033[93m', 
        'NOSE':'\033[94m', 
        'MOUTH':'\033[36m', 
        'TONGUE':'\033[96m'
    }
    labels = sorted(colors)

    if not is_nn:
        occurence_count = Counter(prediction)
        print(f"SAMPLE N°{nb_sample} " + '\033[38;5;206m' + f"({sample_name})" + '\033[0m' + f" : {colors[labels[occurence_count.most_common(1)[0][0]]]}{labels[occurence_count.most_common(1)[0][0]]}" + '\033[0m')
    else:
        print(f"SAMPLE N°{nb_sample} " + '\033[38;5;206m' + f"({sample_name})" + '\033[0m' + f" : {colors[labels[prediction]]}{labels[prediction]}" + '\033[0m')


if __name__ == "__main__":
    use()
