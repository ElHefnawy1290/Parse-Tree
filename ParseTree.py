import operator

class Node:
    def __init__(self, value):
        self.value = value
        self.leftchild = None
        self.rightchild = None
    
    def getRootVal(self):
        return self.value

    def getLeftChild(self):
        return self.leftchild
    
    def getRightChild(self):
        return self.rightchild
    
    def setLeftChild(self, leftchild):
        self.leftchild = leftchild
    
    def setRightChild(self, rightchild):
        self.rightchild = rightchild

def parse(expression):
    return parse_expression(list(expression.split()))

def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '^': operator.pow}
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(float(evaluate(leftC)), float(evaluate(rightC)))   
    else:
        root_val = parseTree.getRootVal()
        return float(root_val)

def parse_expression(tokens): #                     1 + ( 2 * 3 ) =>                                                             

    if len(tokens) == 1:
        return tokens[0] if isinstance(tokens[0], Node) else Node(tokens[0]) # 1 + node

    # make all () as subtrees and parsing them and return the root of the subtree
    while '(' in tokens:
        open_idx = tokens.index('(')
        close_idx = find_matching_parenthesis(tokens, open_idx)
        sub_tree = parse_expression(tokens[open_idx + 1:close_idx])
        tokens = tokens[:open_idx] + [sub_tree] + tokens[close_idx + 1:]

    
    op_idx = find_lowest_precedence_operator(tokens)
    if(op_idx == -1):
        return tokens[0] if isinstance(tokens[0], Node) else Node(tokens[0])
    
    root = Node(tokens[op_idx])
    root.setLeftChild(parse_expression(tokens[:op_idx]))
    root.setRightChild(parse_expression(tokens[op_idx + 1:]))

    return root

def isValid(parseTree):
    validops = '*/+-^'
    if parseTree is None:
        return False
    if parseTree != None:
        if parseTree.getRootVal() in validops:
            return isValid(parseTree.getLeftChild()) and isValid(parseTree.getRightChild())
        else:
            return not (parseTree.getLeftChild() or parseTree.getRightChild())

def find_matching_parenthesis(tokens, open_idx):
    stack = 1
    for i in range(open_idx + 1, len(tokens)):
        if tokens[i] == '(':
            stack += 1
        elif tokens[i] == ')':
            stack -= 1
        if stack == 0:
            return i
    raise ValueError("Mismatched parentheses")

def find_lowest_precedence_operator(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    lowest = float('inf')
    index = -1
    for i, token in enumerate(tokens):        # 1/3/2  example => will find the second / operator and return the index
        if isinstance(token, Node):
            continue
        if token in precedence and precedence[token] <= lowest:
            lowest = precedence[token]
            index = i
    return index


def printTree(tree, level = 0):
    if tree:
        printTree(tree.getRightChild(), level+1)
        print(' ' * 4 * level + '->', tree.getRootVal())
        printTree(tree.getLeftChild(), level+1)


# Test cases ==========================================================================
expression1 = '6 + ( 3 - 4 ) / ( 4 ^ ( 0 + 3 ) )'           # 5.9375             
expression2 = '1 + ( 2 * 3 )'                               #  7
expression3 = '1 + 2 * ( 3 - 4 )'                           # -1
expression4 = '-1 - 2 - 3'                                  # -6
expression5 = '-2 * 3 + 4'                                  # -2
expression6 = '3 + ( 5 + 2 )'                               # 10
expression7 = '3 + 2 ^ 3'                                   # 11
expression8 = '3 ^ ( 2 + 1 ) + ( 1 + 2 ) + ( 1 + 1 )'       # 32
expression9 =  '( 7 - 6 * 5 ^ 4 + 1 / 3 / 2 )'              # -3743.83
expression10 = '2 * 3 + 5 * 4 - 9 / 6'                      # 24.5
expression11 = '( 2 * 3 + 5 * 4 - 9 / 6 )'                  # 24.5
expression12 = '( ( 3 * 5 ) + ( 1 - 4 ) ) / 4 + 7'          # 11


print("============================= TEST CASES ==============================")
test = Node('*')
test.setLeftChild(Node('+'))
test.setRightChild(Node('^'))
l1 = test.getLeftChild()
r1 = test.getRightChild()
l1.setLeftChild(Node('1'))
l1.setRightChild(Node('2'))
r1.setLeftChild(Node('10'))
r1.setRightChild(Node('2'))
print(isValid(test))
printTree(test)

test = parse(expression1)
print(evaluate(test))

test = parse(expression2)
print(evaluate(test))

test = parse(expression3)
print(evaluate(test))

test = parse(expression4)
print(evaluate(test))

test = parse(expression5)
print(evaluate(test))

test = parse(expression6)
print(evaluate(test))

test = parse(expression7)
print(evaluate(test))

test = parse(expression8)
print(evaluate(test))

test = parse(expression9)
print(evaluate(test))

test = parse(expression10)
print(evaluate(test))

test = parse(expression11)
print(evaluate(test))

test = parse(expression12)
print(evaluate(test))


