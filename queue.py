#FIFO

queue = []


def enQ():
    queue.append(input("Enter new string: ").strip())

def deQ():
    if len(queue) == 0:
        print("Can't pop from an empty queue")
    else:
        print("Removed [",queue.pop(0),"]")

def viewQ():
    print(queue)

CMDs = {'e' : enQ, 'd' : deQ, 'v' : viewQ}

def showmenu():
    pr = """
    (E)nqueue
    (D)equue
    (V)iew
    (Q)uit
    Enter choice: """

    while True:
        while True:
            try:
                choice = input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            
            print("\nYou picked: [%s]" % choice)
            if choice not in 'edvq':
                print("Invalid choice, try again")
            else:
                break
        
        if choice == "q":
            break
        CMDs[choice]()

if __name__ == '__main__':
    showmenu()