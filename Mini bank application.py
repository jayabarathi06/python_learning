class iob:
    def __init__(self,name,address,acc_no,ifsc_code,micr_code):
        self.name=name
        self.address=address
        self.acc_no=acc_no
        self.ifsc_code=ifsc_code
        self.micr_code=micr_code
        self.baln=0
    def deposit(self):
        print("**************WELCOME TO IOB*****************")
        no1=int(input("ENTER YOUR Acc_no: "))
        no2=int(input("RE-ENTER YOUR Acc_no: "))
        ifsccd=int(input("ENTER YOUR IFSC CODE: "))
        micr=int(input("Enter your Micr_code: "))
        if no1==no2 :
            if self.ifsc_code==ifsccd:
                if self.micr_code==micr:
                    
                    print("User of this ACC: ",self.name)
                    d_amount=int(input("Enter your deposit Amount: "))
                    if d_amount>0:
                       self.baln+=d_amount
                       print("Now your Acc_baln is: ",self.baln)
                    else:
                       print("...Minimum you put Rs.1...")
                else:
                    print("Micr_code is mismatched")
            else:
                print("Ifsc_code is mis-matched")
        else:
            print("Acc_no is mismatched")
    def with_raw(self):
        print("************WITHDRAWAL FROM YOUR ACCOUNT*************")
        ac=int(input("ENTER YOUR ACCOUNT_NO: "))
        rac=int(input("RE-ENTER YOUR ACCOUNT_NO: "))
        ifcd=int(input("ENTER YOUR IFSC_CODE: "))
        micd=int(input("ENTER YOUR MICR: "))
        if ac==rac:
            if self.ifsc_code==ifcd:
                if self.micr_code==micd:
                    print("User of this acc: ",self.name)
                    w_amount=int(input("ENTER YOUR WITH_RAW AMOUNT: "))
                    if self.baln>0:
                       if w_amount>0:
                          self.baln-=w_amount
                          print("Your with_raw Amount: ",w_amount)
                          print("Now your acc_baln is: ",self.baln)
                       else:
                           print("Minimum your w_raw amount is Rs 100")
                    else:
                        print("Your Acc_baln is Zero so cann't w_raw Amount.")
                else:
                    print("Micr_code is mismatched")
            else:
                print("Ifsc code is Mismatched")
        else:
            print("Acc details is mismatched")
    def trans(self,sender):
        print("************SEND MONEY TO ANOTHER ACCOUNT*****************")
        num1=int(input("Enter Receiver acc_no: "))
        num2=int(input("Re-enter Receiver acc_no: "))
        ifsc=int(input("Enter Receiver Ifsc_code: "))
        mic=int(input("Enter Micr_code: "))
        if num1==num2 :
            if self.ifsc_code==ifsc:
                if self.micr_code==mic:
                    print("Amount Receiver Name: ",self.name)
                    amount=int(input("Enter sending Amount: "))
                    if sender.baln>=amount:
                       self.baln+=amount
                       sender.baln-=amount
                       print("Now Receiver Acc_baln: ",self.baln)
                       print("Now Sender Acc_balan: ",sender.baln)
                    else:
                        print("Cann't Send Amount Beacuse the sender not have that Amount")
                else:
                    print("Micr_code is Mismatched")
            else:
                print("Ifsc_code is Mismatched")
        else:
            print("Acc details Mismatched")
acc1=iob("jayabarathijayabalan","1/80,tirkoilur",9455,1234,9876)
acc2=iob("sreesha","kallakurichi",12345,1000,3456)
acc1.deposit()
acc1.with_raw()
acc2.trans(acc1)#reciever#now receiver is self.trans(sender)#send the money acc1 to acc2

