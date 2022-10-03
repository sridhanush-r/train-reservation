print("WELCOME TO INDIAN RAILWAYS")
print("CHOOSE THE OPTIONS:")
print("1.Login \n"
      "2.PNR Status \n"
      "3.Reservation Booking \n"
      "4.Complaints & Enquiry \n")
x=int(input("enter the choice: "))
if x==1:
      print("if you have account >>> 1"
            "\n"
            "For NEW ACCOUNT >>> 2")
      t=int(input("Enter choice: "))
      if t==1:
            Q=[]
            M = int(input("enter mobile number: "))
            Q.append(M)
            C = input("Enter CAPTCHA: ")
            Q.append(C)
            import random as ra
            b = []
            O = ra.randrange(1000, 9999)
            b.append(O)
            print(f'OTP is :{O}')
            p = int(input("Enter OTP:"))
            if b[0] == p:
                  print("OTP IS VERIFIED")
                  print("LOGIN IS SUCCESSFULL")
                  
            else:
                  print("NOT VERIFIED")
      elif t==2:
            L=[]
            FN = input("First Name:")
            L.append(FN)
            LN = input("Last Name:")
            L.append(LN)
            M = int(input("Mobile Number:"))
            L.append(M)
            print("ADDRESS")
            AD1 = int(input("D.No.:"))
            L.append(AD1)
            AD2 = input("Street:")
            L.append(AD2)
            AD3 = input("Area:")
            L.append(AD3)
            AD4 = input("District:")
            L.append(AD4)
            AD5 = input("State:")
            L.append(AD5)
            AD6 = input("Country:")
            L.append(AD6)
            AD7=int(input("AADHAR NUMBER:"))
            L.append(AD7)
            C = input("Enter CAPTCHA: ")
            import  random as ra
            b=[]
            O = ra.randrange(1000,9999)
            b.append(O)
            print(f'OTP is :{O}')
            p=int(input("Enter OTP:"))
            if b[0]==p:
                  print("OTP IS VERIFIED")
            else:
                  print("NOT VERIFIED")
            print("Account Details:")
            print(L)
elif x==2:
      print("PNR Status")
      y=int(input("Enter PNR Number:32613767"))
      print("Train No:12732"
            "Train Name:blue mountain exp"
            "Boarding Date:14-09-2022"
            "From:CBE"
            "To:OTY")
elif x==3:
      R = []
      print("Reservation ")
      name = input("NAME:")
      R.append(name)
      mbno = int(input("Ph.No.:"))
      R.append(mbno)
      print('"PLEASE ENTER THE SELECTED BOARDING STATION"')
      a = {"st1":"1.CBE","st2":"2.MTP","st3":"3.OTY","st4":"4.NLG"}
      print(a.items())
      f = (input("From:"))
      R.append(f)
      print('"PLEASE ENTER THE SELECTED DEPARTURE STATION"')
      t = (input("To:"))
      R.append(t)
      d = int(input('Date:(DD/MM/YYYY):'))
      R.append(d)
      print("SELECT CLASSES")
      b = {"c1":"1.EA","c2":"2.AC1","c3":"3.AC2","c4":"4.AC3","c5":"5.GEN"}
      print(b.values())
      c = input("PLEASE ENTER THE SELECTED CLASS:")
      R.append(c)
      print(R)

      b = int(input("TO PRINT TICKET >>> 1\n"
                    "TO SEE THE FILLED DETAILS >>> 2"))
      if b == 1:
            print("IRCTC TICKET")
            print("NAME:", R[0])
            print("FROM:", R[2])
            print("TO:", R[3])
            print("DATE:", R[4])
            print("CLASS:", R[5])
            print("PNR No.:462781")
            print("TRAIN No.:1376")
            print("TRAIN NAME: NLG EXP")
      elif b == 2:
            print("TICKET DETAILS")
            print("NAME:", R[0])
            print("FROM:", R[2])
            print("TO:", R[3])
            print("DATE:", R[4])
            print("CLASS:", R[5])
      else:
            print("WRONG OPTION")
elif x==4:
      s=int(input("FOR COMPLAINTS >>> 1\n"
                  "FOR ENQUIRY >>> 2"))
      if s==1:
            f=input("WRITE YOUR COMPLAINTS:")
      elif s==2:
            print("CALL: +91 9876543210 - NORTH\n"
                  "CALL: +91 9876543211 - EAST\n"
                  "CALL: +91 9876543212 - WEST\n"
                  "CALL: +91 9876543213 - SOUTH")
else:
      print("WRONG OPTION"
            "\n"
            "PAGE CLOSED...RELOAD")