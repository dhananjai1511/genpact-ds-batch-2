class Triangle:
    def __init__(self, display):
        self.display = display
    
    def lower_diag_triangle(self, n):
        for i in range(n):
            for j in range(n):
                if i >= j:
                    print(self.display, end = "")
                else:
                    print("   ", end = "")
            print("\n")

    def upper_diag_triangle(self, n):
        for i in range(n):
            for j in range(n):
                if i <= j:
                    print(self.display, end = "")
                else:
                    print("   ", end = "")
            
            print("\n")

    def square(self, n):
        for i in range(n):
            for j in range(n):
                print(self.display, end = "")
            
            print("\n")
    
    def secondary_upper_diag_triangle(self, n):
        for i in range(n):
            for j in range(n):
                if j >= n - i - 1:
                    print(self.display, end = "")
                else:
                    print("   ", end = "")
            
            print("\n")