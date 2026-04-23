from typing import List

Data = List[int]

def mul_data(data: Data) -> int:
    result = 1
    for num in data:
        result = result * num
    return result

print(mul_data([1,2,3,4.2]))