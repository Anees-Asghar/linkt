from linkt.LinkedList import LinkedList

if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()

    for i in range(5): l1.append(i)
    for i in range(5, 10): l2.append(i)
    l3 = l1 + l2
    l3[2] = 'Anees'
    for n in l3: print(n)