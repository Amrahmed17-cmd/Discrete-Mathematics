from discrete_math.utils import clear_screen, pause
from discrete_math.combinations import combinations
from discrete_math.permutations import permutations
from discrete_math.cartesian import cartesian_product, display_cartesian_product

def combinations_main():
    """Main function for combinations calculation"""
    clear_screen()
    
    n = int(input("the value of n: "))
    r = int(input("the value of r: "))
    
    print(f"\nC({n}, {r}) = {combinations(n, r)}")
    print()
    pause()

def permutations_main():
    """Main function for permutations calculation"""
    clear_screen()
    
    n = int(input("the value of n: "))
    r = int(input("the value of r: "))
    
    print(f"\nP({n}, {r}) = {permutations(n, r)}")
    print()
    pause()

def cartesian_main():
    """Main function for cartesian product calculation"""
    clear_screen()
    
    set1 = []
    set2 = []
    
    n = int(input("Enter number of elements in set 1: "))
    for i in range(n):
        element = input(f"Element {i+1}: ")
        set1.append(element)
    
    m = int(input("\nEnter number of elements in set 2: "))
    for i in range(m):
        element = input(f"Element {i+1}: ")
        set2.append(element)
    
    product = cartesian_product(set1, set2)
    display_cartesian_product(product)
    
    print()
    pause()

def main_display():
    """Main menu display and control function"""
    choice = 0
    while choice != 4:
        clear_screen()
        print("=============================================================")
        print("===================== Discrete Structure ====================")
        print("=============================================================")
        
        print("1. Combinations")
        print("2. Permutations")
        print("3. Cartesian Product")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("=============================================================")
            print("======================= Combinations ========================")
            print("=============================================================")
            print()
            combinations_main()
        elif choice == 2:
            print("=============================================================")
            print("======================= Permutations ========================")
            print("=============================================================")
            print()
            permutations_main()
        elif choice == 3:
            clear_screen()
            print("=================================================================")
            print("======================= Cartesian Product =======================")
            print("=================================================================")
            print()
            cartesian_main()
        elif choice == 4:
            clear_screen()
            print("Exiting...")
        else:
            print("Invalid choice. Please try again.")
            pause() 