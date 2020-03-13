import sys
import subprocess  # subprocess.call
from collections import Counter


def solution(inFilePath, outFilePath):
    # ===> 파일 입력
    content = open(inFilePath, 'r')
    filteredList = []
    while True:
        line = content.readline()
        if not line:
            break
        tpl = tuple(line.split())
        if tpl[0] != 'jackson':
            filteredList.append(tpl[2])  # 각 이름별 빈도가 아니라 제일 마지막 값의 빈도이므로 콜렉션에는 마지막 값만 있으면 OK
    content.close()

    # ===> 빈도 구하기
    print(str(filteredList))
    counter = Counter(filteredList)
    rs = counter.most_common()

    # ===> 파일 출력
    outFile = open(outFilePath, 'w')
    outFile.write(str(rs))
    outFile.close()

if __name__ == "__main__":
    solution(sys.argv[1], sys.argv[2])
