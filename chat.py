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
	new = []
	person = None #為了對話如果前面沒有人名，程式會出錯，故在迴圈前加一個人名
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:#前面是None，後面不用補述條件
			new.append(person + ':' + line)#這行在前面是人名的話，會被continue掉，不會執行
	return new

#寫出檔案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

#設計main function
def main():
	lines = read_file('input.txt')	
	lines = convert(lines)
	write_file('outcome.txt', lines)
#這邊才把我們要的input.txt投幣進去
main()