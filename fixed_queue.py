
from typing import Any

class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리"""
        pass
    
    def __init__(self, capacity: int) -> None:
        """큐 초기화"""
        self.no = 0  # 현재 데이터 개수 
        self.front = 0  # 맨 앞 원소 커서
        self.rear = 0  # 맨 끝 원소 커서
        self.capacity = capacity  # 큐의 크기
        self.que = [None] * capacity  # 큐의 본체 (list형 배열)

    def __len__(self) -> int:
        """큐에 있는 모든 데이터 개수를 반환"""
        return self.no
    
    def is_empty(self) -> bool:  # front, rear 값이 둘다 0이 아니어도 큐가 비어있을 수 있음
        return self.no <= 0
    
    def is_full(self) -> bool:
        """큐가 가득 차 있는지 판단"""
        return self.no >= self.capacity
    

    def enque(self, x:Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full 
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0  # rear값이 capacity값과 같아 배열의 끝에 왔을 경우 인덱스를 0으로 되돌림 (링버퍼 구조이기 때문)
    
    def deque(self) -> Any: 
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1  # 맨 앞의 데이터를 디큐
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0  # front값이 capacity값과 같아 배열의 끝에 왔을 경우, 맨 앞 인덱스인 0으로 되돌림 (링버퍼 구조이기 때문)
        return x


    def peek(self) -> Any:
        """큐에서 데이터를 피크(맨 앞 데이터를 들여다봄)"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self, value: Any) -> Any:
        """큐에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity  # 배열의 처음부터 검색하는 게 아닌 front 부터 검색 !
            if self.que[idx] == value:  # 검색 성공
                return idx
        return -1  # 검색 실패
    
    def count(self, value: Any) -> int:
        """큐에 있는 value의 개수를 반환"""
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1  # 들어있으면 개수 +1
        return c
    
    def __contains__(self, value: Any) -> bool:
        """큐에 value가 있는지 판단"""
        return self.count(value)
    
    def clear(self) -> None:
        """큐의 모든 데이터를 비움"""
        self.no = self.front = self.rear = 0  # int형 데이터 타입이기 때문에 0으로 초기화

    def dump(self) -> None:
        """모든 데이터를 맨 앞으로 맨 끝 순으로 출력"""
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
            print()
