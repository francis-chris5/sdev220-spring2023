

import emoji

rateOfPay = float(input(emoji.emojize("How much do you make :thumbs_up: : ")))
hours = float(input(emoji.emojize("How much did you work :tired_face: : ")))

if hours > 40:
	grossPay = 40 * rateOfPay + (hours-40) * (rateOfPay * 1.5)
else:
	grossPay = hours * rateOfPay


print(emoji.emojize("That will be $" + format(grossPay, ".2f") + " this week :astonished_face:."))
