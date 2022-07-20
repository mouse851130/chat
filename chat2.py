#chat2
#chat

# 1. 讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
#encoding = utf-8-sig是為了解決編碼有中文的問題

#2.轉換對話紀錄
def convert(lines):
	person = None #為了對話如果前面沒有人名，程式會出錯，故在迴圈前加一個人名
	allen_word_count = 0
	allen_sticker_count = 0
	allen_picture_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_picture_count = 0
	for line in lines:
		s = line.split(' ') #split切割完會變成清單
		time = s[0]
		name = s[1]
		#這裡可以看listsplit的python，有寫清單的存取模式
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_picture_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name =='Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_picture_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	
	print('Allen說了幾個字:', allen_word_count)
	print('Allen傳的貼圖:', allen_sticker_count)
	print('Viki說了幾個字:', viki_word_count)
	print('Viki傳的貼圖:', viki_sticker_count)	
	print('Allen傳的圖片:', allen_picture_count)
	print('Viki傳的圖片:', viki_picture_count)
		#print(s)


#寫出檔案，function跟function中間要空兩行
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

#設計main function
def main():
	lines = read_file('LINE-Viki.txt')	
	lines = convert(lines)
	#write_file('outcome2.txt', lines)
#這邊才把我們要的input.txt投幣進去
main()