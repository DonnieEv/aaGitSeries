numbers = [3, 7, 4, 9, 2, 8, 1]

def triangle(length):
    for i in range(1 ,length + 1):
        print("*" * i)

def peak_num(numbers):
    peaks = [i for i in range(1, len(numbers) - 1) if numbers[i] > numbers[i-1] and numbers[i] > numbers[i +1 ]]
    peaksp = [numbers[i] for i in peaks]
    return peaksp

def running_average(numbers):
    total = 0
    result = []
    for i, num in enumerate(numbers):
        total += num
        avg = total / (i + 1)
        result.append(avg)
        print(f"After {num}: {avg:.2f}")
    return result

triangle(len(numbers))
print(' ')
print(peak_num(numbers))
print(' ')
running_average(numbers)
