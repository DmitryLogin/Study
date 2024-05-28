from fake_math import divide as f_div
from true_math import divide as t_div


print(f_div(12, 2))
print(t_div(12, 2))

print(f_div(65, 0))
print(t_div(65, 0))

print(f_div(12, 12))
print(t_div(12, 12))
