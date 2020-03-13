import sys
# import json
# ===> 딕셔너리 키의 특성을 이용한 버전


def solution(inFilePath, outFilePath):
    # ===> 파일 입력
    content = open(inFilePath, 'r')
    dic = {}
    while True:
        line = content.readline()
        if not line:
            break
        tpl = tuple(line.split())
        if tpl[0] != 'jackson':
            dic[tpl[2]] = (dic[tpl[2]] + 1) if (tpl[2] in dic) else 1
            # dic[tpl[2]] = (dic.get(tpl[2], 0)) + 1
    content.close()
    print(dic)

    # ===> 파일 출력
    outFile = open(outFilePath, 'w')
    # outFile.write(json.dumps(dic))
    outFile.write(str(dic))
    outFile.close()

if __name__ == "__main__":
    solution(sys.argv[1], sys.argv[2])
