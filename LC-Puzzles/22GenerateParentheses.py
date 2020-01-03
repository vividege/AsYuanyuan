'''
定义一个函数backTrack(s,left, right)
1. s:表示当前已经生成的字符串
2. left：表示左括号计数
3. right：表示右括号计数
4. 当s的长度为设定的括号个数2*N时，就成为我们想要的字符串，即可加入结果
5. 如果left小于N,那就用"("加上后面的字串，如果right<left，就让")"加上后面的字串
'''


def generateParentheses(n):
    result = []

    def backTrack(s, left, right):
        if 2 * n == len(s):
            result.append(s)
        if left < n:
            backTrack(s + '(', left + 1, right)
        if right < left:
            backTrack(s + ')', left, right + 1)

    backTrack('', 0, 0)
    return result


if __name__ == '__main__':
    print(generateParentheses(1))
    print(generateParentheses(2))
    print(generateParentheses(3))
    print(generateParentheses(4))
