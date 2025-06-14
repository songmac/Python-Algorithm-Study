
from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형(Sequence) a 요소의 최댓값을 임의의 자료형(Any)으로 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
