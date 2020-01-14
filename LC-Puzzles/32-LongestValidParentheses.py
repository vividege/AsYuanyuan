def longestValidParentheses(s: str) -> int:
    '''
    Solution I
    算法解释：
    1.从左向右扫描，如果左括号数等于右括号数，那么计数加一
    2.如果右括号数大于左括号数，则复位
    3.同样道理进行从右到左扫描。
    '''
    left = 0
    right = 0
    max = 0
    for c in s:
        if c == '(':
            left += 1
        elif c == ')':
            right += 1
        if left == right:
            max = max if max > 2 * right else 2 * right
        elif right > left:
            left = right = 0
    left = right = 0
    for c in s[::-1]:
        if c == '(':
            left += 1
        elif c == ')':
            right += 1
        if left == right:
            max = max if max > 2 * right else 2 * left
        elif left > right:
            left = right = 0
    return max


def longestValidParentheses2(s: str) -> int:
    '''
    Solution II:
    '''
    max = 0
    stack = list()
    stack.append(-1)  # 设定上一次括号配对正确的位置为-1

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                lastValid = stack[len(stack) - 1]  # lastValid为上一次括号匹配正确的位置
                max = max if i - lastValid < max else i - lastValid  # 当前序号减去上次次匹配正确的位置即为当前最长度
    return max
if __name__ == '__main__':
    s = ')()(())()'
    print(longestValidParentheses2(s))
