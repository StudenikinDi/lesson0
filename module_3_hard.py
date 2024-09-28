data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data_structure):
    sum_len = 0
    sum_int = 0
    def recur(data):
        nonlocal sum_len, sum_int
        if isinstance(data, list) or isinstance(data, set) or isinstance(data, tuple):
           for i in data:
               recur(i)
        elif isinstance(data, dict):
            for value in data.values():
                recur(value)
            for key in data.keys():
                recur(key)
        elif isinstance(data, int) or isinstance(data,str):
            if isinstance(data, int):
                sum_int += data
            elif isinstance(data, str):
                sum_len += len(data)
    recur(data_structure)
    return sum_len + sum_int
result = calculate_structure_sum(data_structure)
print(result)