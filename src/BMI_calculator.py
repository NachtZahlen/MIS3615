import webbrowser

def bmi_calculator(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18.5:
        print("your bmi is {:.1f}. You are underweighted.".format(bmi))
        webbrowser.open('https://www.mcdonalds.com/us/en-us.html')
    elif bmi < 18.5 and bmi <= 25:
        print("your bmi is {:.1f}. You are normal-weighted.".format(bmi))
    elif 25 < bmi <= 29.9:
        print("your bmi is {:.1f}. You are overweighted.".format(bmi))
    else:
        print("your bmi is {:.1f}. You are obese.".format(bmi))


weight = input('Enter your weight: ')
height = input('Enter your height: ')
weight = float(weight)
height = float(height)

bmi_calculator(weight, height)
