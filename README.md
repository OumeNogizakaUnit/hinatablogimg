# hinatablogimg

日向陽

# 必要なもの

* pip コマンド

# 準備

`hinatablogimg` は `pip` コマンド用いてインストールが可能です。

```
pip install git+https://github.com/funnelyuuta/hinatablogimg
```

# 実行

```
hinatablogimg ./savedir
```

# 使い方

```
Usage: hinatablogimg [OPTIONS] SAVEDIR

  Argument:

      SAVEDIR             探索画像保存先パス

Options:
  --startpage INTEGER RANGE       探索開始ページ  [default: 0]
  --endpage INTEGER RANGE         探索終了ページ  [default: 3]
  --logpath PATH                  ログファイル出力先パス  [default:
                                  ./log/hinatablogimg.log]

  --loglevel [DEBUG|INFO|WARNING|ERROR|CRITICAL]
                                  ログレベル  [default: INFO]
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
