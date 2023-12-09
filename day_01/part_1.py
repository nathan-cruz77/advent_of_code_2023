total = 0

with open('input.txt') as f:
    for line in f:
        digits = [c for c in line if c.isdigit()]
        calibration_value = int(f'{digits[0]}{digits[-1]}')

        print(calibration_value)

        total += calibration_value

    print(total)
