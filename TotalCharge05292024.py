charge = float(input('Input cost of the meal before tax and tip\n'))
tax = charge * 0.07
tip = (charge+tax) * 0.18
total = charge + tax + tip
print('Cost of meal: ${:.2f}'.format(charge))
print('Tax:          ${:.2f}'.format(tax))
print('Tip:          ${:.2f}'.format(tip))
print('Total:        ${:.2f}'.format(total))