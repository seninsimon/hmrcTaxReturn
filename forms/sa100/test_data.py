# ==========================================
# SA100 TEST DATA
# ==========================================

# Data for SA100 Page 1 (TR1)
DATA_SA100_TR1 = {
    'utr_number': "1234567890",
    'nino': "AB123CD",
    'Employerreference': "1234567890",
    'date': "12122022",
    'dateofbirthday': "12",
    'dateofbirthmonth': "12",
    'dateofbirthyear': "2022",
    'phonenumber': "1234567890000",
    'dateofbirthday2': "12",
    'dateofbirthmonth2': "12",
    'dateofbirthyear2': "2022",
    'NationalInsuranceNumber1': "0",
    'NationalInsuranceNumber2': "0",
    'NationalInsuranceNumber3': "0",
    'NationalInsuranceNumber4': "0",
    'NationalInsuranceNumber5': "0",
    'NationalInsuranceNumber6': "0",
    'NationalInsuranceNumber7': "0",
    'NationalInsuranceNumber8': "0",
    'NationalInsuranceNumber9': "0",

}

# Data for SA100 Page 2 (TR2)
DATA_SA100_TR2 = {
    # ===== Employment =====
    "employmentYes": "X",
    "employmentNo": "X",
    "employmentNumber": "1",

    # mapped codes (added)
    "YTR1_1A": "X",   # employmentYes
    "Q1_1": "X",      # employmentNo
    "YTR1_1B": "1",   # employmentNumber


    # ===== Trusts etc =====
    "trustsEtcYes": "X",
    "trustsEtcNo": "X",


    # ===== Self-employed =====
    "selfEmployedYes": "X",
    "selfEmployedNo": "X",
    "selfEmployedNumber": "1",

    # mapped codes (added)
    "YTR2A_2A": "X",  # selfEmployedYes
    "Q2_1": "X",      # selfEmployedNo
    "YTR2A_2B": "1",  # selfEmployedNumber


    # ===== Capital gains =====
    "capitalGainsTaxSummaryYes": "X",
    "capitalGainsTaxSummaryNo": "X",


    # ===== Computations =====
    "computationsProvidedYes": "X",


    # ===== Residence / remittance =====
    "residenceRemittanceYes": "X",
    "residenceRemittanceNo": "X",


    # ===== Partnership =====
    "partnershipYes": "X",
    "partnershipNo": "X",
    "partnershipNumber": "1",


    # ===== Additional information =====
    "additioanlInformationYes": "X",
    "additioanlInformationNo": "X",


    # ===== UK property =====
    "ukpropertyYes": "X",
    "ukpropertyNo": "X",

    # mapped code (added)
    "YTR4_4A": "X",   # ukpropertyYes


    # ===== Foreign =====
    "foreignYes": "X",
    "foreignNo": "X",


    # ===== Extra pages =====
    "ifYouNeedMorePagesYes": "X",
    "ifYouNeedMorePagesNo": "X",
}

# Data for SA100 Page 3 (TR3)
DATA_SA100_TR3 = {
    # INC1 – taxedUkInterest
    "INC1_0": "0",
    "INC1_1": "0",
    "INC1_2": "0",
    "INC1_3": "0",
    "INC1_4": "0",
    "INC1_5": "0",
    "INC1_6": "0",
    "INC1_7": "0",

    # INC5 – otherDividends
    "INC5_0": "0",
    "INC5_1": "0",
    "INC5_2": "0",
    "INC5_3": "0",
    "INC5_4": "0",
    "INC5_5": "0",
    "INC5_6": "0",
    "INC5_7": "0",

    # INC2 – untaxedUkInterest
    "INC2_0": "0",
    "INC2_1": "0",
    "INC2_2": "0",
    "INC2_3": "0",
    "INC2_4": "0",
    "INC2_5": "0",
    "INC2_6": "0",
    "INC2_7": "0",

    # INC6 – foreignDividends
    "INC6_0": "0",
    "INC6_1": "0",
    "INC6_2": "0",
    "INC6_3": "0",

    # INC3 – untaxedForeignInterest
    "INC3_0": "0",
    "INC3_1": "0",
    "INC3_2": "0",
    "INC3_3": "0",

    # INC7 – taxTakenOffForeignDividends
    "INC7_0": "0",
    "INC7_1": "0",
    "INC7_2": "0",
    "INC7_3": "0",

    # INC4 – dividendsFromUkCompanies
    "INC4_0": "0",
    "INC4_1": "0",
    "INC4_2": "0",
    "INC4_3": "0",
    "INC4_4": "0",
    "INC4_5": "0",
    "INC4_6": "0",
    "INC4_7": "0",

    # INC8 – statePension
    "INC8_0": "0",
    "INC8_1": "0",
    "INC8_2": "0",
    "INC8_3": "0",
    "INC8_4": "0",

    # INC12 – taxTakenOffBox
    "INC12_0": "0",
    "INC12_1": "0",
    "INC12_2": "0",
    "INC12_3": "0",
    "INC12_4": "0",
    "INC12_5": "0",
    "INC12_6": "0",
    "INC12_7": "0",

    # INC9 – statePensionLumpSum
    "INC9_0": "0",
    "INC9_1": "0",
    "INC9_2": "0",
    "INC9_3": "0",
    "INC9_4": "0",

    # INC13 – TaxableIncapacityBenefitandcontribution
    "INC13_0": "0",
    "INC13_1": "0",
    "INC13_2": "0",
    "INC13_3": "0",
    "INC13_4": "0",

    # INC10 – Taxtakenoffbox
    "INC10_0": "0",
    "INC10_1": "0",
    "INC10_2": "0",
    "INC10_3": "0",
    "INC10_4": "0",

    # INC14 – TaxtakenoffIncapacityBenefitinbox
    "INC14_0": "0",
    "INC14_1": "0",
    "INC14_2": "0",
    "INC14_3": "0",
    "INC14_4": "0",

    # INC11 – PensionsotherthanStatePension
    "INC11_0": "0",
    "INC11_1": "0",
    "INC11_2": "0",
    "INC11_3": "0",
    "INC11_4": "0",
    "INC11_5": "0",
    "INC11_6": "0",
    "INC11_7": "0",

    # INC15 – JobseekersAllowance
    "INC15_0": "0",
    "INC15_1": "0",
    "INC15_2": "0",
    "INC15_3": "0",
    "INC15_4": "0",

    # INC16 – TotalofanyothertaxableStatePensionsandbenefits
    "INC16_0": "0",
    "INC16_1": "0",
    "INC16_2": "0",
    "INC16_3": "0",
    "INC16_4": "0",

    # INC17 – Othertaxableincome
    "INC17_0": "0",
    "INC17_1": "0",
    "INC17_2": "0",
    "INC17_3": "0",
    "INC17_4": "0",
    "INC17_5": "0",
    "INC17_6": "0",
    "INC17_7": "0",

    # INC20 – Benefitfrompreownedassets
    "INC20_0": "0",
    "INC20_1": "0",
    "INC20_2": "0",
    "INC20_3": "0",
    "INC20_4": "0",
    "INC20_5": "0",
    "INC20_6": "0",
    "INC20_7": "0",

    # INC18 – Totalamountofallowableexpenses
    "INC18_0": "0",
    "INC18_1": "0",
    "INC18_2": "0",
    "INC18_3": "0",
    "INC18_4": "0",
    "INC18_5": "0",
    "INC18_6": "0",
    "INC18_7": "0",

    # INC19 – Anytaxtakenoffbox17
    "INC19_0": "0",
    "INC19_1": "0",
    "INC19_2": "0",
    "INC19_3": "0",
    "INC19_4": "0",
    "INC19_5": "0",
    "INC19_6": "0",
    "INC19_7": "0",

    # INC21 – Description
    "INC21_0": "aksdbsabd",
}


DATA_SA100_TR4 = {
    # REL1 – Paymentstoregisteredpensionschemes (box 1)
    "REL1_0": "0",
    "REL1_1": "0",
    "REL1_2": "0",
    "REL1_3": "0",
    "REL1_4": "0",
    "REL1_5": "0",
    "REL1_6": "0",
    "REL1_7": "0",

    # REL1_1 – Totalofanyone-offpaymentsinboxone
    "REL1_1_0": "0",
    "REL1_1_1": "0",
    "REL1_1_2": "0",
    "REL1_1_3": "0",
    "REL1_1_4": "0",
    "REL1_1_5": "0",
    "REL1_1_6": "0",
    "REL1_1_7": "0",

    # REL2 – Paymentstoaretirementannuitycontract (box 2)
    "REL2_0": "0",
    "REL2_1": "0",
    "REL2_2": "0",
    "REL2_3": "0",
    "REL2_4": "0",
    "REL2_5": "0",
    "REL2_6": "0",
    "REL2_7": "0",

    # REL5 – GiftAidpaymentsmadeinyearto5April2025 (box 5)
    "REL5_0": "0",
    "REL5_1": "0",
    "REL5_2": "0",
    "REL5_3": "0",
    "REL5_4": "0",
    "REL5_5": "0",
    "REL5_6": "0",
    "REL5_7": "0",

    # REL6 – Totalofanyone-offpaymentsinboxfive (box 6)
    "REL6_0": "0",
    "REL6_1": "0",
    "REL6_2": "0",
    "REL6_3": "0",
    "REL6_4": "0",
    "REL6_5": "0",
    "REL6_6": "0",
    "REL6_7": "0",

    # REL7 – treatedasifmadeintheyearto5April2024 (box 7)
    "REL7_0": "0",
    "REL7_1": "0",
    "REL7_2": "0",
    "REL7_3": "0",
    "REL7_4": "0",
    "REL7_5": "0",
    "REL7_6": "0",
    "REL7_7": "0",

    # REL3 – Paymentstoyouremployersschemewhichwerenotdeducted (box 3)
    "REL3_0": "0",
    "REL3_1": "0",
    "REL3_2": "0",
    "REL3_3": "0",
    "REL3_4": "0",
    "REL3_5": "0",
    "REL3_6": "0",
    "REL3_7": "0",

    # REL4 – Taxreliefsfour (box 4 – overseas pension scheme)
    "REL4_0": "0",
    "REL4_1": "0",
    "REL4_2": "0",
    "REL4_3": "0",
    "REL4_4": "0",
    "REL4_5": "0",
    "REL4_6": "0",
    "REL4_7": "0",

    # REL8 – Taxreliefseight (box 8)
    "REL8_0": "0",
    "REL8_1": "0",
    "REL8_2": "0",
    "REL8_3": "0",
    "REL8_4": "0",
    "REL8_5": "0",
    "REL8_6": "0",
    "REL8_7": "0",

    # REL9 – Taxreliefsnine (box 9 – shares/securities)
    "REL9_0": "0",
    "REL9_1": "0",
    "REL9_2": "0",
    "REL9_3": "0",
    "REL9_4": "0",
    "REL9_5": "0",
    "REL9_6": "0",
    "REL9_7": "0",

    # REL10 – taxreliefsten (box 10 – land/buildings)
    "REL10_0": "0",
    "REL10_1": "0",
    "REL10_2": "0",
    "REL10_3": "0",
    "REL10_4": "0",
    "REL10_5": "0",
    "REL10_6": "0",
    "REL10_7": "0",

    # REL13–16 – single-value boxes
    "REL13": "X",       # registered blind
    "REL15": "X",       # want spouse’s surplus
    "REL16": "X",       # give surplus to spouse
    "REL14": "senin",   # local authority name
}

DATA_SA100_TR5 = {
    # SLR1 – notification from Student Loans
    "SLR1": "X",

    # SLR2 – employer deducted Student Loan
    "SLR2_0": "0",
    "SLR2_1": "0",
    "SLR2_2": "0",
    "SLR2_3": "0",
    "SLR2_4": "0",
    "SLR2_5": "0",
    "SLR2_6": "0",
    "SLR2_7": "0",

    # SLR3 – employer deducted Postgraduate Loan
    "SLR3_0": "0",
    "SLR3_1": "0",
    "SLR3_2": "0",
    "SLR3_3": "0",
    "SLR3_4": "0",
    "SLR3_5": "0",
    "SLR3_6": "0",
    "SLR3_7": "0",

    # CBC1 – total Child Benefit
    "CBC1_0": "0",
    "CBC1_1": "0",
    "CBC1_2": "0",
    "CBC1_3": "0",
    "CBC1_4": "0",

    # CBC2 – number of children
    "CBC2": "12",

    # CBC3 – stopped getting Child Benefit (date)
    "CBC3_0": "10",   # day
    "CBC3_1": "12",   # month
    "CBC3_2": "2024", # year

    # MAT1 & MAT2 – spouse/civil partner name
    "MAT1": "aksdbsabd",   # first name
    "MAT2": "aksdbsabd",   # last name

    # MAT3 – spouse/civil partner NI number
    "MAT3_0": "0",
    "MAT3_1": "0",
    "MAT3_2": "0",
    "MAT3_3": "0",
    "MAT3_4": "0",
    "MAT3_5": "0",
    "MAT3_6": "0",
    "MAT3_7": "0",
    "MAT3_8": "0",

    # MAT4 – spouse/civil partner date of birth
    "MAT4_0": "12",   # day
    "MAT4_1": "12",   # month
    "MAT4_2": "2024", # year

    # MAT5 – date of marriage/civil partnership
    "MAT5_0": "12",   # day
    "MAT5_1": "12",   # month
    "MAT5_2": "2024", # year
}

DATA_SA100_TR6 = {
    # FIN1 – Tax refunded or set off (box 1)
    "FIN1_0": "0",
    "FIN1_1": "0",
    "FIN1_2": "0",
    "FIN1_3": "0",
    "FIN1_4": "0",
    "FIN1_5": "0",
    "FIN1_6": "0",
    "FIN1_7": "0",

    # FIN2 – If you have not paid enough tax (box 2)
    "FIN2": "X",

    # FIN3 – If you have not paid enough tax (box 3)
    "FIN3": "X",

    # FIN4 – Name of bank or building society
    "FIN4": "aksdbsabd",

    # FIN6 – Name of account holder
    "FIN6": "aksdbsabd",

    # FIN5 – Branch sort code (box 6)
    "FIN5_0": "0",
    "FIN5_1": "0",
    "FIN5_2": "0",
    "FIN5_3": "0",
    "FIN5_4": "0",
    "FIN5_5": "0",

    # FIN7 – Account number (box 7)
    "FIN7_0": "0",
    "FIN7_1": "0",
    "FIN7_2": "0",
    "FIN7_3": "0",
    "FIN7_4": "0",
    "FIN7_5": "0",
    "FIN7_6": "0",
    "FIN7_7": "0",

    # FIN8 – Building society reference number (box 8)
    "FIN8_0": "0",
    "FIN8_1": "0",
    "FIN8_2": "0",
    "FIN8_3": "0",
    "FIN8_4": "0",
    "FIN8_5": "0",
    "FIN8_6": "0",
    "FIN8_7": "0",
    "FIN8_8": "0",
    "FIN8_9": "0",
    "FIN8_10": "0",
    "FIN8_11": "0",
    "FIN8_12": "0",
    "FIN8_13": "0",

    # FIN9–11 – nominee / bank declarations
    "FIN9": "X",
    "FIN10": "X",
    "FIN11": "X",

    # FIN12 – Nominee’s address
    "FIN12": "aksdbsabd",

    # FIN13 – postcode
    "FIN13_0": "0",
    "FIN13_1": "0",
    "FIN13_2": "0",
    "FIN13_3": "0",
    "FIN13_4": "0",
    "FIN13_5": "0",
    "FIN13_6": "0",
    "FIN13_7": "0",

    # FIN14 – declaration signature
    "FIN14": "sign",
}

DATA_SA100_TR7 = {
    # FIN15 – Your tax adviser’s name
    "FIN15": "aksdbsabd",

    # FIN16 – Their phone number
    "FIN16_0": "0",
    "FIN16_1": "0",
    "FIN16_2": "0",
    "FIN16_3": "0",
    "FIN16_4": "0",
    "FIN16_5": "0",
    "FIN16_6": "0",
    "FIN16_7": "0",
    "FIN16_8": "0",
    "FIN16_9": "0",
    "FIN16_10": "0",
    "FIN16_11": "0",
    "FIN16_12": "0",
    "FIN16_13": "0",

    # FIN17 – First line of their address including postcode
    "FIN17": "aksdbsabd",

    # FIN18 – Reference your adviser uses for you
    "FIN18_0": "0",
    "FIN18_1": "0",
    "FIN18_2": "0",
    "FIN18_3": "0",
    "FIN18_4": "0",
    "FIN18_5": "0",
    "FIN18_6": "0",
    "FIN18_7": "0",
    "FIN18_8": "0",
    "FIN18_9": "0",
    "FIN18_10": "0",
    "FIN18_11": "0",
    "FIN18_12": "0",
    "FIN18_13": "0",

    # FIN19 – Any other information
    "FIN19": "aksdbsabd",
}

DATA_SA100_TR8 = {

   "FIN20": "X",

   "FIN21": "X",



   "FIN23": "Xasdasd",

   "FIN24": "aksdbsabd",

   "FIN25": "aksdbsabd",

   "FIN26": "aksdbsabd",
}
