def generate_balanced_parentheses():
    def backtrack(s=''):
        if len(s) == 6:
            if is_valid(s):
                result.append(s)
            return
        for char in '{}[]()':
            if char not in s:
                backtrack(s + char)

    def is_valid(expression):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in expression:
            if char in '({[':
                stack.append(char)
            elif char in ')}]':
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return len(stack) == 0

    result = []
    backtrack()
    return result

balanced_parentheses = generate_balanced_parentheses()
print("Valid Combinations of Balanced Parentheses:")
print(balanced_parentheses)
