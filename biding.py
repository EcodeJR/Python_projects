#use while loop to make the code work with each participant at a time
print("ASSET AUCTION")
print("Instructions: Each participant will the amount he/she wishes to buy an asset and highest bidder wins.")
print("Follow all instructions during the bidding stage.. :\n And goodluck")

bidders = []
x = []
items = ("HP EliteBook", "Toyota Camry", "4 bedroom Flat")


#getting bidders numbers/names/bids and appending it to the list
numb_of_bidders = int(input("Enter the number of Bidders :\n"))
for i in range(0,numb_of_bidders):
    print("starting price $30,000")
    bidder_name_amount = input("Enter name of bidder")
    bidders.append(bidder_name_amount)
    amount = int(input("Enter amount to bid"))
    x.append(amount)

print(bidders,":\n", x, ":\n")
print(max(x), "won")
print("Here are your items", items)