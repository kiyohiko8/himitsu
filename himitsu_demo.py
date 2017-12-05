import random
import os 




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
#word_vecの作成（0~271）
def mk_vec(all_word_list):
	word_vec = {}
	for i, word in enumerate(all_word_list):

		word_vec[word] = i + 1
		
	return word_vec
	
	
#既知情報辞書の作成
def mk_know_dic(x,vec):
	know_dic  = {}		
	for (j, data) in enumerate(x):
		if x[j] >= 0.8:
			for k,v in vec.items():
				if vec[k] == j:
					know_dic[k] = x[j]
					
	return know_dic
	
	
#ランダムデータの作成(本システムではいらない)
def mk_rand_data(word_len):
	know_data = []
	for i in range(word_len):
		a = random.random()
		know_data.append(a)
		
	return know_data

	
	
	
if __name__ == "__main__":
	word_vec = mk_vec(all_word_list)
	print(word_vec)
	print("word_vec = {")
	for k, v in word_vec.items():
		print("[", k, ":", v, "]")
	print("}")
	
	#全ひみつ道具のデータ数をカウント
	word_len = len(all_word_list)
	
	#ランダム知識データの作成
	know_data = mk_rand_data(word_len)
	
	#ユーザ知識辞書の作成	
	know_dic = mk_know_dic(know_data, word_vec)
	
	#知っていそうな道具を確率とともに表示
	for k, v in know_dic.items():
		print("[", k, ":", v, "]")
	
	

				


