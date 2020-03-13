import sys
import subprocess
from collections import Counter


# python은 tab space 혼용 안된다고 함
# ===> 리스트 사이즈를 고정하는 버전
def solution(inFilePath, outFilePath):
    # ===> 파일 입력
    content = open(inFilePath, 'r')
    # proc = subprocess.Popen('cat ./in.txt | wc -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # count = proc.stdout.read()
    # count = proc.communicate()	# read/write 시에 자식 프로세스 블록으로 인한 교착 방어 - async / await 효과 
    count = int(subprocess.getoutput('cat ' + inFilePath + ' | wc -l').strip())
    # List = new ArrayList(count)
    filteredList = [None] * count
    for i in range(0, count):
        line = content.readline()
        tpl = tuple(line.split())
        if tpl[0] != 'jackson':
            filteredList[i] = tpl[2]
    # None 제거
    filteredList = list(filter(lambda x: x is not None, filteredList))
    content.close()

    # ===> 빈도 구하기
    print(str(filteredList))  	# [ 'a', 'a', 'c' ]
    counter = Counter(filteredList)
    rs = counter.most_common()

    # ===> 파일 출력
    outFile = open(outFilePath, 'w')
    outFile.write(str(rs))
    outFile.close()

print('aaa' + str(sys.argv[0]))

if __name__ == "__main__":
    solution(sys.argv[1], sys.argv[2])
