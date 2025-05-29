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
    pass


if __name__ == "__main__":
    main()
