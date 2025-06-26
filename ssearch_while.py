from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    # 함수 어노테이션(Function Annotation) : 파이썬 함수의 매개변수나 반환값에 대해 타입 정보를 명시하는 문법 (강제성 X, 코드 자체에 영향도 X)
    # def 함수이름(매개변수: 타입) -> 반환타입:
    # - Any : 제약이 없는 임의의 자료형을 의미
    # - Sequence : 시퀀스 형을 의미 ex. 리스트(list)형, 바이트 배열(bytearray)형, 문자열(str)형, 튜플(tuple)형, 바이트열(bytes)형

    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while문)"""

    i = 0
    while True:
        if i == len(a):
            return -1  # 검색에 실패한 경우, -1 반환
        if a[i] == key:
            return i  # 검색에 성공한 경우, 현재 배열의 인덱스 번호를 반환
        i += 1