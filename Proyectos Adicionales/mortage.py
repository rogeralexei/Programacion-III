class Mortage():
    def __init__(self,loan,interest):
        self.loan=loan
        self.interest=interest/100

    def fixed_terms(self,n):
        total=self.loan+(self.loan*self.interest)
        fixed_terms=total/n
        return "The user will need to pay {} per month during the fixed term of {} payments".format(fixed_terms,n)

    
if __name__=="__main__":
    loan=float(input("Please provide us the amount of your loan: "))
    interest=float(input("Please provide us the amount of your total interest: "))
    customer_loan=Mortage(loan,interest)
    n=int(input("Please provide the number of terms in months to pay your loan: "))
    print(customer_loan.fixed_terms(n))




    