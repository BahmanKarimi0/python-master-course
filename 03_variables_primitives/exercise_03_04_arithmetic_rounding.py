"""
Exercise 03‑04 – arithmetic ops, rounding, formatted output
"""
length: float = 5.6789
width: float = 2.3456
price_per_m2: int = 850_000
area: float = length * width
perimeter: float = (length + width) * 2
area_rounded: float = round(area, 3)
cost = area * price_per_m2
cost_million: float = round(cost / 1_000_000, 2)
square_side: float = area ** 0.5
side_cm: str = str(round(square_side * 100, 1))
print(f'Area: {area:.4f} m\u00B2  (rounded: {area_rounded} m\u00B2')
print(f'Perimeter : {perimeter:.6f} m')
print(f'Cost: {cost:,.2f} Rials  ≈ {cost_million} million Rials')
print(f'Equivalent square side: {square_side:.2f} m  ({side_cm} cm)')
