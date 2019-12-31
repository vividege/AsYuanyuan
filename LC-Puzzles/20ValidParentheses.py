def validateParentheses(s):
    parenthese = {'(': ')', '[': ']', '{': '}'}
    stack = list()
    for c in s:
        if c in parenthese.keys():
            stack.append(c)
        else:
            if not stack or c != parenthese.get(stack.pop()):
                return False
    return not stack


if __name__ == '__main__':
    print(validateParentheses(')'))
    print(validateParentheses('('))
    print(validateParentheses('()[]{}{'))
    print(validateParentheses('()[]{}]'))
    print(validateParentheses("([)]"))
    print(validateParentheses("[)"))
    print('===================')
    print(validateParentheses(''))
    print(validateParentheses('()'))
    print(validateParentheses('([{}])'))
    print(validateParentheses('()[]{}'))
    s = list()
