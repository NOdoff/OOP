from stack import Stack
from queue import Queue
 

def evalExpr(expr):

    def isMoreImportant(operator, stack_top_operator):
        if stack_top_operator == None:
            return False

        if operator in P_m_d:
            return True
        else:
            if stack_top_operator in P_m_d:
                return False
            else:
                return True

    def perfomOperator(op1, op, op2):
        if op == "+":
            return int(op1) + int(op2)
        elif op == "-":
            return int(op1) - int(op2)
        elif op == "*":
            return int(op1) * int(op2)
        else:
            return int(op1) / int(op2)

    operator = Stack()
    operand = Stack()
    num = list('0123456789')
    P_m_d = list('*/')
    P_a_s = list('-+')
    for char in expr:
        print(' -> ', operand.__str__())
        print(' => ', operator.__str__())
        if char in num:
            operand.push(char)
        elif char == '(':
            operator.push(char)
        elif char in P_m_d or char in P_a_s:
            while isMoreImportant(char, operator.peek()):
                if operator.peek() not in P_m_d and \
                operator.peek() not in P_a_s:
                    operator.push(char)
                else:
                    if(operand.size() < 2):
                        break
                    op = operator.pop()
                    op1 = operand.pop()
                    op2 = operand.pop()
                    operand.push(perfomOperator(op1,op,op2))
        elif char == ')':
            while(operator.peek() != '('):
                op = operator.pop()
                op1 = operand.pop()
                op2 = operand.pop()
                operand.push(perfomOperator(op1,op,op2))
        else:
            pass
    while not operator.isEmpty():
        op = operator.pop()
        op1 = operand.pop()
        op2 = operand.pop()
        operand.push(perfomOperator(op1,op,op2))

    return operand.peek()
   

if __name__ == '__main__':
    m_expr = input("Enter the expression: ")
    print(evalExpr(m_expr))