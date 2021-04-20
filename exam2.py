def func(deposit_amount, amount, annual_percentage):
    result = deposit_amount
    count = 0
    while result < amount:
        result = annual_percentage / 100 / 12 * result + result
        count += 1
    return count


print(func(1000000, 1061520.150601, 12))
