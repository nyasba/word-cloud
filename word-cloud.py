import MeCab

from wordcloud import WordCloud

FILE_NAME = "input.txt"

with open(FILE_NAME, "r", encoding="utf-8") as f:
    text = f.read()

stop_words = [
	'あ','い','う','え','お',
	'か','き','く','け','こ',
	'さ','し','す','せ','そ',
	'た','ち','つ','て','と',
	'な','に','ぬ','ね','の',
	'は','ひ','ふ','へ','ほ',
	'ま','み','む','め','も',
	'や','ゆ','よ',
	'ら','り','る','れ','ろ',
	'わ','を','ん',
	'が','ぎ','ぐ','げ','ご',
	'ざ','じ','ず','ぜ','ぞ',
	'だ','ぢ','づ','で','ど',
	'だ','ぢ','づ','で','ど',
	'する', 'いる', 'ある', 'ない', 'おる',
	'もの', 'いう', 'そう', 'なる', '見る',
	'ござる', 'くださる', '思う', 'いただく',
    'くれる', 'こと', 'できる', 'しまう',
    '欲しい', 'いたす'
]

#MeCab を使用して形態素解析
mecab = MeCab.Tagger()
node  = mecab.parseToNode(text)
words = []

#名詞、動詞、動詞である単語のみを抽出
while node:
    print(node.feature)
    cols = node.feature.split(",")
    if cols[0] == u"名詞" and cols[2] != u"人名":
        words.append(node.surface)
    elif cols[0] == u"形容詞":
        words.append(cols[10])
    elif cols[0] == u"動詞":
        words.append(cols[10])
    elif cols[0] == u"感動詞" and len(cols) > 10:
        words.append(cols[10])
    node = node.next

#単語を空白で結合
text = ' '.join(words);

#ワードクラウドを作成
wordcloud = WordCloud(
	width = 1200,  # 幅
	height = 800,  # 高さ
	background_color = 'white', # 背景色
	font_path = '/System/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc', # 日本語フォントを指定
	stopwords = set(stop_words), # 出力から除外する単語
)

wordcloud.generate(text)
wordcloud.to_file("wordcloud.png")