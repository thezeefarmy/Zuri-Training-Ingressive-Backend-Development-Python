class Budget:

    def __init__(self, food, cloth, entertain):

        self.food = food
        self.cloth= cloth
        self.entertain = entertain


    def compute_balances(self):
    
        print(f" The balance for category food is {self.food}")

        print(f" The balance for category clothing is {self.cloth}")

        print(f" The balance for category entertainment is {self.entertain}")



    def deposit_funds(self, foodDeposit, clothDeposit, entertainDeposit):

        print("##Depositing funds into the categories##\n")

        self.food = self.food + foodDeposit
        self.cloth = self.cloth + clothDeposit
        self.entertain = self.entertain + entertainDeposit

        print("Category Balance after depositing:\n")

        self.compute_balances()


    def withdraw_funds(self, foodWithdraw, clothWithdraw, entertainWithdraw):

        print("##Withdrawing funds from categories##\n")


        self.food = self.food - foodWithdraw
        self.cloth = self.cloth - clothWithdraw
        self.entertain = self.entertain - entertainWithdraw

        print("Category Balance after withdrawing:\n")

        self.compute_balances()

    
    






