
# python은 tuple, list, dict 세가지 기본 type을 가장 많이 사용해봐야 합니다.
# python은 tab space 혼용 안된다고 함 :: inconsistent use of tabs and spaces in indentation
def solution(inFile, outFile):
	content = open(inFile, 'r')
	while True:
		line = content.readline()
		if not line:
			break
		print(line)
	content.close()


solution('./in.txt', './out.txt')