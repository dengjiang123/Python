class Stock:
    def __init__(self,company="aa",shares=1,share_val=1.0,total_val=1):
        self.company=company
        self.shares=shares
        self.share_val=share_val
        self.total_val=shares*share_val
    def update(self,price):
        self.share_val=price
        self.total_val=self.shares*self.share_val
    def sell(self,num,price):
        self.shares-=num
        self.total_val=self.shares*price
    def buy(self,num,price):
        self.shares+=num
        self.total_val=self.shares*price
    def show(self):
        print(self.company,self.shares)
        print(self.share_val,self.total_val)

zhejiang=Stock("shini",20,12.5)
zhejiang.show()
zhejiang.buy(15,20)
zhejiang.show()
zhejiang.sell(10,1)
zhejiang.show()
zhejiang.update(100)
zhejiang.show()
