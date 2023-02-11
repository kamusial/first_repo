# def multiply(x, y):
#     if isinstance(x, (int, float)) and isinstance(y, (int, float)):
#         return round(x * y, 5)
#     else:
#         return x * y
#
# def no_of_letter(text):
#     return len(text)

def fissbuzz(i):
    try:
        i = int(float(i))
    except:
        return None
    if i > 0:
        if i % 15 == 0:
            return 'fissbuzz'
        elif i % 5 == 0:
            return 'buzz'
        elif i % 3 == 0:
            return 'fiss'
        return i
    return None

