import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))
# print(len(['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
# 'await', 'break', 'class','continue','def', 'del', 'elif', 'else',
# 'except', 'finally', 'for', 'from','global', 'if','import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
# 'while', 'with', 'yield']))
print(keyword.iskeyword('False'))
print(keyword.iskeyword('True'))
print(keyword.iskeyword('return'))
print(keyword.iskeyword('print'))
print(keyword.iskeyword('assert'))
print(keyword.iskeyword('try'))
