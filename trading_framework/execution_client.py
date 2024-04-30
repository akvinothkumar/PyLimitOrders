from typing import Protocol


class ExecutionException(Exception):
    msg = "Check the data properly to ignore the errors"


class ExecutionClient(Protocol):

    def buy(self, product_id: str, order_mode: str, limit_amount: int,  current_price: int):
        """
        Execute a buy order, throws ExecutionException on failure
        :param product_id: the product to buy
        :param amount: the amount to buy
        :return: None
        """
        ... 
        

    def sell(self, product_id: str,  order_mode: str, limit_amount: int, current_price: int):
        """
        Execute a sell order, throws ExecutionException on failure
        :param product_id: the product to sell
        :param amount: the amount to sell
        :return: None
        amount: existing_order_price
        order_mode: flag_value_to_decide_buy_or_sell
        """
        ... 

            

    

class MyExecutionClient(ExecutionClient):
    #Directly we can't able to instantiate the class which inherited the class Protocol but we can inherit the class to the subclass and there we can able to instantiate.
    def buy(self, product_id: str, order_mode: str, limit_amount: float,  current_price: float):
        print("From function buy")
        """
        Execute a buy order, throws ExecutionException on failure
        :param product_id: the product to buy
        :param amount: the amount to buy
        :return: None
        limit_amount: limit_price_either_to_buy_or_sell
        """
        try:
            self.execute_order(order_mode, product_id, limit_amount, current_price)
        except ExecutionException as e:
            print("Exception:", e.msg)
        

    def sell(self, product_id: str,  order_mode: str, limit_amount: float, current_price: float):
        print("From function sell")
        """
        Execute a sell order, throws ExecutionException on failure
        :param product_id: the product to sell
        :param amount: the amount to sell
        :return: None
        limit_amount: limit_price_either_to_buy_or_sell
        order_mode: flag_value_to_decide_buy_or_sell
        """
        try:
            self.execute_order(order_mode, product_id, limit_amount, current_price)
        except ExecutionException as e:
            print("Exception:", e.msg)   

    def execute_order(self, order_mode, product_id, limit_amount, current_price):   
        # print("From execute order function!!!:", order_mode)
        # print("current price:", current_price)
        # print("limit_amount:", limit_amount)    
        if order_mode == "buy":            
            if current_price <= limit_amount:
                print(f"Order bought successfully! Details: Product ID:{product_id}, Amount:{limit_amount}")
            else:
                print("Current price is still higher than the limit price!")    

        if order_mode == "sell":
            if current_price > limit_amount:
                print(f"Order sold successfully! Details: Product ID:{product_id}, Amount:{limit_amount}")
            else:
                print("Current price isn't higher than the price which you bought!")    