#pysatcatcher
[![Build Status](https://travis-ci.org/HAYASAKA-Ryosuke/pysatcatcher.png?branch=master)](https://travis-ci.org/HAYASAKA-Ryosuke/pysatcatcher)
#はじめに
これはアマチュア衛星追尾のために作ったpython製の地上局運用ソフトです。
機能は軌道計算した結果に合わせてアマチュア無線機とアンテナ制御コントローラへのコマンド送信となります。
現在のコードではアマチュア無線機はIC910、アンテナ制御コントローラはRAC825を想定して作成しております。

#必要なライブラリ

軌道計算にはPyEphemを使用し、制御機器にはPySerialを使用してます。

"""
pip install pyephem pyserial
"""

GUI部分はkivyを使用しております。

http://kivy.org/#home

#起動と操作

"""
python main.py
"""

とタイプすることでアプリケーションが起動します。

追尾対象となるTLEと周波数、変調方式を選択してoperateボタンをクリックするだけです。

#ライセンス

MITライセンスです。

LICENSEファイルに従ってください。
