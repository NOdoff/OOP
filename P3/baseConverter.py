from queue import Queue

def baseConverter(decNum, base):
    i_num = int(decNum)
    i_base = int(base)

    q = Queue()

    while i_num != 0:
        if i_base > i_num:
            q.enqueue(i_num)
            i_num = 0
        elif i_num % i_base == 0: 
            c_num = i_num / i_base
            q.enqueue(c_num)
            i_num = i_num - i_base * c_num
        else:
            i = 1
            multiple = i_base
            while multiple < i_num:
                i += 1
                multiple = multiple * i
                
            i_num = i_num - i_base * (i - 1)
            q.enqueue(i - 1)
    out = ''
    while not q.isEmpty():  
        out += str(q.dequeue())
    
    return out
    

if __name__ == '__main__':
    num = input("Enter the decimal number: ")
    base = input("Enter the base: ")
    print(baseConverter(num, base))