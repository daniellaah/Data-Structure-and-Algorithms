# 解法一:
def solution1(s, d):
    return len(d) <= len(s) and (s+s).find(d) >= 0

# 解法二: 
def solution2(src, des):
    size_src = len(src)
    size_des = len(des)
    if size_des > size_src:
        return False
    flag = None
    for i in range(size_src + 1):
        flag = True
        for j in range(size_des):
            if src[(i+j)%size_src] != des[j]:
                flag = False
                break
        if flag == True:
            return flag
    return flag

if __name__ == "__main__":
    print(solution1('fdasfdvadfasf', 'asffdas'))
    print(solution2('fdasfdvadfasf', 'asffdas'))
    print(solution1('ABCD', 'CDAB'))
    print(solution2('ABCD', 'CDAB'))
