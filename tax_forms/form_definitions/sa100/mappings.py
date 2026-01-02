# ==========================================
# SA100 FORM COORDINATE MAPPINGS
# ==========================================

SA100_TR1 = {
    'utr_number': {
        'x': 91,
        'y': 735,
        'type': 'text'
    },
    'nino': {
        'x': 91,
        'y': 722,
        'type': 'text'
    },
    'Employerreference': {
        'x': 148,
        'y': 710,
        'type': 'text'
    },
    'date': {
        'x': 148,
        'y': 688,
        'type': 'text'
    },
    'dateofbirthday': {
        'x': 68,
        'y': 134,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'dateofbirthmonth': {
        'x': 106,
        'y': 134,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'dateofbirthyear': {
        'x': 142,
        'y': 134,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },
    'phonenumber': {
        'x': 323,
        'y': 146,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },
    'dateofbirthday2': {
        'x': 70,
        'y': 47,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'dateofbirthmonth2': {
        'x': 106,
        'y': 47,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'dateofbirthyear2': {
        'x': 142,
        'y': 47,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },
    'NationalInsuranceNumber1': {
        'x': 326,
        'y': 85,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'NationalInsuranceNumber2': {
        'x': 364,
        'y': 85,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'NationalInsuranceNumber3': {
        'x': 398,
        'y': 85,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },
    'NationalInsuranceNumber4': {
        'x': 442,
        'y': 85,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    'NationalInsuranceNumber5': {
        'x': 480,
        'y': 85,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
}

SA100_TR2 = {
    # ===== Employment =====
    'employmentYes': {'x': 90, 'y': 599, 'type': 'text'},
    'employmentNo': {'x': 142, 'y': 599, 'type': 'text'},
    'employmentNumber': {'x': 212, 'y': 599, 'type': 'text'},

    # mapped codes (added)
    'YTR1_1A': {'x': 90, 'y': 599, 'type': 'text'},   # employmentYes
    'Q1_1': {'x': 142, 'y': 599, 'type': 'text'},     # employmentNo
    'YTR1_1B': {'x': 212, 'y': 599, 'type': 'text'},  # employmentNumber


    # ===== Trusts etc =====
    'trustsEtcYes': {'x': 350, 'y': 632, 'type': 'text'},
    'trustsEtcNo': {'x': 402, 'y': 632, 'type': 'text'},


    # ===== Self-employed =====
    'selfEmployedYes': {'x': 90, 'y': 430, 'type': 'text'},
    'selfEmployedNo': {'x': 142, 'y': 430, 'type': 'text'},
    'selfEmployedNumber': {'x': 212, 'y': 430, 'type': 'text'},

    # mapped codes (added)
    'YTR2A_2A': {'x': 90, 'y': 430, 'type': 'text'},   # selfEmployedYes
    'Q2_1': {'x': 142, 'y': 430, 'type': 'text'},     # selfEmployedNo
    'YTR2A_2B': {'x': 212, 'y': 430, 'type': 'text'}, # selfEmployedNumber


    # ===== Capital gains =====
    'capitalGainsTaxSummaryYes': {'x': 349, 'y': 497, 'type': 'text'},
    'capitalGainsTaxSummaryNo': {'x': 402, 'y': 497, 'type': 'text'},


    # ===== Computations =====
    'computationsProvidedYes': {'x': 534, 'y': 497, 'type': 'text'},


    # ===== Residence / remittance =====
    'residenceRemittanceYes': {'x': 350, 'y': 375, 'type': 'text'},
    'residenceRemittanceNo': {'x': 402, 'y': 375, 'type': 'text'},


    # ===== Partnership =====
    'partnershipYes': {'x': 90, 'y': 338, 'type': 'text'},
    'partnershipNo': {'x': 142, 'y': 338, 'type': 'text'},
    'partnershipNumber': {'x': 212, 'y': 338, 'type': 'text'},


    # ===== Additional information =====
    'additioanlInformationYes': {'x': 350, 'y': 250, 'type': 'text'},
    'additioanlInformationNo': {'x': 402, 'y': 250, 'type': 'text'},


    # ===== UK property =====
    'ukpropertyYes': {'x': 92, 'y': 224, 'type': 'text'},
    'ukpropertyNo': {'x': 142, 'y': 224, 'type': 'text'},

    # mapped code (added)
    'YTR4_4A': {'x': 92, 'y': 224, 'type': 'text'},   # ukpropertyYes


    # ===== Foreign =====
    'foreignYes': {'x': 91, 'y': 58, 'type': 'text'},
    'foreignNo': {'x': 142, 'y': 58, 'type': 'text'},


    # ===== Extra pages =====
    'ifYouNeedMorePagesYes': {'x': 350, 'y': 125, 'type': 'text'},
    'ifYouNeedMorePagesNo': {'x': 402, 'y': 125, 'type': 'text'},
}


SA100_TR3 = {
    # INC1 – taxedUkInterest
    'INC1_0': {'x': 85, 'y': 693, 'type': 'text'},
    'INC1_1': {'x': 100, 'y': 693, 'type': 'text'},
    'INC1_2': {'x': 115, 'y': 693, 'type': 'text'},
    'INC1_3': {'x': 130, 'y': 693, 'type': 'text'},
    'INC1_4': {'x': 148, 'y': 693, 'type': 'text'},
    'INC1_5': {'x': 163, 'y': 693, 'type': 'text'},
    'INC1_6': {'x': 179, 'y': 693, 'type': 'text'},
    'INC1_7': {'x': 195, 'y': 693, 'type': 'text'},

    # INC5 – otherDividends
    'INC5_0': {'x': 345, 'y': 707, 'type': 'text'},
    'INC5_1': {'x': 362, 'y': 707, 'type': 'text'},
    'INC5_2': {'x': 378, 'y': 707, 'type': 'text'},
    'INC5_3': {'x': 390, 'y': 707, 'type': 'text'},
    'INC5_4': {'x': 405, 'y': 707, 'type': 'text'},
    'INC5_5': {'x': 423, 'y': 707, 'type': 'text'},
    'INC5_6': {'x': 438, 'y': 707, 'type': 'text'},
    'INC5_7': {'x': 455, 'y': 707, 'type': 'text'},

    # INC2 – untaxedUkInterest
    'INC2_0': {'x': 82, 'y': 636, 'type': 'text'},
    'INC2_1': {'x': 100, 'y': 636, 'type': 'text'},
    'INC2_2': {'x': 115, 'y': 636, 'type': 'text'},
    'INC2_3': {'x': 130, 'y': 636, 'type': 'text'},
    'INC2_4': {'x': 148, 'y': 636, 'type': 'text'},
    'INC2_5': {'x': 163, 'y': 636, 'type': 'text'},
    'INC2_6': {'x': 179, 'y': 636, 'type': 'text'},
    'INC2_7': {'x': 195, 'y': 636, 'type': 'text'},

    # INC6 – foreignDividends
    'INC6_0': {'x': 342, 'y': 636, 'type': 'text'},
    'INC6_1': {'x': 360, 'y': 636, 'type': 'text'},
    'INC6_2': {'x': 374, 'y': 636, 'type': 'text'},
    'INC6_3': {'x': 390, 'y': 636, 'type': 'text'},

    # INC3 – untaxedForeignInterest
    'INC3_0': {'x': 82, 'y': 580, 'type': 'text'},
    'INC3_1': {'x': 100, 'y': 580, 'type': 'text'},
    'INC3_2': {'x': 115, 'y': 580, 'type': 'text'},
    'INC3_3': {'x': 130, 'y': 580, 'type': 'text'},

    # INC7 – taxTakenOffForeignDividends
    'INC7_0': {'x': 342, 'y': 592, 'type': 'text'},
    'INC7_1': {'x': 360, 'y': 592, 'type': 'text'},
    'INC7_2': {'x': 374, 'y': 592, 'type': 'text'},
    'INC7_3': {'x': 390, 'y': 592, 'type': 'text'},

    # INC4 – dividendsFromUkCompanies
    'INC4_0': {'x': 82, 'y': 520, 'type': 'text'},
    'INC4_1': {'x': 100, 'y': 520, 'type': 'text'},
    'INC4_2': {'x': 115, 'y': 520, 'type': 'text'},
    'INC4_3': {'x': 130, 'y': 520, 'type': 'text'},
    'INC4_4': {'x': 148, 'y': 520, 'type': 'text'},
    'INC4_5': {'x': 163, 'y': 520, 'type': 'text'},
    'INC4_6': {'x': 179, 'y': 520, 'type': 'text'},
    'INC4_7': {'x': 195, 'y': 520, 'type': 'text'},

    # INC8 – statePension
    'INC8_0': {'x': 82, 'y': 433, 'type': 'text'},
    'INC8_1': {'x': 100, 'y': 433, 'type': 'text'},
    'INC8_2': {'x': 115, 'y': 433, 'type': 'text'},
    'INC8_3': {'x': 130, 'y': 433, 'type': 'text'},
    'INC8_4': {'x': 148, 'y': 433, 'type': 'text'},

    # INC12 – taxTakenOffBox
    'INC12_0': {'x': 358, 'y': 447, 'type': 'text'},
    'INC12_1': {'x': 376, 'y': 447, 'type': 'text'},
    'INC12_2': {'x': 390, 'y': 447, 'type': 'text'},
    'INC12_3': {'x': 407, 'y': 447, 'type': 'text'},
    'INC12_4': {'x': 422, 'y': 447, 'type': 'text'},
    'INC12_5': {'x': 438, 'y': 447, 'type': 'text'},
    'INC12_6': {'x': 455, 'y': 447, 'type': 'text'},
    'INC12_7': {'x': 468, 'y': 447, 'type': 'text'},

    # INC9 – statePensionLumpSum
    'INC9_0': {'x': 82, 'y': 375, 'type': 'text'},
    'INC9_1': {'x': 100, 'y': 375, 'type': 'text'},
    'INC9_2': {'x': 115, 'y': 375, 'type': 'text'},
    'INC9_3': {'x': 130, 'y': 375, 'type': 'text'},
    'INC9_4': {'x': 148, 'y': 375, 'type': 'text'},

    # INC13 – TaxableIncapacityBenefitandcontribution
    'INC13_0': {'x': 342, 'y': 389, 'type': 'text'},
    'INC13_1': {'x': 360, 'y': 389, 'type': 'text'},
    'INC13_2': {'x': 374, 'y': 389, 'type': 'text'},
    'INC13_3': {'x': 390, 'y': 389, 'type': 'text'},
    'INC13_4': {'x': 405, 'y': 389, 'type': 'text'},

    # INC10 – Taxtakenoffbox
    'INC10_0': {'x': 82, 'y': 331, 'type': 'text'},
    'INC10_1': {'x': 100, 'y': 331, 'type': 'text'},
    'INC10_2': {'x': 115, 'y': 331, 'type': 'text'},
    'INC10_3': {'x': 130, 'y': 331, 'type': 'text'},
    'INC10_4': {'x': 148, 'y': 331, 'type': 'text'},

    # INC14 – TaxtakenoffIncapacityBenefitinbox
    'INC14_0': {'x': 342, 'y': 345, 'type': 'text'},
    'INC14_1': {'x': 360, 'y': 345, 'type': 'text'},
    'INC14_2': {'x': 374, 'y': 345, 'type': 'text'},
    'INC14_3': {'x': 390, 'y': 345, 'type': 'text'},
    'INC14_4': {'x': 405, 'y': 345, 'type': 'text'},

    # INC11 – PensionsotherthanStatePension
    'INC11_0': {'x': 83, 'y': 262, 'type': 'text'},
    'INC11_1': {'x': 100, 'y': 262, 'type': 'text'},
    'INC11_2': {'x': 115, 'y': 262, 'type': 'text'},
    'INC11_3': {'x': 130, 'y': 262, 'type': 'text'},
    'INC11_4': {'x': 148, 'y': 262, 'type': 'text'},
    'INC11_5': {'x': 163, 'y': 262, 'type': 'text'},
    'INC11_6': {'x': 179, 'y': 262, 'type': 'text'},
    'INC11_7': {'x': 195, 'y': 262, 'type': 'text'},

    # INC15 – JobseekersAllowance
    'INC15_0': {'x': 342, 'y': 300, 'type': 'text'},
    'INC15_1': {'x': 360, 'y': 300, 'type': 'text'},
    'INC15_2': {'x': 374, 'y': 300, 'type': 'text'},
    'INC15_3': {'x': 390, 'y': 300, 'type': 'text'},
    'INC15_4': {'x': 405, 'y': 300, 'type': 'text'},

    # INC16 – TotalofanyothertaxableStatePensionsandbenefits
    'INC16_0': {'x': 342, 'y': 254, 'type': 'text'},
    'INC16_1': {'x': 360, 'y': 254, 'type': 'text'},
    'INC16_2': {'x': 374, 'y': 254, 'type': 'text'},
    'INC16_3': {'x': 390, 'y': 254, 'type': 'text'},
    'INC16_4': {'x': 405, 'y': 254, 'type': 'text'},

    # INC17 – Othertaxableincome
    'INC17_0': {'x': 83, 'y': 136, 'type': 'text'},
    'INC17_1': {'x': 100, 'y': 136, 'type': 'text'},
    'INC17_2': {'x': 115, 'y': 136, 'type': 'text'},
    'INC17_3': {'x': 130, 'y': 136, 'type': 'text'},
    'INC17_4': {'x': 148, 'y': 136, 'type': 'text'},
    'INC17_5': {'x': 163, 'y': 136, 'type': 'text'},
    'INC17_6': {'x': 179, 'y': 136, 'type': 'text'},
    'INC17_7': {'x': 195, 'y': 136, 'type': 'text'},

    # INC20 – Benefitfrompreownedassets
    'INC20_0': {'x': 342, 'y': 149, 'type': 'text'},
    'INC20_1': {'x': 360, 'y': 149, 'type': 'text'},
    'INC20_2': {'x': 374, 'y': 149, 'type': 'text'},
    'INC20_3': {'x': 390, 'y': 149, 'type': 'text'},
    'INC20_4': {'x': 405, 'y': 149, 'type': 'text'},
    'INC20_5': {'x': 422, 'y': 149, 'type': 'text'},
    'INC20_6': {'x': 438, 'y': 149, 'type': 'text'},
    'INC20_7': {'x': 455, 'y': 149, 'type': 'text'},

    # INC18 – Totalamountofallowableexpenses
    'INC18_0': {'x': 83, 'y': 92, 'type': 'text'},
    'INC18_1': {'x': 100, 'y': 92, 'type': 'text'},
    'INC18_2': {'x': 115, 'y': 92, 'type': 'text'},
    'INC18_3': {'x': 130, 'y': 92, 'type': 'text'},
    'INC18_4': {'x': 148, 'y': 92, 'type': 'text'},
    'INC18_5': {'x': 163, 'y': 92, 'type': 'text'},
    'INC18_6': {'x': 179, 'y': 92, 'type': 'text'},
    'INC18_7': {'x': 195, 'y': 92, 'type': 'text'},

    # INC19 – Anytaxtakenoffbox17
    'INC19_0': {'x': 83, 'y': 47, 'type': 'text'},
    'INC19_1': {'x': 100, 'y': 47, 'type': 'text'},
    'INC19_2': {'x': 115, 'y': 47, 'type': 'text'},
    'INC19_3': {'x': 130, 'y': 47, 'type': 'text'},
    'INC19_4': {'x': 148, 'y': 47, 'type': 'text'},
    'INC19_5': {'x': 163, 'y': 47, 'type': 'text'},
    'INC19_6': {'x': 179, 'y': 47, 'type': 'text'},
    'INC19_7': {'x': 195, 'y': 47, 'type': 'text'},

    # INC21 – Description
    'INC21_0': {'x': 329, 'y': 83, 'type': 'text'},
}


SA100_TR4 = {
    # REL1 – Paymentstoregisteredpensionschemes
    'REL1_0': {'x': 82, 'y': 629, 'type': 'text'},
    'REL1_1': {'x': 100, 'y': 629, 'type': 'text'},
    'REL1_2': {'x': 115, 'y': 629, 'type': 'text'},
    'REL1_3': {'x': 130, 'y': 629, 'type': 'text'},
    'REL1_4': {'x': 148, 'y': 629, 'type': 'text'},
    'REL1_5': {'x': 163, 'y': 629, 'type': 'text'},
    'REL1_6': {'x': 179, 'y': 629, 'type': 'text'},
    'REL1_7': {'x': 195, 'y': 629, 'type': 'text'},

    # REL1_1 – Totalofanyone-offpaymentsinboxone
    'REL1_1_0': {'x': 82, 'y': 586, 'type': 'text'},
    'REL1_1_1': {'x': 100, 'y': 586, 'type': 'text'},
    'REL1_1_2': {'x': 115, 'y': 586, 'type': 'text'},
    'REL1_1_3': {'x': 130, 'y': 586, 'type': 'text'},
    'REL1_1_4': {'x': 148, 'y': 586, 'type': 'text'},
    'REL1_1_5': {'x': 163, 'y': 586, 'type': 'text'},
    'REL1_1_6': {'x': 179, 'y': 586, 'type': 'text'},
    'REL1_1_7': {'x': 195, 'y': 586, 'type': 'text'},

    # REL2 – Paymentstoaretirementannuitycontract
    'REL2_0': {'x': 82, 'y': 521, 'type': 'text'},
    'REL2_1': {'x': 100, 'y': 521, 'type': 'text'},
    'REL2_2': {'x': 115, 'y': 521, 'type': 'text'},
    'REL2_3': {'x': 130, 'y': 521, 'type': 'text'},
    'REL2_4': {'x': 148, 'y': 521, 'type': 'text'},
    'REL2_5': {'x': 163, 'y': 521, 'type': 'text'},
    'REL2_6': {'x': 179, 'y': 521, 'type': 'text'},
    'REL2_7': {'x': 195, 'y': 521, 'type': 'text'},

    # REL5 – GiftAidpaymentsmadeinyearto5April2025
    'REL5_0': {'x': 82, 'y': 440, 'type': 'text'},
    'REL5_1': {'x': 100, 'y': 440, 'type': 'text'},
    'REL5_2': {'x': 115, 'y': 440, 'type': 'text'},
    'REL5_3': {'x': 130, 'y': 440, 'type': 'text'},
    'REL5_4': {'x': 148, 'y': 440, 'type': 'text'},
    'REL5_5': {'x': 163, 'y': 440, 'type': 'text'},
    'REL5_6': {'x': 179, 'y': 440, 'type': 'text'},
    'REL5_7': {'x': 195, 'y': 440, 'type': 'text'},

    # REL6 – Totalofanyone-offpaymentsinboxfive
    'REL6_0': {'x': 82, 'y': 389, 'type': 'text'},
    'REL6_1': {'x': 100, 'y': 389, 'type': 'text'},
    'REL6_2': {'x': 115, 'y': 389, 'type': 'text'},
    'REL6_3': {'x': 130, 'y': 389, 'type': 'text'},
    'REL6_4': {'x': 148, 'y': 389, 'type': 'text'},
    'REL6_5': {'x': 163, 'y': 389, 'type': 'text'},
    'REL6_6': {'x': 179, 'y': 389, 'type': 'text'},
    'REL6_7': {'x': 195, 'y': 389, 'type': 'text'},

    # REL7 – treatedasifmadeintheyearto5April2024
    'REL7_0': {'x': 82, 'y': 328, 'type': 'text'},
    'REL7_1': {'x': 100, 'y': 328, 'type': 'text'},
    'REL7_2': {'x': 115, 'y': 328, 'type': 'text'},
    'REL7_3': {'x': 130, 'y': 328, 'type': 'text'},
    'REL7_4': {'x': 148, 'y': 328, 'type': 'text'},
    'REL7_5': {'x': 163, 'y': 328, 'type': 'text'},
    'REL7_6': {'x': 179, 'y': 328, 'type': 'text'},
    'REL7_7': {'x': 195, 'y': 328, 'type': 'text'},

    # REL3 – Paymentstoyouremployersschemewhichwerenotdeducted
    'REL3_0': {'x': 344, 'y': 642, 'type': 'text'},
    'REL3_1': {'x': 360, 'y': 642, 'type': 'text'},
    'REL3_2': {'x': 374, 'y': 642, 'type': 'text'},
    'REL3_3': {'x': 390, 'y': 642, 'type': 'text'},
    'REL3_4': {'x': 405, 'y': 642, 'type': 'text'},
    'REL3_5': {'x': 422, 'y': 642, 'type': 'text'},
    'REL3_6': {'x': 438, 'y': 642, 'type': 'text'},
    'REL3_7': {'x': 455, 'y': 642, 'type': 'text'},

    # REL4 – Taxreliefsfour
    'REL4_0': {'x': 344, 'y': 564, 'type': 'text'},
    'REL4_1': {'x': 360, 'y': 564, 'type': 'text'},
    'REL4_2': {'x': 374, 'y': 564, 'type': 'text'},
    'REL4_3': {'x': 390, 'y': 564, 'type': 'text'},
    'REL4_4': {'x': 405, 'y': 564, 'type': 'text'},
    'REL4_5': {'x': 422, 'y': 564, 'type': 'text'},
    'REL4_6': {'x': 438, 'y': 564, 'type': 'text'},
    'REL4_7': {'x': 455, 'y': 564, 'type': 'text'},

    # REL8 – Taxreliefseight
    'REL8_0': {'x': 344, 'y': 428, 'type': 'text'},
    'REL8_1': {'x': 360, 'y': 428, 'type': 'text'},
    'REL8_2': {'x': 374, 'y': 428, 'type': 'text'},
    'REL8_3': {'x': 390, 'y': 428, 'type': 'text'},
    'REL8_4': {'x': 405, 'y': 428, 'type': 'text'},
    'REL8_5': {'x': 422, 'y': 428, 'type': 'text'},
    'REL8_6': {'x': 438, 'y': 428, 'type': 'text'},
    'REL8_7': {'x': 455, 'y': 428, 'type': 'text'},

    # REL9 – Taxreliefsnine
    'REL9_0': {'x': 344, 'y': 378, 'type': 'text'},
    'REL9_1': {'x': 360, 'y': 378, 'type': 'text'},
    'REL9_2': {'x': 374, 'y': 378, 'type': 'text'},
    'REL9_3': {'x': 390, 'y': 378, 'type': 'text'},
    'REL9_4': {'x': 405, 'y': 378, 'type': 'text'},
    'REL9_5': {'x': 422, 'y': 378, 'type': 'text'},
    'REL9_6': {'x': 438, 'y': 378, 'type': 'text'},
    'REL9_7': {'x': 455, 'y': 378, 'type': 'text'},

    # REL10 – taxreliefsten
    'REL10_0': {'x': 344, 'y': 328, 'type': 'text'},
    'REL10_1': {'x': 360, 'y': 328, 'type': 'text'},
    'REL10_2': {'x': 374, 'y': 328, 'type': 'text'},
    'REL10_3': {'x': 390, 'y': 328, 'type': 'text'},
    'REL10_4': {'x': 405, 'y': 328, 'type': 'text'},
    'REL10_5': {'x': 422, 'y': 328, 'type': 'text'},
    'REL10_6': {'x': 438, 'y': 328, 'type': 'text'},
    'REL10_7': {'x': 455, 'y': 328, 'type': 'text'},

    # Single-value fields
    'REL13': {'x': 69, 'y': 192, 'type': 'text'},
    'REL15': {'x': 328, 'y': 204, 'type': 'text'},
    'REL16': {'x': 329, 'y': 142, 'type': 'text'},
    'REL14': {'x': 74, 'y': 142, 'type': 'text'},
}

SA100_TR5 = {
    # SLR1 – notification from Student Loans
    "SLR1": {'x': 69, 'y': 669, 'type': 'text'},

    # SLR2 – employer deducted Student Loan
    "SLR2_0": {'x': 344, 'y': 708, 'type': 'text'},
    "SLR2_1": {'x': 360, 'y': 708, 'type': 'text'},
    "SLR2_2": {'x': 374, 'y': 708, 'type': 'text'},
    "SLR2_3": {'x': 390, 'y': 708, 'type': 'text'},
    "SLR2_4": {'x': 405, 'y': 708, 'type': 'text'},
    "SLR2_5": {'x': 422, 'y': 708, 'type': 'text'},
    "SLR2_6": {'x': 438, 'y': 708, 'type': 'text'},
    "SLR2_7": {'x': 455, 'y': 708, 'type': 'text'},

    # SLR3 – employer deducted Postgraduate Loan
    "SLR3_0": {'x': 344, 'y': 652, 'type': 'text'},
    "SLR3_1": {'x': 360, 'y': 652, 'type': 'text'},
    "SLR3_2": {'x': 374, 'y': 652, 'type': 'text'},
    "SLR3_3": {'x': 390, 'y': 652, 'type': 'text'},
    "SLR3_4": {'x': 405, 'y': 652, 'type': 'text'},
    "SLR3_5": {'x': 422, 'y': 652, 'type': 'text'},
    "SLR3_6": {'x': 438, 'y': 652, 'type': 'text'},
    "SLR3_7": {'x': 455, 'y': 652, 'type': 'text'},

    # CBC1 – total Child Benefit
    "CBC1_0": {'x': 84, 'y': 495, 'type': 'text'},
    "CBC1_1": {'x': 100, 'y': 495, 'type': 'text'},
    "CBC1_2": {'x': 118, 'y': 495, 'type': 'text'},
    "CBC1_3": {'x': 134, 'y': 495, 'type': 'text'},
    "CBC1_4": {'x': 150, 'y': 495, 'type': 'text'},

    # CBC2 – number of children
    "CBC2": {
        'x': 70,
        'y': 435,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },

    # CBC3 – stopped getting Child Benefit (date)
    "CBC3_0": {
        'x': 329,
        'y': 467,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    "CBC3_1": {
        'x': 366,
        'y': 467,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    "CBC3_2": {
        'x': 405,
        'y': 467,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },

    # MAT1 & MAT2 – spouse/civil partner name
    "MAT1": {'x': 72, 'y': 281, 'type': 'text'},
    "MAT2": {'x': 72, 'y': 231, 'type': 'text'},

    # MAT3 – spouse/civil partner NI number
    "MAT3_0": {'x': 72, 'y': 184, 'type': 'text'},
    "MAT3_1": {'x': 82, 'y': 184, 'type': 'text'},
    "MAT3_2": {'x': 107, 'y': 184, 'type': 'text'},
    "MAT3_3": {'x': 122, 'y': 184, 'type': 'text'},
    "MAT3_4": {'x': 145, 'y': 184, 'type': 'text'},
    "MAT3_5": {'x': 160, 'y': 184, 'type': 'text'},
    "MAT3_6": {'x': 183, 'y': 184, 'type': 'text'},
    "MAT3_7": {'x': 199, 'y': 184, 'type': 'text'},
    "MAT3_8": {'x': 221, 'y': 184, 'type': 'text'},

    # MAT4 – spouse/civil partner date of birth
    "MAT4_0": {
        'x': 328,
        'y': 270,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    "MAT4_1": {
        'x': 366,
        'y': 270,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    "MAT4_2": {
        'x': 405,
        'y': 270,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },

    # MAT5 – date of marriage/civil partnership
    "MAT5_0": {
        'x': 328,
        'y': 230,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    "MAT5_1": {
        'x': 366,
        'y': 230,
        'type': 'boxed',
        'box_width': 12,
        'spacing': 1
    },
    "MAT5_2": {
        'x': 405,
        'y': 230,
        'type': 'boxed',
        'box_width': 15,
        'spacing': 1
    },
}

SA100_TR6 = {
    # FIN1 – Tax refunded or set off
    "FIN1_0": {'x': 84, 'y': 606, 'type': 'text'},
    "FIN1_1": {'x': 100, 'y': 606, 'type': 'text'},
    "FIN1_2": {'x': 118, 'y': 606, 'type': 'text'},
    "FIN1_3": {'x': 134, 'y': 606, 'type': 'text'},
    "FIN1_4": {'x': 150, 'y': 606, 'type': 'text'},
    "FIN1_5": {'x': 160, 'y': 606, 'type': 'text'},
    "FIN1_6": {'x': 183, 'y': 606, 'type': 'text'},
    "FIN1_7": {'x': 199, 'y': 606, 'type': 'text'},

    # FIN2 – If you have not paid enough tax (box 2)
    "FIN2": {'x': 69, 'y': 437, 'type': 'text'},

    # FIN3 – If you have not paid enough tax (box 3)
    "FIN3": {'x': 329, 'y': 450, 'type': 'text'},

    # FIN4 – Name of bank or building society
    "FIN4": {'x': 69, 'y': 321, 'type': 'text'},

    # FIN6 – Name of account holder
    "FIN6": {'x': 69, 'y': 275, 'type': 'text'},

    # FIN5 – Branch sort code
    "FIN5_0": {'x': 69, 'y': 215, 'type': 'text'},
    "FIN5_1": {'x': 85, 'y': 215, 'type': 'text'},
    "FIN5_2": {'x': 116, 'y': 215, 'type': 'text'},
    "FIN5_3": {'x': 132, 'y': 215, 'type': 'text'},
    "FIN5_4": {'x': 164, 'y': 215, 'type': 'text'},
    "FIN5_5": {'x': 177, 'y': 215, 'type': 'text'},

    # FIN7 – Account number
    "FIN7_0": {'x': 69, 'y': 167, 'type': 'text'},
    "FIN7_1": {'x': 85, 'y': 167, 'type': 'text'},
    "FIN7_2": {'x': 101, 'y': 167, 'type': 'text'},
    "FIN7_3": {'x': 116, 'y': 167, 'type': 'text'},
    "FIN7_4": {'x': 132, 'y': 167, 'type': 'text'},
    "FIN7_5": {'x': 145, 'y': 167, 'type': 'text'},
    "FIN7_6": {'x': 160, 'y': 167, 'type': 'text'},
    "FIN7_7": {'x': 177, 'y': 167, 'type': 'text'},

    # FIN8 – Building society reference number
    "FIN8_0": {'x': 69, 'y': 123, 'type': 'text'},
    "FIN8_1": {'x': 85, 'y': 123, 'type': 'text'},
    "FIN8_2": {'x': 101, 'y': 123, 'type': 'text'},
    "FIN8_3": {'x': 116, 'y': 123, 'type': 'text'},
    "FIN8_4": {'x': 132, 'y': 123, 'type': 'text'},
    "FIN8_5": {'x': 145, 'y': 123, 'type': 'text'},
    "FIN8_6": {'x': 160, 'y': 123, 'type': 'text'},
    "FIN8_7": {'x': 177, 'y': 123, 'type': 'text'},
    "FIN8_8": {'x': 192, 'y': 123, 'type': 'text'},
    "FIN8_9": {'x': 209, 'y': 123, 'type': 'text'},
    "FIN8_10": {'x': 225, 'y': 123, 'type': 'text'},
    "FIN8_11": {'x': 243, 'y': 123, 'type': 'text'},
    "FIN8_12": {'x': 256, 'y': 123, 'type': 'text'},
    "FIN8_13": {'x': 273, 'y': 123, 'type': 'text'},

    # FIN9–11 – nominee / bank declarations
    "FIN9": {'x': 69, 'y': 66, 'type': 'text'},
    "FIN10": {'x': 327, 'y': 307, 'type': 'text'},
    "FIN11": {'x': 327, 'y': 263, 'type': 'text'},

    # FIN12 – Nominee’s address
    "FIN12": {'x': 327, 'y': 216, 'type': 'text'},

    # FIN13 – Postcode
    "FIN13_0": {'x': 327, 'y': 136, 'type': 'text'},
    "FIN13_1": {'x': 344, 'y': 136, 'type': 'text'},
    "FIN13_2": {'x': 361, 'y': 136, 'type': 'text'},
    "FIN13_3": {'x': 378, 'y': 136, 'type': 'text'},
    "FIN13_4": {'x': 398, 'y': 136, 'type': 'text'},
    "FIN13_5": {'x': 415, 'y': 136, 'type': 'text'},
    "FIN13_6": {'x': 432, 'y': 136, 'type': 'text'},
    "FIN13_7": {'x': 449, 'y': 136, 'type': 'text'},

    # FIN14 – Declaration signature
    "FIN14": {'x': 369, 'y': 63, 'type': 'text'},
}

SA100_TR7 = {
    # FIN15 – Your tax adviser’s name
    "FIN15": {'x': 69, 'y': 711, 'type': 'text'},

    # FIN16 – Their phone number
    "FIN16_0": {'x': 69, 'y': 643, 'type': 'text'},
    "FIN16_1": {'x': 85, 'y': 643, 'type': 'text'},
    "FIN16_2": {'x': 101, 'y': 643, 'type': 'text'},
    "FIN16_3": {'x': 116, 'y': 643, 'type': 'text'},
    "FIN16_4": {'x': 132, 'y': 643, 'type': 'text'},
    "FIN16_5": {'x': 145, 'y': 643, 'type': 'text'},
    "FIN16_6": {'x': 160, 'y': 643, 'type': 'text'},
    "FIN16_7": {'x': 177, 'y': 643, 'type': 'text'},
    "FIN16_8": {'x': 192, 'y': 643, 'type': 'text'},
    "FIN16_9": {'x': 209, 'y': 643, 'type': 'text'},
    "FIN16_10": {'x': 225, 'y': 643, 'type': 'text'},
    "FIN16_11": {'x': 243, 'y': 643, 'type': 'text'},
    "FIN16_12": {'x': 256, 'y': 643, 'type': 'text'},
    "FIN16_13": {'x': 273, 'y': 643, 'type': 'text'},

    # FIN17 – First line of their address including postcode
    "FIN17": {'x': 330, 'y': 712, 'type': 'text'},

    # FIN18 – Reference your adviser uses for you
    "FIN18_0": {'x': 327, 'y': 611, 'type': 'text'},
    "FIN18_1": {'x': 344, 'y': 611, 'type': 'text'},
    "FIN18_2": {'x': 361, 'y': 611, 'type': 'text'},
    "FIN18_3": {'x': 378, 'y': 611, 'type': 'text'},
    "FIN18_4": {'x': 391, 'y': 611, 'type': 'text'},
    "FIN18_5": {'x': 406, 'y': 611, 'type': 'text'},
    "FIN18_6": {'x': 422, 'y': 611, 'type': 'text'},
    "FIN18_7": {'x': 439, 'y': 611, 'type': 'text'},
    "FIN18_8": {'x': 456, 'y': 611, 'type': 'text'},
    "FIN18_9": {'x': 468, 'y': 611, 'type': 'text'},
    "FIN18_10": {'x': 486, 'y': 611, 'type': 'text'},
    "FIN18_11": {'x': 500, 'y': 611, 'type': 'text'},
    "FIN18_12": {'x': 518, 'y': 611, 'type': 'text'},
    "FIN18_13": {'x': 534, 'y': 611, 'type': 'text'},

    # FIN19 – Any other information
    "FIN19": {'x': 78, 'y': 533, 'type': 'text'},
}

SA100_TR8 = {


    "FIN20": {'x': 69, 'y': 687, 'type': 'text'},

    "FIN21": {'x': 69, 'y': 624, 'type': 'text'},


    
        "FIN23":{'x': 327, 'y': 713, 'type': 'text'},


        "FIN24": {'x': 330, 'y': 645, 'type': 'text'},

        "FIN25": {'x': 330, 'y': 578, 'type': 'text'},

        "FIN26": {'x': 330, 'y': 512, 'type': 'text'},


        
}
 