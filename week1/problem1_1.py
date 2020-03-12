# import os			# os.system - Not able to fetch std out
import subprocess	# subprocess.call
# import commands	# removed since 3.6
from collections import Counter

# python은 tab space 혼용 안된다고 함 :: inconsistent use of tabs and spaces in indentation
def solution(inFilePath, outFilePath):

	# ===> 파일 입력
	content = open(inFilePath, 'r')
	# proc = subprocess.Popen('cat ./in.txt | wc -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	# count = proc.stdout.read()
	# count = proc.communicate()
	count = int(subprocess.getoutput('cat ./in.txt | wc -l').strip())
	# List = new ArrayList(count) 같은 걸 하고 싶으면?
	# [ 1 ] filteredListIdx = 0;
	# [ 1 ] filteredList = [ None ]*count
	filteredList = []
	print(count, type(count))
	while True:
		line = content.readline()
		if not line:
			break
		tpl = tuple(line.split())
		if tpl[0] != 'jackson':
			# [ 1 ] filteredList[filteredListIdx] = tpl[2]
			# [ 1 ] filteredListIdx++
			filteredList.append(tpl[2])	# 각 이름별 빈도가 아니라 제일 마지막 값의 빈도이므로 콜렉션에는 마지막 값만 있으면 OK
	content.close()

	# ===> 빈도 구하기
	print(str(filteredList))	# [ 'a', 'a', 'c' ] 
	counter = Counter(filteredList)
	rs = counter.most_common()

	# ===> 파일 출력
	outFile = open(outFilePath, 'w')
	outFile.write(str(rs))
	outFile.close()


solution('./in.txt', './out.txt')