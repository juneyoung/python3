# import json

# use dictionary - 
def solution(inFilePath, outFilePath):
	content = open(inFilePath, 'r')
	dic = {}
	while True:
		line = content.readline()
		if not line:
			break
		tpl = tuple(line.split())
		if tpl[0] != 'jackson':
			# dic[tpl[2]] = 0 if (dic[tpl[2]] == None) else (dic[tpl[2]] + 1)
			dic[tpl[2]] = (dic.get(tpl[2], 0)) + 1
	content.close()
	print(dic)
	# writing file
	outFile = open(outFilePath, 'w')
	# outFile.write(json.dumps(dic))
	outFile.write(str(dic))
	outFile.close()


solution('./in.txt', 'out.txt')