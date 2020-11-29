# pandas読み込み
import pandas as pd

# csvファイル読み込み
data = pd.read_csv("data.csv", header=None, sep=",")

# csvリスト化
kimetsu = list(data[0])

kimetsu

# 検索ツールサンプル
# これをベースに課題の内容を追記してください

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# 検索ツール


def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    # ここに検索ロジックを書く
    if bool(word in kimetsu) == True:
        print("{}が見つかりました".format(word))
    else:
        print("リストに存在しません。追加します。")
        kimetsu.append("{}".format(word))


if __name__ == "__main__":
    search()

# 追加したやつ削除
# kimetsu.pop(7)

kimetsu

# リスト → Series
sr = pd.Series(kimetsu)

# Seriesをcsvに書き込み
sr.to_csv("data.csv")

sr
