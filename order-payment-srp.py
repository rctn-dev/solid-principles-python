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
    def set_status(self):
        self.status='paid'
    def get_status(self):
        print(f'Order status:{self.status}')
    
class PaymentProcessor:
    def pay_credit(self,order, security_code):
        print('processing credit payment method')
        print(f'verifying security code:{security_code}')
        order.set_status()
    def pay_debit(self,order, security_code):
        print('processing debit payment method')
        print(f'verifying security code:{security_code}')
        order.set_status()
if __name__ == "__main__":
    order=Order()
    order.add_item('keyboard',2,150)
    order.add_item('mouse',2,90)
    order.add_item('SSD',1,1000)
    order.get_status()
    print(order.get_total_price())
    payment=PaymentProcessor()
    payment.pay_credit(order,'12496523')
    order.get_status()