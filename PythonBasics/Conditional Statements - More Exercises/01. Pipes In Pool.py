v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_v = p1 * h
p2_v = p2 * h

total_v = p1_v + p2_v
current_pool_v = total_v / v * 100

if total_v <= v:
    current_p1_v = p1_v / total_v * 100
    current_p2_v = p2_v / total_v * 100
    print(f'The pool is {current_pool_v:.2f}% full. Pipe 1: {current_p1_v:.2f}%. Pipe 2: {current_p2_v:.2f}%.')
else:
    print(f'For {h:.2f} hours the pool overflows with {(total_v - v):.2f} liters.')
