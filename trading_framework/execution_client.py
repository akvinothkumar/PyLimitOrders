from typing import Protocol


class ExecutionException(Exception):
    msg = "Check the data properly to ignore the errors"


class ExecutionClient(Protocol):

    def buy(self, product_id: str, amount: int, order_mode: str, current_price: int):
        """
        Execute a buy order, throws ExecutionException on failure
        :param product_id: the product to buy
        :param amount: the amount to buy
        :return: None
        """
        try:
            self.execute_order(order_mode, product_id, amount, current_price)
        except ExecutionException as e:
            print("Exception:", e.msg)
        

    def sell(self, product_id: str, amount: int, order_mode: str, current_price: int):
        """
        Execute a sell order, throws ExecutionException on failure
        :param product_id: the product to sell
        :param amount: the amount to sell
        :return: None
        amount: existing_order_price
        order_mode: flag_value_to_decide_buy_or_sell
        """
        try:
            self.execute_order(order_mode, product_id, amount, current_price)
        except ExecutionException as e:
            print("Exception:", e.msg)   

    def execute_order(self, order_mode, product_id, amount, current_price):
        if order_mode == "buy":
            if current_price <= amount:
                print(f"Order bought successfully! Details: Product ID:{product_id}, Amount:{amount}")
        else:
            if current_price > amount:
                print(f"Order sold successfully! Details: Product ID:{product_id}, Amount:{amount}")
