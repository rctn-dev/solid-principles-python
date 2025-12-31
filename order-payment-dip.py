
from abc import ABC, abstractmethod
class Order:
    items=[]
    quantities=[]
    prices=[]
    total_price=0
    status='open'

    def add_item(self,item, quantity, price):
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)
    def get_total_price(self):
        for i in range(len(self.quantities)):
            self.total_price+=self.quantities[i]*self.prices[i] 
        return self.total_price
    def set_status(self,status):
        self.status=status
    def get_status(self):
        print(f'Order status:{self.status}')

class Authorizer (ABC):
    @abstractmethod
    def is_authorized(self)->bool:
        pass

class SMSAuth(Authorizer):
    authorized=False
    def verify_code(self,code):
        print(f"verifying SMS code {code}")
        self.authorized=True
    def is_authorized(self)->bool:
        return self.authorized
class NotARobot(Authorizer):
    authorized=False
    def not_a_robot(self):
        print(f"Are you a robot?")
        self.authorized=True
    def is_authorized(self)->bool:
        return self.authorized
    
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code=security_code
    def pay(self,order):
        print('processing credit payment method')
        print(f'verifying security code:{self.security_code}')
        order.set_status("paid")
class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer:Authorizer):
        self.authorizer=authorizer
        self.security_code=security_code
    def pay(self,order, security_code):
        if not self.authorizer.is_authorized():
            raise Exception ("Not Authorized")
        print('processing debit payment method')
        print(f'verifying security code:{self.security_code}')
        order.set_status("paid")
    
class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer:Authorizer):
        self.email_address=email_address
        self.authorizer=authorizer
    def pay(self,order):
        if not self.authorizer.is_authorized():
            raise Exception ("Not Authorized")
        print('processing Paypal payment method')
        print(f'verifying email address:{self.email_address}')
        order.set_status("paid")
if __name__ == "__main__":
    order=Order()
    order.add_item('keyboard',2,150)
    order.add_item('mouse',2,90)
    order.add_item('SSD',1,1000)
    order.get_status()
    print(order.get_total_price())
    authorizer=NotARobot()
    payment=PaypalPaymentProcessor('sde@gmail.com', authorizer)
    authorizer.not_a_robot()
    payment.pay(order)
    order.get_status()