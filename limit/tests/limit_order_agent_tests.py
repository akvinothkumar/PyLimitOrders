import unittest
from limit.limit_order_agent import LimitOrderAgent
from trading_framework.execution_client import ExecutionClient
from random import randint

class MyExecutionClient(ExecutionClient):    
    pass

class LimitOrderAgentTest(unittest.TestCase):
    def test_something(self):
        # self.fail("not implemented")
        my_exe_client = MyExecutionClient()
        limit_order_agent = LimitOrderAgent(my_exe_client)   
        product_id = randint(1,100)
        limit_price = randint(1,10000)
        current_prcie = randint(1, 10000) 
        limit_order_agent.on_price_tick(product_id=product_id,limit_price=limit_price,order_mode='buy',current_price=current_prcie)
        product_id = randint(1,100)
        limit_price = randint(1,10000)
        current_prcie = randint(1, 10000)
        limit_order_agent.on_price_tick(product_id=product_id,limit_price=limit_price,order_mode='sell',current_price=current_prcie)
        