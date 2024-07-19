# fNIRS-FaceMapping
![Used languages](https://skillicons.dev/icons?i=python,matlab)

## Description of the project
---

The fNIRS FaceMapping project uses data collected from the Shimadzu LIGHTNIRS Portable functional Near-Infrared Spectroscopy System for research.
The Shimadzu software can export data as plain text files. A simple Python program uses this plain text to convert it into a .csv file.
Data cleaning and analysis are performed with a Matlab program.

fNIRS FaceMappingプロジェクトは、研究のために収集されたShimadzu LIGHTNIRS携帯型機能的近赤外分光システムからのデータを使用します。
Shimadzuソフトウェアは、データをプレーンテキストファイルとしてエクスポートすることができます。簡単なPythonプログラムは、このプレーンテキストを使用して.csvファイルに変換します。
データのクリーンアップと分析は、Matlabプログラムで行います。

---

## About Data
### データについて

Notice that data are in folded like this : \
データがこのように折りたたまれていることに注意してください：
```measurements\to_clean\{CONTROL SUBJECT NAME}\[_temoin{number}|experience{number}]\DATA:```

We collected data from Shimadzu LIGHTNIRS and named them as following : \
Shimadzu LIGHTNIRS からデータを収集し、以下のように名前を付けました：
### Control Experiments
#### 対照実験
1. ```[NO MOVEMENTS]``` **\_temoin1 :** Resting, Closed Eyes, Head still, No chewing gum 
2. ```[JAW]``` **\_temoin2 :** Resting, Closed Eyes, Head still, Chewing gum 
3. ```[NO MOVEMENTS]``` **\_temoin3 :** Resting, Opened Eyes, Head still, No chewing gum 
4. ```[JAW]``` **\_temoin4 :** Resting, Opened Eyes, Head still, Chewing gum 

### Test Experiments
#### テスト実験
5. ```[ALL]``` **experience5**: Moving all face muscles
6. ```[EYEBROWS]``` **experience6 :** Raised Eyebrows 
7. ```[EYEBROWS]``` **experience7 :** Frowned Eyebrows 
8. ```[NOSE]``` **experience8 :** Moving Nostrils 
9. ```[NOSE]``` **experience9 :** Frowned Nose 
10. ```[MOUTH]``` **experience10 :** Smile (No teeth) 
11. ```[MOUTH]``` **experience11 :** Frown 
12. ```[MOUTH]``` **experience12 :** Opened Mouth (Surprised) 
13. ```[MOUTH]``` **experience13 :** Puckered Mouth 
14. ```[TONGUE]``` **experience14 :** Moving Tongue

For each experiment we made 5 tries for 1 minute each. \
各実験で、1分ごとに5回の試行を行いました。

## Python Requirements
### Python の要件

- pandas (2.2.2)
- pathlib (1.0.1)
- scikit-learn (1.5.1)
- keras (3.4.1)
- matplotlib (3.9.1)

> To install all requirements at once just use : ```pip install -r requirements.txt``` \
> すべての要件を一度にインストールするには、次のコマンドを使用してください：
```pip install -r requirements.txt```

## Code Usage
### コードの使用法

#### 4 main files are useful for general usage of code :
##### コードの一般的な使用に役立つ主要なファイルは4つです：

1. ```preprocessing/preprocessing.py``` : this file transform ```.TXT``` files gotten from fNIRS software and transform them into ```.csv``` file for a easier usage.
> このファイルは、fNIRSソフトウェアから取得した ```.TXT``` ファイルを変換し、使いやすい ```.csv``` ファイルに変換します。
2. ```analysis/analyzeData.m``` : this file use MATLAB program to filter collected data and amplify training data.
> このファイルは、MATLABプログラムを使用して収集したデータをフィルタリングし、トレーニングデータを増幅します。 
3. ```ai_train.py``` : this file is used to train ai alogrithm with dedicated database. We trained 4 Classifier algorithms and a Machine Learning Neural Network.
> このファイルは、専用のデータベースを使用してAIアルゴリズムを訓練するためのものです。4つの分類アルゴリズムと1つの機械学習ニューラルネットワークを訓練しました。
4. ```ai_use.py``` : if you are not planning to use your own database, just use this one. The program is used to predict data using trained models in the ```models/``` folder.
> 自分のデータベースを使用する予定がない場合は、このデータベースを使用してください。このプログラムは、```models/``` フォルダーにある訓練済みモデルを使用してデータを予測するために使用されます。

#### If you want to use the program, do as following :
1. Import your collected data in ```MEASUREMENTS/to_clean```
2. Launch ```preprocessing.py``` and type "r" (real data)
3. Launch ```analyzeData.m``` and type "real" (real data)
4. Launch ```ai_use.py``` and enter any generated model from ```models/``` folder
5. Read your results

##### プログラムを使用したい場合は、次のようにしてください：
1. 収集したデータを ```MEASUREMENTS/to_clean``` にインポートします
2. ```preprocessing.py``` を実行し、「r」（実データ）と入力します
3. ```analyzeData.m``` を実行し、「real」（実データ）と入力します
4. ```ai_use.py``` を実行し、models/ フォルダーから生成された任意のモデルを入力します
5. 結果を確認します
