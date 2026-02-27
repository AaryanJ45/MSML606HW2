import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
        # If the input is already empty, we just return None
        if len(input) == 0:
            return None
        
        # Creating a stack to store the nodes/go through the list to make a tree
        # I'm going to create the stack using a list
        stack = []

        # Going through the list, if the current item is an operand, push it to the stack, if it is an operator
        # pop the top two elements in the stack and set them to left and right children on the operator
        for i in input:
            # If the current item is an operand, pushing it to the stack
            if i not in ['+', '-', '*', '/']:
                stack.append(TreeNode(i))
            # If the current item is an operator, setting the right and left children for the operator
            else:
                # Checking if there are enough operands in the stack to perform the operation
                if len(stack) < 2:
                    raise ValueError("Not enough operands to perform the operation")
                right_child = stack.pop()
                left_child = stack.pop()
                stack.append(TreeNode(i, left_child, right_child)) # Now, we can push the operator with its left and right children to the stack
        
        # At the end, the only item that is left in the stack would be the root node of the tree, so we return that
        # Returning the root node of the tree
        return stack.pop()



    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        # If the head is already None, we just return an empty list since there is nothing to print
        if head is None:
            return []
        else:
            # Add the root node to the list, and then recursively calling the function on the left child and the right child
            # PreOrder traversal visits the root node first, then the children from left to right
            return [head.val] + self.prefixNotationPrint(head.left) + self.prefixNotationPrint(head.right)
        

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        # same kind of code as the previous function, recursion, by now adding the parentheses and going in a different order -> left, root, right
        # Again, if the head is already None, we just return empty list
        if head is None:
            return []
        else:
            # Calling the function recursively on the left child, adding the root node, and the calling the function recursively on the right child
            # Adding the parentheses as well in this return
            
            # If the left and right children are both None, we don't want to add parentheses around just the root node, so we just return the root
            if head.left is None and head.right is None:
                return [head.val]
            # Otherwise, we add the parentheses like we were doing before
            else:
                # print(['('] + self.infixNotationPrint(head.left) + [head.val] + self.infixNotationPrint(head.right) + [')'])
                return ['('] + self.infixNotationPrint(head.left) + [head.val] + self.infixNotationPrint(head.right) + [')']


    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        # Same thing as the other two functions, using recursion, but not also in a different order -> left, right, root
        # Returning and empty list if the head is already None
        if head is None:
            return []
        else:
            # Calling the function recursively on the left child, the right child, and then adding the root node to the list
            return self.postfixNotationPrint(head.left) + self.postfixNotationPrint(head.right) + [head.val]


class Stack:
    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):
        # TODO: initialize the stack
        self.stack = [] # Initializing the stack
    
    def push(self, item):
        # Pushing an item into the stack
        self.stack.append(item)
    
    def pop(self): 
        # Popping the top item from the stack
        return self.stack.pop()
    
    def len(self):
        # returning the length of the stack
        return len(self.stack)

    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(self, exp: str) -> int:
        # TODO: implement this using your Stack class

        # checking if there is an empty postfix expression
        if len(exp) == 0:
            return 0       
        stack = Stack() # Creating a stack

        # Going through the expression, if the current item is an operand, I push it to the stack
        # If it is an operator, I pop the top two elements from the stack and perform an operation with them
        # Then, I push the result back into the stack
        for i in exp.split(): # Splitting exp through spaces
            # If the current item is an operand, push it into the stack
            if i not in ['+', '-', '*', '/']:
                # Setting i to an integer before we push, since we are getting in strings
                i = int(i)
                stack.push(i)
            # If the current item is an operator, pop the top two elements and process them
            else:
                # Checking if there are enough operands in the stack to perform the operation
                if stack.len() < 2:
                    raise ValueError("Not enough operands to perform the operation")
                right = stack.pop()
                left = stack.pop()
                # Going through all the cases for the operator
                if i == '+':
                    stack.push(left + right)
                elif i == '-':
                    stack.push(left - right)
                elif i == '*':
                    stack.push(left * right)
                elif i == '/':
                    stack.push(left / right)
                
        # After everything, the only item left in the stack would be the result, so we pop that from the stack and return it
        return stack.pop()



# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")