def split_list_by_user(lst):
    result = []
    current_list = []

    for item in lst:
        if item.startswith("USER"):
            if current_list:
                result.append(current_list)
                current_list = []
        current_list.append(item)

    if current_list:
        result.append(current_list)

    return result

# 测试代码
lst = ['USER wo', 'PASS 8765', 'USER wo', 'PASS 08183080', 'CWD wo', 'TYPE I', 'SIZE 1.txt', 'RETR 1.txt', 'USER win', 'PASS 8765', 'CWD hello', 'TYPE I', 'SIZE 2.txt', 'RETR 2.txt', 'MDTM 2.txt', 'USER cu', 'PASS 8888', 'USER cu', 'PASS 888', 'TYPE I', 'SIZE 1.txt', 'RETR 1.txt']

result_lists = split_list_by_user(lst)
for i, sub_list in enumerate(result_lists):
    print(f"List {i+1}:")
    print(sub_list)
    print()