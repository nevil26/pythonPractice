import csv

def calculate_payout(sales,target,commission_rate,tax_rate):
    commission_rate = 0.05 if sales < 150000 else 0.07
    if sales >= target:
        gross_payout = (sales - target) * commission_rate
    else:
        gross_payout = 0
    tax = gross_payout * tax_rate
    net_payout = gross_payout - tax
    return gross_payout, tax, net_payout

with open ("payout_data_20.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        emp_sales = float(row["Sales"])
        emp_target = float(row["Target"])
        emp_commission = float(row["Commission_rate"])
        emp_tax = float(row["Tax_rate"])

        Gross, Tax, Net = calculate_payout(emp_sales,emp_target,emp_commission,emp_tax)
        print(f"{row['Name']}: Gross = {Gross:.2f}, Tax = {Tax:.2f}, Net = {Net:.2f}")

with open("payout_results.csv", "w") as output_file:
    fieldnames = ["Employee_ID", "Name", "Gross_Payout", "Tax", "Net_Payout"]
    writer = csv.DictWriter(output_file, fieldnames)
    writer.writeheader()

    # Reopen data set
    with open("payout_data_20.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            emp_sales = float(row["Sales"])
            emp_target = float(row["Target"])
            emp_commission = float(row["Commission_rate"])
            emp_tax = float(row["Tax_rate"])

            gross, tax, net = calculate_payout(emp_sales, emp_target, emp_commission, emp_tax)

            writer.writerow({
                "Employee_ID": row["Employee_ID"],
                "Name": row["Name"],
                "Gross_Payout": round(gross, 2),
                "Tax": round(tax, 2),
                "Net_Payout": round(net, 2)
            })
