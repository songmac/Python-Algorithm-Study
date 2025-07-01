
from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""

    class Empty(Exception): 
        """비어 있는 FixedStack에 팝(pop) 또는 피크(peek)할 때 내보내는 예외 처리""" # 피크(peek)? 데이터를 꺼내지 않고 들여다만 보는 동작 (pop과 달리 값을 삭제하지 않음)
        pass

    class Full(Exception):
        """가득 찬 FixedStack에 푸시할 때 내보내는 예외 처리"""
        pass
    

    def __init__(self, capacity: int = 256) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity  # 스택 크기
        self.ptr = 0  # 스택 포인터

    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터 개수를 반환"""
        return self.ptr
    
    def is_empty(self) -> bool:
        """스택이 비어 있는지 판단"""
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        """스택이 가득 차 있는지 판단"""
        return self.ptr >= self.capacity
    

    def push(self, value: Any) -> None:
        """스택에 value를 푸시"""
        if self.is_full():
            raise FixedStack.Full  # 스택이 가득 차 있으면 예외 처리 발생
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """스택에서 데이터를 팝"""
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        """스택에서 데이터를 피크"""
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]
    
    def clear(self) -> None:
        """스택을 비움"""
        self.ptr = 0  # 스택 포인터 값을 통해 빈 스택을 만들면 됨


    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 인덱스를 반환(없으면 -1 반환)"""
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기(top) 부터 선형 검색
            if self.stk[i] == value:
                return i
        return -1
    
    def count(self, value: Any) -> int:
        """스택에 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.ptr):  # 바닥(bottom) 부터 선형 검색
            if self.stk[i] == value:
                c += 1
        return c
    
    def __contains__(self, value: Any) -> bool:  # __(dunder, double underscore) 가 붙은 함수?
        """스택에 value가 있는지 판단"""
        return self.count(value) > 0
    
    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():  # 함수 호출에 왜 self가 붙지?
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
