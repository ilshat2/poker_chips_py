"""
redistribute.py

Решение задачи о минимальном количестве перемещений фишек
между соседями, чтобы у каждого было поровну.
"""

from typing import List


def min_moves(chips: List[int]) -> int:
    """
    Вычисляет минимум ходов по одному обмену между соседями,
    чтобы выровнять количество фишек.
    """
    n = len(chips)
    total = sum(chips)
    if total % n != 0:
        raise ValueError("Нельзя поровну распределить фишки")
    avg = total // n

    moves = 0
    prefix = 0
    # проходим по границам 0-1, 1-2, ..., n-2–n-1
    for i in range(n - 1):
        prefix += chips[i] - avg
        moves += abs(prefix)
    return moves


def main():
    tests = [
        ([1, 5, 9, 10, 5], 12),
        ([1, 2, 3], 1),
        ([0, 1, 1, 1, 1, 1, 1, 1, 1, 2], 1),
    ]
    for chips, expected in tests:
        result = min_moves(chips)
        print(f"{chips} → {result} (ожидалось {expected})")


if __name__ == "__main__":
    main()
