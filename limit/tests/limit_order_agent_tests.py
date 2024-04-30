import unittest
from limit.limit_order_agent import LimitOrderAgent
from trading_framework.execution_client import ExecutionClient

class LimitOrderAgentTest(unittest.TestCase):
    def test_something(self):
        # self.fail("not implemented")
        # exe_client = ExecutionClient()
        limit_order_agent = LimitOrderAgent()    
        limit_order_agent.on_price_tick(product_id='101',limit_price=99,order_mode='buy',current_price=200)
        limit_order_agent.on_price_tick(product_id='101',limit_price=101,order_mode='sell',current_price=100)

   

