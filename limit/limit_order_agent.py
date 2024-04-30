from trading_framework.execution_client import ExecutionClient, MyExecutionClient
from trading_framework.price_listener import PriceListener

class LimitOrderAgent(PriceListener):

    # def __init__(self, execution_client: ExecutionClient):
    #     """

    #     :param execution_client: can be used to buy or sell - see ExecutionClient protocol definition
    #     """
        
    #     super().__init__()
        
    def on_price_tick(self, product_id: str, limit_price: float, order_mode: bool, current_price: float):
        print("From on price tick function at line 15")
        # see PriceListener protocol and readme file
        self.add_order(product_id=product_id, order_mode=order_mode, limit_amount=limit_price, current_price=current_price)

    def add_order(self, product_id, order_mode, limit_amount, current_price):
        mec = MyExecutionClient()
        if order_mode == "buy":
            print("From add order function at line 21###")
            mec.buy(product_id, order_mode, limit_amount, current_price)

        if order_mode == "sell":
            mec.sell(product_id, order_mode, limit_amount, current_price)

