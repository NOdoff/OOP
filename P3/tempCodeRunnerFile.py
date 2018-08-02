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