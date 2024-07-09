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
> Control Experiments \
```[CONTROL]``` **\_temoin1 :** Resting, Closed Eyes, Head still, No chewing gum \
```[CONTROL]``` **\_temoin2 :** Resting, Closed Eyes, Head still, Chewing gum  _(UNUSED)_ \
```[CONTROL]``` **\_temoin3 :** Resting, Opened Eyes, Head still, No chewing gum \
```[CONTROL]``` **\_temoin4 :** Resting, Opened Eyes, Head still, Chewing gum _(UNUSED)_

> Test Experiments \
```[ALL]``` **experience5**: Moving all face muscles _(UNUSED)_\
```[EYEBROWS]``` **experience6 :** Raised Eyebrows \
```[EYEBROWS]``` **experience7 :** Frowned Eyebrows \
```[NOSE]``` **experience8 :** Moving Nostrils \
```[NOSE]``` **experience9 :** Frowned Nose \
```[MOUTH]``` **experience10 :** Smile (No teeth) \
```[MOUTH]``` **experience11 :** Frown \
```[MOUTH]``` **experience12 :** Opened Mouth (Surprised) \
```[MOUTH]``` **experience13 :** Puckered Mouth \
```[TONGUE]``` **experience14 :** Moving Tongue

For each experiment we made 5 tries for 1 minute each.

## Python Requirements

- pandas (2.2.2)
- pathlib (1.0.1)
- scikit-learn (1.5.1)

> To install all requirements at once just use :
```pip install -r requirements.txt```

