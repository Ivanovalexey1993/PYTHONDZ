




from decimal import Decimal as d


def num_accuracy(number, accuracy):
    result = d(f"{number}").quantize(d(f"{accuracy}"))
    return result


num = float(input("Введите число : "))
acc = float(input("Enter the required accuracy '0.0001': "))

print(num_accuracy(num, acc))