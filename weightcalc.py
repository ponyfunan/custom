weight: float = input("Weight: ")
assert weight, "Incorrect weight"
weight = float(weight)
measure_system: str = input('(K)g or (L)bs: ').upper()

match measure_system:
    case 'K':
        print(f'Weight in Lbs: {weight * 2.205}')
    case 'L':
        print(f'Weight in Kg: {weight / 2.205}')
    case _: #any other sequence
        print('Incorrect input. Please try again')