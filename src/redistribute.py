"""
redistribute.py

Решение задачи о минимальном количестве перемещений фишек
между соседями, чтобы у каждого было поровну.
"""

from typing import List
import statistics


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

    prefixes = []
    prefix = 0
    for c in chips:
        prefix += c - avg
        prefixes.append(prefix)
    # Последний элемент prefixes[-1] будет 0, как и положено

    m = int(statistics.median(prefixes))
    moves = sum(abs(p - m) for p in prefixes)
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
