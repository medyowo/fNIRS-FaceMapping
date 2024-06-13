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
```
measurements\to_clean\{CONTROL SUBJECT NAME}\[_temoin{number}|experience{number}]\DATA:
```

We collected data from Shimadzu LIGHTNIRS and named them as following :
> Control Experiments \
_temoin1 : Resting, Closed Eyes, Head still, No chewing gum \
_temoin2 (UNUSED) : Resting, Closed Eyes, Head still, Chewing gum \
_temoin3 : Resting, Opened Eyes, Head still, No chewing gum \
_temoin4 (UNUSED) : Resting, Opened Eyes, Head still, Chewing gum

> Test Experiments \
experience5 : 


## Requirements

