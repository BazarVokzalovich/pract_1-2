import random

random.seed(42)

print("===== БЛОК 2 - Варіант 3 =====")
exact_A = 0.5
exact_B = 0.5
exact_intersection = 0.125
exact_union = 0.875
exact_complement = 0.5

N_block2 = 1000000

count_a = 0
count_b = 0
count_a_and_b = 0
count_a_or_b = 0
count_not_a = 0

for _ in range(N_block2):
    x = random.random()
    y = random.random()

    is_a = x < 0.5
    is_b = y < x

    if is_a:
        count_a += 1
    if is_b:
        count_b += 1
    if is_a and is_b:
        count_a_and_b += 1
    if is_a or is_b:
        count_a_or_b += 1
    if not is_a:
        count_not_a += 1

w_A = count_a / N_block2
w_B = count_b / N_block2
w_intersection = count_a_and_b / N_block2
w_union = count_a_or_b / N_block2
w_complement = count_not_a / N_block2

print(f"{'':<12} | {'Статистика':<12} | {'Теорія':<12} | {'Похибка':<12}")
print("-" * 55)
print(
    f"P(A)         | {w_A:<12.5f} | {exact_A:<12.5f} | {abs(w_A - exact_A):<12.5f}"
)
print(
    f"P(B)         | {w_B:<12.5f} | {exact_B:<12.5f} | {abs(w_B - exact_B):<12.5f}"
)
print(
    f"P(A ∩ B)     | {w_intersection:<12.5f} | {exact_intersection:<12.5f} | {abs(w_intersection - exact_intersection):<12.5f}"
)
print(
    f"P(A ∪ B)     | {w_union:<12.5f} | {exact_union:<12.5f} | {abs(w_union - exact_union):<12.5f}"
)
print(
    f"P(not A)     | {w_complement:<12.5f} | {exact_complement:<12.5f} | {abs(w_complement - exact_complement):<12.5f}"
)

print("\nПеревірка аксіом та теорем ймовірностей:")
print(
    f"1. Теорема додавання: стат {w_union:.5f} ≈ теор {exact_A} + {exact_B} - {exact_intersection} = {exact_union}"
)
print(
    f"2. Властивість протилежної події: P(not A) = 1 - P(A) -> {w_complement:.5f} = 1 - {w_A:.5f} = {1 - w_A:.5f}\n"
)

print("===== БЛОК 4 - Варіант 3 =====")
total_api = 10000
requests_2xx = 9700
requests_4xx = 200
requests_5xx = 100

p_2xx = requests_2xx / total_api
p_4xx = requests_4xx / total_api
p_5xx = requests_5xx / total_api

print(f"Загальна кількість API-запитів: {total_api}")
print(
    f"Статистична ймовірність класу 2xx P(2xx): {p_2xx:.4f} ({p_2xx*100:.2f}%)"
)
print(
    f"Статистична ймовірність класу 4xx P(4xx): {p_4xx:.4f} ({p_4xx*100:.2f}%)"
)
print(
    f"Статистична ймовірність класу 5xx P(5xx): {p_5xx:.4f} ({p_5xx*100:.2f}%)"
)

total_group_sum = p_2xx + p_4xx + p_5xx
print(f"\nПеревірка повної групи: P(2xx) + P(4xx) + P(5xx) = {total_group_sum}")

if abs(total_group_sum - 1.0) < 1e-9:
    print(
        "Висновок: Сума дорівнює 1.0. Події попарно несумісні та утворюють повну групу подій."
    )
