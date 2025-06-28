
from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드""" # 키-값 이 짝을 이루는 구조

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key  # 키 (임의의 자료형)  
        self.value = value  # 값 (임의의 자료형)
        self.next = next  # 뒤쪽 노드를 참고 (Node형)



class ChainedHash:
    """체인법으로 해시 클래스 구현"""
    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity  # 해시 테이블 크기 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)에 모든 버킷이 비어있는 상태


    def hash_value(self, key:Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)  # 해시 값은 다이제스트(digest)값이라고도 함
            # 코드 설명 
            # - key가 int형인 경우와 int형이 아닌 경우(문자열, 리스트, 클래스형 등)를 모두 충족하기 위해 표준 라이브러리로 형 변환 진행
            # - sha256알고리즘 : RSA의 FIPS 알고리즘을 바탕으로 하고, 주어진 바이트 문자열의 해시값을 구하는 해시 알고리즘의 생성자(constructor)임
            # - encode() 함수 : hashlib.sha256에 인수를 전달하기 위해 encode 함수로 바이트 문자열을 생성
            # - hexdigest() 함수 : 해시값을 16진수 문자열로 꺼냄
            # - int 함수 : 16진수 문자열을 int 형으로 변환


    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]  # 노드를 주목

        while p is not None:
            if p.key == key:
                return p.value  # 검색 성공
            p = p.next
        
        return None  # 검색 실패
    

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)  ## 추가하는 key의 해시값
        p = self.table[hash]  # 노드를 주목

        while p is not None:
            if p.key == key:
                return False  # 추가 실패
            p = p.next  # 뒤쪽 노드 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp  # 노드를 추가
        return True  # 추가 성공


    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)  # 삭제할 key의 해시값
        p = self.table[hash]  # 노드를 주목
        pp = None  # 바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  # key 삭제 성공
            pp = p.next  # 뒤쪽 노드를 주목
        return False  # 삭제 실패(key가 존재하지 않음)
    
    
    def dump(self) -> None:
        """해시 테이블을 덤프(내용을 통째로 출력)"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  ⇾ {p.key} ({p.value})', end='')  # 해시값이 같은 버킷의 (키:값)을 화살표로 연결
                p = p.next
            print()
