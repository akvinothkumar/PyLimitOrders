import sys
import os
# sys.path.append('C:\\Users\\SPLPT1\\test\\PyLimitOrders\\trading_framework')
# sys.path.append('C:\Users\SPLPT1\test\PyLimitOrders\trading_framework')
# sys.path.append('\\trading_framework')
# print(sys.path)
# print(os.getcwd())
from trading_framework.execution_client import ExecutionClient
from trading_framework.price_listener import PriceListener

class LimitOrderAgent(PriceListener):

    def __init__(self, execution_client: ExecutionClient) -> None:
        """

        :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
        """
        super().__init__()

    def on_price_tick(self, product_id: str, price: float):
        # see PriceListener protocol and readme file
        self.add_order(product_id=product_id, current_price= price)
        # pass

    def add_order(self, product_id, order_mode, limit_amount, amount, current_price):
        self.current_price = current_price
        self.product_id = product_id
        self.order_mode = order_mode        
        self.limit_amount = limit_amount
        if self.order_mode == "buy":
            self.amount = amount
            ExecutionClient.buy(self.product_id, self.amount, self.order_mode, self.current_price)
        if self.order_mode == "sell":
            self.amount = amount
            ExecutionClient.sell(self.product_id, self.amount, self.order_mode, self.current_price)

# if __name__ == "__main__":
limit_ord_agent = LimitOrderAgent()
limit_ord_agent.on_price_tick("101",'1000')
