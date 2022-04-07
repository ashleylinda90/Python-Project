# Project: Sprint Week 2 Program
# Programmers: Ashley Fillmore, Gerald Bartlett, Michael O'Reilly and John Byrne
# Date: July 30, 2021

# Ashley and Gerald did the majority of the coding, Mike and John helped with the 2 extra required functions and
# read through the whole program multiple times to check for any errors we may have missed, gave opinions and ran
# through the program a few times as well.

# import datetime

import datetime

# Today's date

Date = datetime.date.today()

# Choice 1: Employee Travel Claim - a program to process salesperson travel claims when they return from a business trip.

def EmpTravelClaim():

# Open a defaults file called TCDef.dat with default values

    f = open("TCDef.dat", "r")

    CLAIM_NUM = int(f.readline())
    HST_RATE = float(f.readline())
    PERDIEM_LOW = float(f.readline())
    PERDIEM_HIGH = float(f.readline())
    MILEAGE_RATE = float(f.readline())
    RENTAL_RATE = float(f.readline())

    f.close()

    print()

# Write variables and inputs for Choice 1

    EmpNum = int(input("Enter Employee Number (END to Quit): "))

# Write an if statement to exit the code if user types "END" for EmpNum

    if EmpNum == "END":
        print("Thank You For Your Business!")
        exit(0)

    EmpName = input("Enter Name: ").title()
    TripLoc = input("Enter Trip Location: ").title()
    StartDate = input("Enter Start Date (YYYY-MM-DD): ")
    EndDate = input("Enter End Date (YYYY-MM-DD): ")

# Format the start and end dates

    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    StartDateStr = StartDate.date()
    EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
    EndDateStr = EndDate.date()

    NumDays = (EndDate - StartDate).days

    Car = input("Was Vehicle Owned or Rented? (O/R): ").upper()

# Print statements for inputs

    print()
    print("Claim Number:   {:<10}    Employee Number:  {}".format(CLAIM_NUM, EmpNum))
    print()
    print("Start Date:     {}    Employee Name:    {}".format(StartDateStr, EmpName))
    print("End Date:       {}    Trip Location:    {}".format(EndDateStr, TripLoc))
    print("Number of Days: {:<10}    Rental/Owned:     {}".format(NumDays, Car))

# Calculations

    PerDiem = 0
    MileageAmt = 0
    TotKM = 0
    DayRate = 0

    if NumDays <= 3:
        PerDiem = NumDays * PERDIEM_LOW

    else:
        PerDiem = NumDays * PERDIEM_HIGH

    if Car == "O":
        TotKM = int(input("Enter Total KMs Travelled: "))
        print("Total Kilometres: {}".format(TotKM))
        MileageAmt = MILEAGE_RATE * TotKM
        print("Mileage Amount: ".format(MileageAmt))

    elif Car == "R":
        MileageAmt = NumDays * RENTAL_RATE
        print(" " * 30 + "Rental Cost:      ${:,.2f}".format(MileageAmt))

    ClaimAmt = PerDiem + MileageAmt
    HST = PerDiem * HST_RATE
    ClaimTotal = ClaimAmt + HST

# One of two other functions required - function for formatting per diem, claim amt, hst and claim total as dollar amounts

    def DollarFormat(x):

        format = "${:,.2f}".format(x)
        return format

    print("Per Diem Amount: ", DollarFormat(PerDiem))
    print("Claim Amount:    ", DollarFormat(ClaimAmt))
    print("HST Amount:      ", DollarFormat(HST))
    print("Claim Total:     ", DollarFormat(ClaimTotal))

# Claim Number to increase by 1

    CLAIM_NUM += 1

# Create an append file called Claims.dat with input values and calculations

    f = open("Claims.dat", "a")

    f.write("{}, ".format(CLAIM_NUM))
    f.write("{}, ".format(str(EmpNum)))
    f.write("{}, ".format(str(EmpName)))
    f.write("{}, ".format(str(TripLoc)))
    f.write("{}, ".format(str(StartDateStr)))
    f.write("{}, ".format(str(EndDateStr)))
    f.write("{}, ".format(str(NumDays)))
    f.write("{}, ".format(str(Car)))
    f.write("{}, ".format(str(TotKM)))
    f.write("{}, ".format(str(PerDiem)))
    f.write("{}, ".format(str(MileageAmt)))
    f.write("{}, ".format(str(ClaimAmt)))
    f.write("{}, ".format(str(HST)))
    f.write("{}\n".format(str(ClaimTotal)))

    f.close()

# Print message that says data was saved to file

    print()
    print("Data successfully saved to the Claims.dat file.")
    print()

# Write the current values back to the TCDef.dat file

    f = open("TCDef.dat", "w")

    f.write("{}\n".format(str(CLAIM_NUM)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(PERDIEM_LOW)))
    f.write("{}\n".format(str(PERDIEM_HIGH)))
    f.write("{}\n".format(str(MILEAGE_RATE)))
    f.write("{}\n".format(str(RENTAL_RATE)))

    f.close()

# Choice 2: Edit System Default Values - read and update the values from the defaults table.

def EditValues():

# Open TCDef.dat file to read the lines

    f = open("TCDef.dat", "r")

    lines = f.readlines()

    f.close()

    CLAIM_NUM = lines[0]
    HSTRate = float(lines[1])
    PerDiemLow = float(lines[2])
    PerDiemHigh = float(lines[3])
    MileageRate = float(lines[4])
    RentalRate = float(lines[5])

# Print statements for the values in TCDef.dat

    print("NL CHOCOLATE COMPANY")
    print("Edit System Default Values")
    print()
    print("Claim Number:          {:<15}".format(CLAIM_NUM))
    print("HST Rate:             ${:,.2f}".format(HSTRate))
    print("Per Diem Low Rate:   ${:,.2f}".format(PerDiemLow))
    print("Per Diem High Rate:  ${:,.2f}".format(PerDiemHigh))
    print("Mileage Rate:         ${:,.2f}".format(MileageRate))
    print("Rental Rate:         ${:,.2f}".format(RentalRate))
    print()

# Write inputs and if statements for user to be able to change or not change the values in TCDef.dat

    ChangeValue = input("Would You Like to Change Any Values in the TCDef.dat File? (Y/N): ").upper()

    if ChangeValue.upper() == "N":
        print()
        print("No Updates Have Been Made to the Default Values at This Time.")

    elif ChangeValue.upper() == "Y":
        ChangeClaimNum = input("Would You Like to Change the Claim Number in the File? (Y/N): ").upper()
        if ChangeClaimNum.upper() == "Y":
            CLAIM_NUM = int(input("Please Choose a New Value for Claim Number: "))

        ChangeHSTRate = input("Would You Like to Change the HST Rate in the File? (Y/N): ").upper()
        if ChangeHSTRate.upper() == "Y":
            HSTRate = float(input("Please Choose a New Value for HST Rate: "))

        ChangePerDiemLowRate = input("Would You Like to Change the Per Diem Low Rate in the File? (Y/N): ").upper()
        if ChangePerDiemLowRate.upper() == "Y":
            PerDiemLow = float(input("Please Choose a New Value for Per Diem Low Rate: "))

        ChangePerDiemHighRate = input("Would You Like to Change the Per Diem High Rate in the File? (Y/N): ").upper()
        if ChangePerDiemHighRate.upper() == "Y":
            PerDiemHigh = float(input("Please Choose a New Value for Per Diem High Rate: "))

        ChangeMileageRate = input("Would You Like to Change the Mileage Rate in the File? (Y/N): ").upper()
        if ChangeMileageRate.upper() == "Y":
            MileageRate = float(input("Please Choose a New Value for Mileage Rate: "))

        ChangeRentalRate = input("Would You Like to Change the Rental Rate in the File? (Y/N): ").upper()
        if ChangeRentalRate.upper() == "Y":
            RentalRate = float(input("Please Choose a New Value for Rental Rate: "))

        else:
            print("Must Choose Either 'Y' or 'N'. Please Re-Enter: ")

# Open TCDef.dat file to overwrite the original default values if user changes any

        f = open("TCDef.dat", "w")

        f.write("{}\n".format(CLAIM_NUM))
        f.write("{}\n".format(HSTRate))
        f.write("{}\n".format(PerDiemLow))
        f.write("{}\n".format(PerDiemHigh))
        f.write("{}\n".format(MileageRate))
        f.write("{}\n".format(RentalRate))

# Print statements to show updated default values

        print()
        print("DEFAULT VALUES SUCCESSFULLY UPDATED.")
        print()
        print("Claim Number:        {}".format(CLAIM_NUM))
        print("HST Rate:           ${:,.2f}".format(HSTRate))
        print("Per Diem Low Rate:  ${:,.2f}".format(PerDiemLow))
        print("Per Diem High Rate: ${:,.2f}".format(PerDiemHigh))
        print("Mileage Rate:       ${:,.2f}".format(MileageRate))
        print("Rental Rate:        ${:,.2f}".format(RentalRate))
        print()

# User can press any key to continue

        Continue = input("Press Any Key to Continue: ")

        f.close()

# Else statement if user does not type Y or N

    else:
        print("You Must Choose Y or N. Please Re-Enter: ")

# Choice 3: Print Travel Claim Report - process the Claims.dat file and generate the report.

def ClaimReport():

# Print statements to output report headings

    print()
    print("         1         2         3         4         5         6         7         8         9")
    print("1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890")
    print()
    print("                                        NL CHOCOLATE COMPANY")  # NOTE - in the document, the report heading was Smackers, but we used NL Chocolate Company as that's the company named at the beginning.
    print()
    print(f"                               TRAVEL CLAIMS LISTING AS OF {Date}")
    print()
    print("  CLAIM      CLAIM       SALESPERSON           CLAIM           PER DIEM       MILEAGE       CLAIM")
    print("  NUMBER     DATE           NAME              LOCATION          AMOUNT        AMOUNT        AMOUNT")
    print("=" * 101)

# Open Claims.dat file to read the lines

    f = open("Claims.dat", "r")

# Define Claim Counter

    ClaimCtr = 0
    PerDiemAcc = 0
    MileageAcc = 0
    ClaimAmtAcc = 0

# for statement for Claims Lines in 'f'

    for ClaimsDataLine in f:

        ClaimsLine = ClaimsDataLine.split(",")

        CLAIM_NUM = ClaimsLine[0]
        StartDateStr = ClaimsLine[4]
        EmpName = ClaimsLine[2]
        TripLoc = ClaimsLine[3]
        PerDiem = float(ClaimsLine[9])
        MileageAmt = float(ClaimsLine[10])
        ClaimAmt = float(ClaimsLine[11].strip())

# Print statement for values in report

        print("  {:<5}  {}   {:<18}    {:<13}     ${:<8,.2f}      ${:<8,.2f}    ${:<10,.2f} ".format(CLAIM_NUM, StartDateStr, EmpName, TripLoc, PerDiem, MileageAmt, ClaimAmt))

# Claim Counter increases by 1

        ClaimCtr += 1
        PerDiemAcc += PerDiem
        MileageAcc += MileageAmt
        ClaimAmtAcc += ClaimAmt

    f.close()

# Print statements for listed claims

    print("=" * 101)
    print("{} Claims Listed                                               ${:<10,.2f}   ${:<10,.2f}   ${:<10,.2f}".format(ClaimCtr, PerDiemAcc, MileageAcc, ClaimAmtAcc))
    print()
    print(" " * 45 + "END OF REPORT")

# Choice 4: Graph Monthly Claim Totals - use MatPlotLib to produce a line graph indicating total sales for each month.

def MatPlot():

    import matplotlib.pyplot as plt

    import csv

    x = []
    y = []

# Open Defaults.dat to read values

    with open('Defaults.dat', 'r') as csvfile:

        plots = csv.reader(csvfile, delimiter=',')

        for row in plots:
            x.append(row[0]) # dates
            y.append(row[1]) # totals

# plt to show info/colors on graph

    plt.plot(x, y, label='Monthly Totals!')
    plt.xlabel('Months', color='blue')
    plt.ylabel('Claims', color='red')
    plt.title('NL CHOCOLATE COMPANY TRAVEL CLAIMS', color='red')
    plt.legend()
    plt.show()

# Two of two other required functions - function to give Maurice a little surprise

def Surprise():

    f = open("DoNotOpen.dat", "r")
    x = f.read()

    print(x)

    f.close()

# Write while true loop for print statements and if statements for user choices

while True:

    print()
    print("NL Chocolate Company")
    print("Travel Claims Processing System")
    print()
    print("1. Enter an Employee Travel Claim.")
    print("2. Edit System Default Values.")
    print("3. Print the Travel Claim Report.")
    print("4. Graph Monthly Claim Totals.")
    print("5. Quit Program.")
    print("6. Pick 6 For a Surprise!")
    print()
    Choice = int(input("   Enter Choice (1-6): "))
    print()

# Validate input to allow only 1 - 5

    if Choice <= 0:
        print("Choice Must Be 1-5. Please Re-Enter: ")
    elif Choice >= 7:
        print("Choice Must Be 1-5. Please Re-Enter: ")

# Write if statements for all choices

    if Choice == 1:
        EmpTravelClaim()
    if Choice == 2:
        EditValues()
    if Choice == 3:
        ClaimReport()
    if Choice == 4:
        MatPlot()
    if Choice == 5:
        print("Thank You, Have a Nice Day!")
        break
    if Choice == 6:
        Surprise()









