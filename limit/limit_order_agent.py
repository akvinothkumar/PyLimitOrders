from trading_framework.execution_client import ExecutionClient, ExecutionException
from trading_framework.price_listener import PriceListener

class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient):
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """       
        self.execution_client = execution_client   
        self.order_list = []  
        self.completed_order_list = []
        # super().__init__()

    
    # #Directly we can't able to instantiate the class which inherited the class Protocol but we can inherit the class to the subclass and there we can able to instantiate.
    # def buy(self, product_id: str, order_mode: str, limit_amount: float,  current_price: float):
    #     print("From function buy")
    #     """
    #     Execute a buy order, throws ExecutionException on failure
    #     :param product_id: the product to buy
    #     :param amount: the amount to buy
    #     :return: None
    #     limit_amount: limit_price_either_to_buy_or_sell
    #     """
    #     try:
    #         self.execute_order(order_mode, product_id, limit_amount, current_price)
    #     except ExecutionException as e:
    #         print("Exception:", e.msg)

      

    def execute_order(self, order_mode, product_id, limit_amount, current_price):   
        # print("From execute order function!!!:", order_mode)
        # print("current price:", current_price)
        # print("limit_amount:", limit_amount)    
        if order_mode == "buy":            
            print("==========================BUY MODE===========================================")
            if current_price <= limit_amount:
                print(f"Order bought successfully! Details: Product ID:{product_id}, Amount:{limit_amount}")
            else:
                print("Current price is still higher than the limit price!")  
            print("==========================BUY MODE===========================================")      

        if order_mode == "sell":
            print("==========================SELL MODE===========================================")
            if current_price > limit_amount:
                print(f"Order sold successfully! Details: Product ID:{product_id}, Amount:{limit_amount}")
            else:
                print("Current price isn't higher than the price which you bought!")   
            print("==========================SELL MODE===========================================")    

        # print("From line 52:", self.completed_order_list)
        print("From line 52:", type(self.completed_order_list))
        print("From line 53:", len(self.completed_order_list))
        for completed_order in self.completed_order_list:
            print("54:", completed_order)
        #     self.order_list.remove(completed_order)
            # if completed_order in self.completed_order_list:
            #     # print("From line 55:", completed_order[0])
            self.order_list.remove(completed_order)
        
    def on_price_tick(self, product_id: str, limit_price: float, order_mode: bool, current_price: float):
        print("From on price tick function at line 62")
        # see PriceListener protocol and readme file
        # self.add_order(product_id=product_id, order_mode=order_mode, limit_amount=limit_price, current_price=current_price)
        self.order_list.append((product_id, order_mode, limit_price, current_price))     
        print("From line 66:", self.order_list)  
        self.add_order(self.order_list)

    def add_order(self, order_list):
        print("From line 70:", order_list)
        # mec = MyExecutionClient()
        # self.order_list.append(product_id, order_mode, limit_amount, current_price)
        for order in order_list:
            if order[1] == "buy":
                print("From add order function at line 53###")
                self.execution_client.buy(order[0], order[2])
                try:
                    self.execute_order(order[1], order[0], order[2], order[3])
                except ExecutionException as e:
                    print("Exception:", e.msg)  

            if order[1] == "sell":
                self.execution_client.sell(order[0], order[2])
                try:
                    self.execute_order(order[1], order[0], order[2], order[3])
                except ExecutionException as e:
                    print("Exception:", e.msg)

            self.completed_order_list.append(order)               
        



    
