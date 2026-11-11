"""
PS 57 - Bank Loan Calculator
Calculates monthly EMI, total payable amount and total interest for a bank
loan, and checks eligibility based on monthly income (EMI <= 40% of income).
"""

MAX_EMI_PERCENT = 0.40


def calculate_emi(principal, annual_rate, months):
    """EMI = P x r x (1+r)^n / ((1+r)^n - 1), r = annual_rate / 12 / 100.
    If the rate is 0, EMI = P / n. Result is rounded to 2 decimals."""
    if annual_rate == 0:
        emi = principal / months
    else:
        r = annual_rate / 12 / 100
        factor = (1 + r) ** months
        emi = principal * r * factor / (factor - 1)
    return round(emi, 2)


def calculate_total_payable(emi, months):
    """Total payable = (rounded) EMI x number of months."""
    return round(emi * months, 2)


def calculate_total_interest(total_payable, principal):
    """Total interest = total payable - principal."""
    return round(total_payable - principal, 2)


def max_allowed_emi(monthly_income):
    """Maximum EMI allowed is 40% of monthly income."""
    return round(monthly_income * MAX_EMI_PERCENT, 2)


def is_eligible(emi, monthly_income):
    """Eligible if EMI <= 40% of monthly income."""
    return emi <= max_allowed_emi(monthly_income)


def read_number(prompt, convert=float):
    """Read a number from the console; return None if it is not numeric."""
    try:
        return convert(input(prompt).strip())
    except ValueError:
        return None


def main():
    print("===== Bank Loan Calculator =====")

    # Each value is validated as soon as it is entered.
    principal = read_number("Principal: ")
    if principal is None or principal <= 0:
        print("Invalid loan amount. Enter a positive amount.")
        return

    annual_rate = read_number("Annual rate: ")
    if annual_rate is None or not (0 <= annual_rate <= 30):
        print("Invalid annual rate. Enter a rate between 0 and 30.")
        return

    months = read_number("Tenure (months): ", int)
    if months is None or not (1 <= months <= 360):
        print("Invalid tenure. Enter months between 1 and 360.")
        return

    income = read_number("Monthly income: ")
    if income is None or income <= 0:
        print("Invalid monthly income. Enter a positive amount.")
        return

    emi = calculate_emi(principal, annual_rate, months)
    total_payable = calculate_total_payable(emi, months)
    total_interest = calculate_total_interest(total_payable, principal)
    limit = max_allowed_emi(income)

    print()
    if is_eligible(emi, income):
        print(f"EMI: Rs. {emi:.2f} | Total Payable: Rs. {total_payable:.2f}")
        print(f"Total Interest: Rs. {total_interest:.2f} | Eligible: Yes")
    else:
        print(f"EMI: Rs. {emi:.2f}")
        print(f"Maximum allowed EMI (40% of income): Rs. {limit:.2f}")
        print("Loan not eligible: EMI exceeds the allowed limit.")


if __name__ == "__main__":
    main()
