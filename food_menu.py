import time

while True:
    def intro():
        print("\nYou are most welcome to our restaurant!")
        print("\nPlease make your order.")
    

    def food_types():
        foods = ['Posho', 'Cassava', 'Matooke', 'Chapati','Potatoes', 'Rice']
        request = input("Please enter a food: ")
        if request in foods:
            print(request, 'is available.')
        else:
            print('Processing...')
            time.sleep(1)
            print(request, 'is not available. Choose another.')
            quit()
    intro()
    
    


    def sauce():
        print("please choose your sauce.")
        sauces = ['Beans', 'Meat', 'Beef', 'G-nuts', 'Pease', 'Chicken', ]
        request = input("please enter sauce: ")
        if request in sauces:
            print(request, 'is available.')
        else:
            print('Processing...')
            time.sleep(1)
            print(request, 'is not available.')
            quit()
    intro()
    food_types()


    def drinks():
        print("What drink would you like to have?")
        def soft_drinks():
            drink = ('Water', 'Coke', 'Pepsi', 'Mirinda', 'Fanta', 'Novida')
            request = input("Choose a soft drink: ")
            if request in drink:
                print(request, "is available")
            else:
                print('Processing...')
                time.sleep(1)
                print(request, 'is not available.')
                quit()
        soft_drinks()
    intro()
    food_types()
    sauce()
    
        
        
    def alcoholic_drinks():
            yo_ddrink = ('', '', '', '')
    alcoholic_drinks()

    def thank_you():
        print("PLEASE ENJOY YOUR MEAL!...")
    
    
    drinks()
    break



