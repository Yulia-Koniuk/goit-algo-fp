import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        total = roll1 + roll2
        sums_count[total] += 1

    probabilities = {key: value / num_rolls * 100 for key, value in sums_count.items()}
    return probabilities

print("\nМетод Монте-Карло:")
def print_probabilities(probabilities):
    for key, value in probabilities.items():
        print(f"{key} - {value:.2f}% ({probabilities[key] / 100:.2f})")

    analytical_data = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
        7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    print("\nАналітичні дані:")
    for key, value in analytical_data.items():
        print(f"{key} - {value:.2f}% ({value / 100:.2f})")

    plt.figure(figsize=(10, 6))
    plt.plot(probabilities.keys(), probabilities.values(), label='Метод Монте-Карло', marker='o')
    plt.plot(analytical_data.keys(), analytical_data.values(), label='Аналітичні дані', linestyle='dashed', marker='x')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність (%)')
    plt.title('Порівняння ймовірностей сум при киданні двох кубиків')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    num_rolls = 1000000
    probabilities = simulate_dice_rolls(num_rolls)
    print_probabilities(probabilities)

