
from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1  # 비어있음
    DELETED = 2 # 삭제 완료


class Bucket:
    """해시를 구성하는 버킷"""

    def __init__(self, key: Any = None, value: Any = None,
                 stat: Status = Status.EMPTY) -> None:  # '-> None'문법으로 보아 해당 함수는 반환 값이 없음을 의미
        """초기화"""
        self.key = key  # 키
        self.value = value  # 값
        self.stat = stat  # 속성

    def set(self, key: Any, value: Any, stat: Status) -> None:  # 위의 init과 달리, 이미 만들어진 객체에 값을 덮어쓸 수 있는 함수
        """모든 필드에 값을 설정"""
        self.key = key  # 키
        self.value = value  # 값
        self.stat = stat  # 속성

    def set_status(self, stat: Status) -> None:  # def set에 이미 속성이 있지만, 단순히 stat만 바꾸고 싶을 때 불필요하게 key/value까지 다시 넘기지 않도록 분리함
        """속성을 설정"""
        self.stat = stat


class OpenHash:
    """오픈 주소법으로 구현하는 해시 클래스"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity  # 해시 테이블의 크기를 지정
        self.table = [Bucket()] * self.capacity  # 해시 테이블

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):  # isinstance(obj, type) 함수는 객체 obj가 해당 타입인지 확인하는 내장 함수 
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    def rehash_value(self, key: Any) -> int:
        """재해시값을 구함"""
        return(self.hash_value(key) + 1) % self.capacity
    
    def search_node(self, key: Any) -> Any:  # 버킷 객체를 반환 (내부적으로 조작 시 사용)
        """키가 key인 버킷을 검색"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]  # 버킷을 주목

        for i in range(self.capacity):  # i 말고 _로 하는 게 파이썬 관용이지만 i로 써도 됨  
                                        # 왜 해시 테이블 크기 만큼 반복해야하는지? 모든 버킷을 확인해도 빈자리가 없을 수 있기에, 전체 테이블 만큼 순회해야 함
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return None
    
    def search(self, key: Any) -> Any:  # 버킷의 value만 반환 (사용자에게 보여줄 때 사용)
        """키가 key인 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:
            return p.value  # 검색 성공
        else:
            return None  # 검색 실패
        
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        if self.search(key) is not None:
            return False  # 이미 등록된 키
        
        hash = self.hash_value(key)  # 추가하는 키의 해시값
        p = self.table[hash]  # 버킷을 주목
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return False  # 해시 테이블이 가득 참 (EMPTY or DELETED 버킷을 찾지 못했다면 테이블 전체가 꽉 찼다는 것을 의미)
    
    def remove(self, key: Any) -> int:
        """키가 key인 원소를 삭제"""
        p = self.search_node(key)  # 버킷을 주목
        if p is None:
            return False  # 이 키는 등록되어 있지 않음
        p.set_status(Status.DELETED)
        return True
    
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i].stat == Status.DELETED:
                print('-- 삭제 완료 --')
