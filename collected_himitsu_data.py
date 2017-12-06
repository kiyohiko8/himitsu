"""
###プログラム概要
- 収集したデータより入力データと教師データを作成
"""
#collected himitsu-data by google form 

import os
import random
import himitsu_data_gd

#訓練データの作成	
def mk_x_train(all_word_list, word_vec, collected):
	
	#ユーザ毎のデータをまとめた全データ
	x_train = []
	for items in collected:
		#ユーザ毎のデータ
		x_data  = []
		for item in items:
			x_data.append(word_vec[item])
		
		for i in range(10):
			#知っているデータからランダムに5個選択
			x_predata = random.sample(x_data, 5)
			#昇順にソート
			x_predata.sort()
			x_train.append(x_predata)
		
	return x_train
	
	
#教師データの作成
def mk_y_train(all_word_list, collected):
	y_train = []
	for j in all_word_list:
		y_data = []
		#collectedの中の一つのリストはユーザ用
		for words in collected:
			#ユーザのデータの中にユーザーが選択した道具があるなら１を追加
			if j in words:
				y_data.append(int(1))
				
			else:
				y_data.append(int(0))
			
			for i in range(10):
				y_train.append(y_data)
				
	return y_train
				




if __name__ == "__main__":

	himitsu  = himitsu_data_gd.mk_allword_list()
	word_vec = himitsu_data_gd.mk_vec(himitsu)

	#模擬データでcollectedを生成
	collected = []
	for j in range(10):
		b = random.randint(8,50)
		user = random.sample(himitsu, b)
		
		collected.append(user)
		
	
			


	x_train  = mk_x_train(himitsu, word_vec, collected)
	y_train  = mk_y_train(himitsu, collected)
	
	print(x_train)
	print(y_train)
	
	


