total = 0

def process_order(x_list):
    global total
    for order in x_list:
        next_order = x_list.pop()
        order_total = next_order[1]*next_order[2]
        total += order_total
        print(f"You filled an order for {next_order[1]} {next_order[0]} for a total of ${order_total:.2f}")
    return


######################################################################################################
# DO NOT CHANGE ANY OF THE CODE BELOW HERE                                                           #
######################################################################################################

x = [("oranges", 4, 3.22),("gummy bears",1,1.99),("sour bites", 3, 2.33), ("antacid", 1, 5.33)]

while(len(x)>0):
    process_order(x)

print("Total price: ${:.2f}".format(total))
