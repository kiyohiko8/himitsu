"""
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split
"""
import os
import random

"""
##プログラム概要

- 被験者に知っているひみつ道具を入力させる
	+ 質問形式（ランダム）
	+ 入力した結果から被験者の知識リストを作成
	
- 学習済みモデルに入力
	+ 既知と推測される語をリスト化
	
- 推定結果を出力

"""



"""データの読み込み"""

#全単語データの読み込み（リスト型）
all_word_list = ["悪運ダイヤ","悪魔のパスポート","アソボウ","穴ほり機","アパートごっこの木",
			"アベコンベ","あべこべクリーム","アヤカリン","あらかじめアンテナ","あらかじめ日記",
			"アラビンのランプ","アンキパン","石ころぼうし","いたずらオモチャ化機","いつでも日記",
			"イマニ目玉","インスタントミニチュア製造カメラ","インスタント旅行カメラ","ウソ８００",
			"うそつ機","うそつきかがみ","うそ発見器","打ち上げ式豆太陽","うちでの小づち",
			"うつつまくら","ウマタケ","ウラオモテックス","ウマシマキャンデー","ウルトラミキサー",
			"ウルトラ・スペシャルマイティ・ストロングスーパーよろい","衛星テレビ","エコー衛星",
			"E・S・P訓練ボックス","エスパーぼうし","XYZ線カメラ","N・Sワッペン","エラ・チューブ",
			"エースキャップ","お医者さんカバン","おざしきゲレンデ","おしかけ電話","おせじ口べに・悪口べに",
			"おそだアメ","オトコンナ","おねしょじゃ口","おはなしバッジ","おもちゃの兵隊","音楽イモ",
			"オールマイティーバス","快足シューズ","怪談ランプ","海底バイキングセット","カクミサイル発射衛星",
			"かくれマント","かげきりばさみ","かげとりもち","かぜうつし機","家族合わせケース","カッコータマゴ",
			"かならずあたる手相セット","かならず実現する予定メモ帳","カネバチ","ガリバートンネル","記憶映写とんかち",
			"きこりの泉","気象衛星","ギシンアンキ","きせかえカメラ","キューピッドのや","驚時機（きょうじき）",
			"強力岩トカシ","クイックとスロー","空気ピストル","空気砲","くすぐりノミ","くせなおしガス",
			"組み立て円盤セット","雲がためガス","暗くなる電球","グルメテーブルかけ","くろうみそ",
			"月光とう","けむりのロボット","ゲラゲライヤホン","こいのぼりそうじゅうき","声のキャンデー",
			"ごきげんメーター","ここほれワイヤー","小人ばこ","コベアベ","ゴルゴンの道","ころばし屋",
			"コンク・フード","コンピューターペンシル","さいなん報知器","細胞縮小き","３０分できく毛はえぐすり",
			"自家用衛星","時間カメラ","ジキルハイド","実景プラネタリウム","室内旅行機","シナリオライター",
			"シネラマン","シャーロック・ホームズ・セット","重力ペンキ","しゅみの日曜農業セット",
			"瞬間移動潜水艦","正直太郎","深海クリーム","深海ヘッドランプ","進化退化放射線源",
			"人生やりなおし機","ジーンマイク","水圧銃","推理ぼう","スケジュールどけい","スケスケ望遠鏡",
			"スナオン","ズバリパイプ","スパイセット","スペアポケット","スモールライト","刷りこみタマゴ","スリルブーメラン",
			"スロー","スーパーダンのふろしき","スーパー手ぶくろ","正かくグラフ","声紋キャンディー製造機","せん水艦",
			"せん風機","ソウナルじょう","そっくりクレヨン","ソノウソホント","台風のたまご","タイムカメラ",
			"タイムシーバー","タイムテレビ","タイムフロシキ","タイムマシン","ダイリガム","タケコプター",
			"だっしゅうざい","タヌ機","断層ビジョン","たんぼロール","地球セット","地球はかいばくだん",
			"地底探検車","チューブ入り雲","つけかえ手ぶくろ","つけると暗くなる電球","続きスプレー","偵察衛星",
			"手がかりレンズ","テキオー灯","手ぶくろ電話","てるてるぼーず","テレパしい","天気調整マシン",
			"電子頭脳","電車ごっこ","デンデンハウス","とうしめがね","動物がたにげだしじょう","動物変身ビスケット",
			"動物ライト","とう明人間目ぐすり","とうめいペンキ","とうめいマント","通りぬけフープ",
			"どくさいスイッチ","トゲつき寝袋","どこでも大ほう","どこでもドア","トッカエ・バー",
			"トモダチロボット","ドラえもん","取り消しゴム","とりよせバッグ","ドリームマッチ","トレーサーバッジ",
			"どんな病気にもきくくすり","ニクメナイン","二十二世紀のマジックハンド","日曜農業セット",
			"日本一周大旅行ゲーム","人間あやつり機","人間機関車セット","人間製造機","人間切断機","寝ぶくろ",
			"眠くならない薬","のろいカメラ","バイバイン","ばっ金箱","バッジ製造カメラ","ハツラツン","反のうテストロボット",
			"万能わな","ひっこし地図","日づけ変更カレンダー","ヒトマネロボット","ひょうろんロボット","ヒラリマント",
			"ピーヒョロロープ","風船いかだ","フエルミラー","フエール銀行","ふきとばし・せん風機","復元光線",
			"ブラックベルト","フルーツボート","フワフワオビ","フー子","ペコペコバッタ","ペット用魚えさ",
			"ヘッドランプ","へやこうかんスイッチ","ヘリトンボ","返事先どりポスト",
			"ポラロイドインスタントミニチュアせいぞうカメラ","ほんもの図鑑","ほんやくコンニャク","ポータブル国会",
			"ホームズセット","マグマ探知機","マジック・セメント","マッドウォッチ","ま水ストロー","○×うらない",
			"万病薬","見えなくなる目ぐすり","見たままスコープ","ミチビキエンゼル","虫の声の素","ムユウボウ",
			"ムリヤリトレパン","ムードもりあげ楽団","女神ロボット","目鼻ペン","めんくいカメラ","もぐら手ぶくろ",
			"もしもボックス","もちせいぞうマシン","もどりライト","桃太郎印のきびだんご","モモボート",
			"モンタージュバケツ","ヤカンレコーダー","友情カプセルとコントローラー","ゆうびんロケット","ゆっくり反射ぞうきん",
			"ゆめふうりん","ようろうおつまみ","四次元くずかご","四次元三輪車","四次元ポケット","予定メモ帳",
			"ラジコン宇宙人","ラッキーガン","立体映写機","流行性ネコシャクシビールス","ルームスイマー","レーダーステッキ",
			"ロケットそうじゅうくんれん機","ロボ子","Yロウ","わすれとんかち","わすれろ草"]

#辞書型に落とし込む：ベクトル表現
#word_vec;基盤となるひみつ道具辞書
word_vec = {}
for i, word in enumerate(all_word_list):

	word_vec[word] = i
	

#作成した辞書の表示	
#print(word_vec)
"""
valueからkeyを抽出する方法
for k,v in word_vec.items():
	if word_vec[k] == 0:
		print(k)

"""


"""被験者に知識情報を入力させる"""


#指定道具数ランダム抽出			
a = random.sample(all_word_list, 100)

#知識情報入力
wiselist = []
for item in a:
	print(item)
	print("これを知っていれば1, 知らなければ0を入力してください")
	data = input()
	while 0 < 1:
		if data == str(0):
			break
		elif data == str(1):
			break
		else:
			print("入力しなおしてください")
			data = input()
	if data == str(1):
		wiselist.append(item)
	
	#知っている知識が５個以上になったらループを抜け出す
	if len(wiselist) > 4:
		break

#出来上がったリストの表示		
print(wiselist)
	


"""被験者の回答から入力用データを作成"""

input_data = []
for item in wiselist:
	input_data.append(word_vec[item])

#word_vecを元に作成した入力用のデータを表示	
print(input_data)
	


	

"""学習済みモデルの活用"""
"""
# モデルを読み込む
model = model_from_json(open('predict_model.json').read())

# 学習結果を読み込む
model.load_weights('predict_weights.h5')

model.summary();

model.compile(loss="binary_crossentropy", optimizer=SGD(lr=0.1), metrics=['accuracy'])


#ユーザデータの推定値出力...入力は被験者の入力作業によって得られたデータ
predictions = model.predict(input_data)

#既知・未知推定情報の取得
for i, word in enumerate(predictions):
	if predintions[i] > 0.8:
		know_list.append(all_word_list[i])
		
"""

"""
#ユーザが知っていると思われる単語を表示	
print(know_list)
"""
