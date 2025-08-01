
[English](README.md) | [日本語](README-jp.md) | [العربية](README-ar.md) | [Português](README-pt.md) | [Español](README-es.md)

# Facebook クローラー 使用手順

## 1. 依存ライブラリのインストール

```bash
pip install -r requirements.txt
````

## 2. `facebook.exe` の設定

### アカウントのパスワードを入力

コード内の指定箇所にFacebookアカウントのユーザー名とパスワードを入力してください。

```python
# 例（引用符内を置き換えてください）
username = "your_username"
password = "your_password"
```

### グループリンクの置き換え

クロールしたいターゲットグループのリンクに、コード内のリンクを置き換えてください。

```python
# 例（実際のグループリンクに置き換えてください）
group_url = " https://www.facebook.com/groups/your_target_group "
```

### クロール数の設定（任意）

クロールするデータの量を制限したい場合は、以下の2つの数値を変更してください。

```python
# 例（必要な数値に修正してください）
while len(data) < 98:
```

```python
# 例（必要な数値に修正してください）
if len(data) >= 98:
```

## 3. 手動操作が必要な場合の対応

### ポップアップウィンドウが表示された場合

以下のようなポップアップが表示されたら、手動で閉じてください。
[![1.png](https://i.postimg.cc/Gt1LCdJn/1.png)](https://postimg.cc/2b2RdpK0)
[![2.png](https://i.postimg.cc/9FbW63Ds/2.png)](https://postimg.cc/F7f5SBgx)

### ページのリフレッシュ

ページが正しく読み込まれない場合は、手動でリフレッシュしてください。
[![3.png](https://i.postimg.cc/CKBSnzcV/3.png)](https://postimg.cc/v1sppHRP)

### 画像認証コードの処理

画像認証コードが表示された場合は、画面の指示に従って入力してください。入力後、プログラムは終了せずに継続して動作します。

## 4. クロール完了の通知

以下の出力が表示されたらクロールが完了しています。

```python
"Data saved to .......csv"
```



需要我继续给你阿拉伯语、葡萄牙语、西班牙语版本吗？
```
