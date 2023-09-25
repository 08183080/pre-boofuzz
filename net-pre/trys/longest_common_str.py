"""
和其有关系的py文件
string_distance.py
"""
# LCS问题
def find_lcsubstr(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    mmax = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i+1][j+1] = m[i][j] + 1
                if m[i+1][j+1] > mmax:
                    mmax = m[i+1][j+1]
                    p = i + 1
    return s1[p-mmax:p],mmax    # 返回最长字串及其长度

s1 = "USER dragon"
s2 = "USER luffy"

print(f"{s1}和{s2}的最长公共子串:", find_lcsubstr(s1, s2)[0])
print(f"识别的模式:{find_lcsubstr(s1, s2)[0]}"," xxx")