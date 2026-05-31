units_to_m = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'cm': 0.01, 'mm': 0.001}
task = input().split()

result = float(task[0]) * units_to_m[task[1]] if task[1] != 'm' else float(task[0])

if task[3] != 'm':
    result /= units_to_m[task[3]]

print(f"{result:.2e}")




