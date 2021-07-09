# macのホームページ
* hm-ogaki@smile.co.jp
* 実装する機能
     1. ログイン、サインアップ
     1. 物件の登録(管理画面)
     1. 物件の編集(管理画面)
     1. 物件の削除(管理画面)
     1. 検索機能
     1. scanした書類のアップロード機能
     1. お気に入り(ログイン後)

## モデル
* Property　プロパティー
     1. buildingName = models.CharField(max_length=100)物件名
     1. buildingType = models.CharField(max_length=100)建物の種類（戸建て、集合住宅など）
     1. price = models.IntegerField()価格
     1. buildingAge = models.IntegerField()築年月
     1. floor = models.CharField(max_length=100)階建
     1. transportation  = models.CharField(max_length=100)交通
     1. address = models.CharField(max_length=100)所在地
     1. showerRoomAndBathRoom = models.CharField(max_length=100)バス、トイレ
     1. kitchen = models.CharField(max_length=100)キッチン
     1. Feature = models.CharField(max_length=100)設備・サービス
     1. other = models.CharField(max_length=100)その他
     1. renovation = models.CharField(max_length=100)リフォーム
     1. size = models.IntegerField()専用面積
     1. typeOfBuildingConstruction = models.CharField(max_length=100)建物構造
     1. entranceImage = models.ImageField(upload_to='images')エントランス写真
     1. exteriorImage = models.ImageField(upload_to='images')外観写真
     1. floorPlan = models.ImageField(upload_to='images')間取り図
     1. buildingDescription = models.TextField()物件詳細

* Favorite　プロパティー
     1. buildingName = models.CharField(max_length=100)物件名
     1. buildingType = models.CharField(max_length=100)建物の種類（戸建て、集合住宅など）
     1. price = models.IntegerField()価格


<!-- * Recent最近見た物件一覧
     1. 

* SearchCondition保存した検索条件
     1.  -->

## サイトマップ
* Topページ
     * ログインページ
          1. ログイン機能
          * サインアップ
               1. サインアップ
     * フィルタリングページ
          1. 市区郡の選択
          1. 価格、間取り、面積、駅からの徒歩、築年数、間取り図ありなし
          1. 該当件数の表示
          1. 検索する物件の種類変更
          1. 検索条件を保存
          * 該当リストページ
               1. 該当リストの表示
               * 詳細ページ
                    1. 詳細情報の表示
                    1. お気に入りリストに追加
                    1. 電話番号の表示
                    * メールお問い合わせフォームページ
     * お気に入りページ
          1. お気に入りリストの表示
          1. お気に入りリストの削除
          * 詳細ページ
               1. 詳細情報の表示
               1. 電話番号の表示
               * メールお問い合わせフォームページ
     <!-- * 最近見た物件ページ
          1. 最近見た物件リストの表示
          * 詳細ページ 
               1. 詳細情報の表示
               1. 電話番号の表示
               * メールお問い合わせフォームページ -->
     <!-- * 検索条件の保存ページ
          1. 検索条件のリスト表示
          * 該当リストの表示
               * 詳細ページ
                    1. 詳細情報の表示
                    1. お気に入りリストに追加
                    1. 電話番号の表示
                    * メールお問い合わせフォームページ -->

## Django開発準備
### .gitignore 
1. myvenv
1. db.sqlite3
1. .vscode
1. __pycache__
1. .DS_Store
1. media
### requirements.txt
1. Django~=3.1.7
1. django-cors-headers~=3.4.0
1. djangorestframework~=3.11.1
1. Pillow==8.1.2
### パッケージのインストール 
1. pip3 install -r requirements.txt
1. source myvenv/bin/activate


## Next.js開発準備

1. frontendディレクトリを作成
1. frontendディレクトリ内でnpx create-next-app . --use-npmを実行
1. db.sqlite3


## APIコール
1. libフォルダを作成し、必要なjsファイルを格納