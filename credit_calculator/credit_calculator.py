import argparse
import math

def diff_payment(principal, periods, interest):
    total_payment = 0
    for m in range(1, periods + 1):
        monthly_payment = math.ceil(principal / periods + interest * (principal - (principal * (m - 1)) / periods))
        total_payment += monthly_payment
        print(f"Month {m}: payment is {monthly_payment}")
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")

def annuity_payment(principal, periods, interest):
    annuity_payment = math.ceil(principal * (interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
    total_payment = annuity_payment * periods
    print(f"Your annuity payment = {annuity_payment}!")
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")

def loan_principal(payment, periods, interest):
    principal = payment / ((interest * math.pow(1 + interest, periods)) / (math.pow(1 + interest, periods) - 1))
    print(f"Your loan principal = {math.ceil(principal)}!")
    overpayment = payment * periods - principal
    print(f"Overpayment = {overpayment}")

def calculate_diff(args):
    if args.payment:
        print("Incorrect parameters")
        return
    diff_payment(args.principal, args.periods, args.interest)

def calculate_annuity(args):
    if args.payment and args.principal:
        print("Incorrect parameters")
        return
    if args.payment:
        loan_principal(args.payment, args.periods, args.interest)
    elif args.principal:
        periods = math.ceil(math.log(args.payment / (args.payment - args.interest * args.principal), 1 + args.interest))
        years = periods // 12
        months = periods % 12
        if years > 0 and months > 0:
            print(f"It will take {years} years and {months} months to repay this loan!")
        elif years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif months == 0:
            print(f"It will take {years} years to repay this loan!")
        annuity_payment(args.principal, args.periods, args.interest)

def main():
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["diff", "annuity"], help="type of payment")
    parser.add_argument("--principal", type=float, help="loan principal")
    parser.add_argument("--periods", type=int, help="number of periods")
    parser.add_argument("--interest", type=float, help="loan interest")
    parser.add_argument("--payment", type=float, help="monthly payment")

    args = parser.parse_args()

    if not args.type or not args.interest or (args.type == "diff" and args.payment) or (args.payment and args.payment < 0) or (args.principal and args.principal < 0) or (args.periods and args.periods < 0):
        print("Incorrect parameters")
        return

    if args.type == "diff":
        calculate_diff(args)
    else:
        calculate_annuity(args)

if __name__ == "__main__":
    main()
