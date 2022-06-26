m_price = 200
k_price = 175
v_price = 120

cargos_count = int(input())
m_count = 0
m_cargo_quantity = 0
k_count = 0
k_cargo_quantity = 0
v_count = 0
v_cargo_quantity = 0

for _ in range(cargos_count):
    cargo = int(input())
    if cargo <= 3:
        m_count += 1
        m_cargo_quantity += cargo
    elif 4 <= cargo <= 11:
        k_count += 1
        k_cargo_quantity += cargo
    elif cargo >= 12:
        v_count += 1
        v_cargo_quantity += cargo

cargos_quantity = m_cargo_quantity + k_cargo_quantity + v_cargo_quantity
avg_price = (m_cargo_quantity * m_price + k_cargo_quantity * k_price + v_cargo_quantity * v_price) / cargos_quantity
print(f'{avg_price:.2f}')
result = m_cargo_quantity / cargos_quantity * 100
print(f'{result:.2f}%')
result = k_cargo_quantity / cargos_quantity * 100
print(f'{result:.2f}%')
result = v_cargo_quantity / cargos_quantity * 100
print(f'{result:.2f}%')