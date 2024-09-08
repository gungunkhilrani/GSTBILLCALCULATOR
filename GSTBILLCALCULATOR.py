from typing import final

print("Welcome To GST Bill Calculator")
bill = float(input("Enter The Amount Of Your Bill : ₹ "))
Gst = int(input("Enter Gst Percentage on Your Bill  : "))
people = int(input("Enter The No. Of People You Want to Split The Bill With : "))

Gst_as_percent = Gst/100
bill_after = Gst_as_percent * bill
Total_bill = bill_after + bill
bill_per_person = Total_bill/ people
final_amount = round(bill_per_person,2)
print(f"Amount To Be Paid By Each Person : {final_amount}")
