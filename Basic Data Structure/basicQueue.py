from collections import deque

class FoodQueue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, order):
        self.queue.append(order)
        print(f"addOrder: (order)")
        
    def dequeue(self):
        if not self.is_empty():
            order = self.queue.popleft()
            print(f"customersReciveOrder: (order)")
            
    def is_empty(self):
        return len(self.queue) == 0
    
    def display_queue(self):
        print("WaitingOrderInQueue: ")
        for order in self.queue:
            print(order)

# Create a food queue recived's resteruant
food_queue = FoodQueue()

while True:
    print("\nSelect your food order, please : ")
    print("1. add order")
    print("2. recived a first order")
    print("3. show order queue in order list")
    print("4. Exit order")
    
    choice = input("Plases select your order: ")
    
    if choice == '1':
        order = input("Insert your order list: ")
        food_queue.enqueue(order)
    elif choice == '2':
        food_queue.dequeue()
        

     