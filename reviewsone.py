#reviews

count = 0
data = [] #空清單
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1 = count += 1
		if count % 100000 == 0:  # % 是求餘數的意思
			print(len(data))
print('總共有：', len(data), '筆留言')
print('第一筆留言：', data[0])

#計算字詞的出現次數:用字典

wc = {}	#word_count
for d in data:
	words = d.split()	#words將會是一個清單，因為清單切割完會變小清單
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1#新增key

#字典做完:排版
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
#前面是word:key，後面是value(出現幾次)
#想知道有幾個字：
print(len(wc))
#print(wc)
	#print(words)
	#break

#查找特定字詞:
print(wc['Allen'])

#讓使用者查字:
while True:
	word = input('你要查什麼字: ')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為：', wc[word], '次')
	else:
		print('這個字沒有出現過')