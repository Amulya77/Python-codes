# Secret Auction

import art


print(art.logo)
print("Welcome to the secret auction program.")

bids={}
bid_f=False

def find_highest_bidder(bidding_record):
    #biddding_record={"Angela:134,"James":323}
    highest_bid = 0
    winner=""
    for key in bidding_record:
        bidamt=bidding_record[key]
        if bidamt>highest_bid:
            highest_bid=bidamt
            winner=key
    print(f"The winner is {winner} with a bid of ${highest_bid}")
        



while not bid_f:
    name=input("What is your name?: ")
    price=int(input("What is your bid? $: "))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'yes or 'no'\n")
    if should_continue =='no':
        bid_f=True
        find_highest_bidder(bids) 
    # since the "replit" module is not available and there doesn't seem to be a simple way to clear the screen that
    # would RELIABLY work on different platforms, i.e. "import os" AND "os.system("clear")" OR "os.system("cls")" ...
    # ... just print a bunch of blank lines instead, both between each bid and at the end
    
    elif should_continue =='yes':
        print("\n" * 100)
         