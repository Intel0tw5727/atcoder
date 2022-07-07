# atcoder

## 概要
自分が問いた問題管理用

## 利用ライブラリ

- atcoder-cli
    - ターミナルで問題やサンプル取得用
- online-judge-tools
    - atcoder-cliと連携してサンプル取得や提出を行うやつ

## 実行順番

1. コンテスト用ディレクトリを作成
    - `acc new CONTEST_NAME`
2. コードを書きテストを実施する
    - 数値処理系
        - ```pyenv local pypy3.7-c-jit-latest && pyenv rehash && oj t -d tests/ -c "pypy3 main.py"```
    - 文字列処理系
        - ```pyenv local 3.8.2 && pyenv rehash && oj t -d tests/ -c "python3 main.py"```
3. テストOKなら提出
    - 数値処理系
        -  `acc s main.py -- --guess-python-interpreter pypy -w 0 -y`
    - 文字列処理系
        -  `acc s main.py -- --guess-python-version 3 -w 0 -y`