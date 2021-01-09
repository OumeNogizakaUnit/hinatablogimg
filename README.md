# hinatablogimg

日向陽

# 必要なもの

* poetry コマンド
* make コマンド

# 準備

以下のコマンドを実行

```
make init
```

# 実行

```
make run
```

# Windowsで動かす

試してないから動くかはわからない

下記のコマンドたちをPowerShellで管理者で実行

## 仮想環境作成


```
python -m venv venv
.\venv\Scripts\python.exe -m pip install -U pip setuptools wheel
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe -m pip install .

```

## 実行

```
.\venv\Scripts\python.exe hinatablogimg/main.py

```
