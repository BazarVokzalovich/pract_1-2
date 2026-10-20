import math
import os
import random
import matplotlib.pyplot as plt

random.seed(42)

os.makedirs("graphics", exist_ok=True)

print("===== БЛОК 1 =====")
P_true = 0.5
N_list = [10, 100, 1000, 10000, 100000, 1000000]

frequency_list = []
delta_list = []

print(f"{'N':<10} | {'W(A)':<12} | {'Похибка Δ':<12}")
print("-" * 38)

for n in N_list:
    M = sum(1 for _ in range(n) if random.random() < P_true)
    wa = M / n
    delta = abs(wa - P_true)

    frequency_list.append(wa)
    delta_list.append(delta)
    print(f"{n:<10} | {wa:<12.5f} | {delta:<12.5f}")

plt.figure(figsize=(10, 5))
plt.axhline(
    y=P_true,
    color="r",
    linestyle="--",
    label=f"Теоретична ймовірність P(A) = {P_true}",
)
plt.plot(
    N_list,
    frequency_list,
    marker="o",
    color="b",
    label="Статистична частота W(A)",
)
plt.xscale("log")
plt.xlabel("Кількість випробувань N (лог. шкала)")
plt.ylabel("Частота / Ймовірність")
plt.title("Блок 1: Закон великих чисел (ЗВЧ)")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig("graphics/block1_lvn.png")
plt.close()


print("\n===== БЛОК 3 =====")
N_pi_list = [10, 100, 1000, 10000, 100000, 1000000]
pi_estimates = []

print(f"{'N':<10} | {'Оцінка':<12} | {'Похибка':<12}")
print("-" * 38)

for n in N_pi_list:
    M_inside = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            M_inside += 1

    pi_approx = 4 * (M_inside / n)
    pi_estimates.append(pi_approx)
    delta_pi = abs(pi_approx - math.pi)
    print(f"{n:<10} | {pi_approx:<12.5f} | {delta_pi:<12.5f}")


plt.figure(figsize=(10, 5))
plt.axhline(
    y=math.pi, color="g", linestyle="--", label=f"math.pi ({math.pi:.5f})"
)
plt.plot(
    N_pi_list,
    pi_estimates,
    marker="s",
    color="orange",
    label="Оцінка Монте-Карло",
)
plt.xscale("log")
plt.xlabel("Кількість точок N (лог. шкала)")
plt.ylabel("Значення Pi")
plt.title("Блок 3: Оцінка числа $\pi$ методом Монте-Карло")
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig("graphics/simulation_results.png")
plt.close()

print("\n[УСПІХ]: Блоки 1 та 3 виконано, графіки збережено в 'graphics/'!")