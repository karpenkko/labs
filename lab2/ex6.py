class BinaryTree:
    def __init__(self, key, price):
        self.key = key
        self.price = price
        self.left = None
        self.right = None

# Method to create nodes
    def insert(self, key, price):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = BinaryTree(key, price)
                else:
                    self.left.insert(key, price)
            elif key > self.key:
                if self.right is None:
                    self.right = BinaryTree(key, price)
                else:
                    self.right.insert(key, price)
        else:
            self.key = key
            self.price = price

# Method to find the node and the total price
    def find_total(self, value, num):
        if value < self.key:
            if self.left is None:
                return f"{value} is not found"
            return self.left.find_total(value, num)
        elif value > self.key:
            if self.right is None:
                return f"{value} is not found"
            return self.right.find_total(value, num)
        else:
            return f"Total: {self.price * num}$"

# Method to print the whole tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print("Key ", self.key, ": ", self.price, "$", sep="")
        if self.right:
            self.right.print_tree()


root = BinaryTree(345, 30)
root.insert(144, 50)
root.insert(370, 45)
root.insert(264, 37)
root.insert(189, 44)
root.insert(351, 63)
root.print_tree()

try:
    print("Enter the product code:")
    code = int(input())
    print("Enter the  number of products:")
    number = int(input())
    print(root.find_total(code, number))
except ValueError:
    print("Enter only integers")