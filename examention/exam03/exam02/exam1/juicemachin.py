class juiceorder :
    def __init__(self,manu_trpy,num,size,price = "juiceorder"):
        self.manu = manu_trpy
        self.num = num
        self.size = size
        self.price = price

        def check_manu  (manu) 
        manu = manu.upper()
        if manu == "Oj":
            return "orange juice"
        if manu == "Aj":
            return "Appple juice"
        if manu == "Wj":
            return "Watermelon juice"
        if manu == "Pj":
            return "pineapple Juice"