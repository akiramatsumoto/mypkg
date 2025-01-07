# mypkg
[![test](https://github.com/akiramatsumoto/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/akiramatsumoto/mypkg/actions/workflows/test.yml)  
ロボットシステム学の講義で提出するためのROS 2のパッケージです.  
パソコンの電池残量をトピック```/batterylevel```から出します.
## ノード
### battery_monitor
パソコンの電池残量を調べ, 2秒ごとに送信します.
#### 送信先トピック
- batterylevel
## 注意点
- [resource/mypkg](https://github.com/akiramatsumoto/mypkg/blob/kanashi/resource/mypkg)には何も記述されていませんが, [setup.py](https://github.com/akiramatsumoto/mypkg/blob/kanashi/setup.py)によるビルド時に必要なため削除しないでください.

## ROSバージョン
- ROS 2 Humble Hawksbill（ローカル環境, およびGitHub Actionsの両方で使用）
## ライセンス
- このパッケージは3条項BSDライセンスの下, 再頒布および使用が許可されます.
- © 2024 Akira Matsumoto
