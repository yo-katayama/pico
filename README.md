# RaspberryPi Pico API snippet

RaspberryPi PicoをAPIサーバー化したり、各種モジュールを断片保存するリポジトリ

# DEMO

HTTPリクエストを行うことで、Picoから気温を取得する。

# Requirement

基本的に事前インストールは不要で、モジュールをダウンロードして配置することで使用できる。

# Installation

Requirementで列挙したライブラリなどのインストール方法を説明する

```bash
pip install huga_package
```

# Usage

サーボモータを動かすコマンド例

```bash
curl -X POST -H "Content-Type: application/json" -d '{"angle": 20}' http://172.20.10.6/servo
```

# Note

注意点などがあれば書く

# Author

* 作成者
* 所属
* E-mail

# License
ライセンスを明示する

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).

社内向けなら社外秘であることを明示してる

"hoge" is Confidential.
