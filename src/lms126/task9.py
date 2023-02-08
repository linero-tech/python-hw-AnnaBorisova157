from to_do import TODO


def task9():
    return """
 input Amount from customer keypad
 read customer's details from accounts database
    IF customer has insufficient funds
    THEN BEGIN display 'insufficient funds' message
END
    ELSE BEGIN display offer of available funds
    INPUT customer's response (Y/N)
    IF response is 'Y'
      THEN set reduced Amount
      ELSE set Amount to zero
    ENDIF
    END
return customer's card
  IF Amount is not zero
  THEN BEGIN dispense cash Amount
  IF WithdrawalType is with_receipt
  THEN print receipt for Amount
  ENDIF
update accounts database
END Withdrawal
"""