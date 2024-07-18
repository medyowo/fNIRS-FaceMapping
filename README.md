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

Notice that data are in folded like this : 
```measurements\to_clean\{CONTROL SUBJECT NAME}\[_temoin{number}|experience{number}]\DATA:```

We collected data from Shimadzu LIGHTNIRS and named them as following :
### Control Experiments
1. ```[CONTROL]``` **\_temoin1 :** Resting, Closed Eyes, Head still, No chewing gum 
2. ```[CONTROL]``` **\_temoin2 :** Resting, Closed Eyes, Head still, Chewing gum  _(UNUSED)_ 
3. ```[CONTROL]``` **\_temoin3 :** Resting, Opened Eyes, Head still, No chewing gum 
4. ```[CONTROL]``` **\_temoin4 :** Resting, Opened Eyes, Head still, Chewing gum _(UNUSED)_

### Test Experiments
5. ```[ALL]``` **experience5**: Moving all face muscles _(UNUSED)_
6. ```[EYEBROWS]``` **experience6 :** Raised Eyebrows 
7. ```[EYEBROWS]``` **experience7 :** Frowned Eyebrows 
8. ```[NOSE]``` **experience8 :** Moving Nostrils 
9. ```[NOSE]``` **experience9 :** Frowned Nose 
10. ```[MOUTH]``` **experience10 :** Smile (No teeth) 
11. ```[MOUTH]``` **experience11 :** Frown 
12. ```[MOUTH]``` **experience12 :** Opened Mouth (Surprised) 
13. ```[MOUTH]``` **experience13 :** Puckered Mouth 
14. ```[TONGUE]``` **experience14 :** Moving Tongue

For each experiment we made 5 tries for 1 minute each.

## Python Requirements

- pandas (2.2.2)
- pathlib (1.0.1)
- scikit-learn (1.5.1)
- keras (3.4.1)
- matplotlib (3.9.1)

> To install all requirements at once just use :
```pip install -r requirements.txt```

## Code Usage

#### 4 main files are useful for general usage of code :

1. ```preprocessing/preprocessing.py``` : this file transform ```.TXT``` files gotten from fNIRS software and transform them into ```.csv``` file for a easier usage.
2. ```analysis/analyzeData.m``` : this file use MATLAB program to filter collected data and amplify training data. 
3. ```ai_train.py``` : this file is used to train ai alogrithm with dedicated database. We trained 4 Classifier algorithms and a Machine Learning Neural Network.
4. ```ai_use.py``` : if you are not planning to use your own database, just use this one. The program is used to predict data using trained models in the ```models/``` folder.

#### If you want to use the program, do as following :
1. Import your collected data in ```MEASUREMENTS/to_clean```
2. Launch ```preprocessing.py``` and type "r" (real data)
3. Launch ```analyzeData.m``` and type "real" (real data)
4. Launch ```ai_use.py``` and enter any generated model from ```models/``` folder
5. Read your results
