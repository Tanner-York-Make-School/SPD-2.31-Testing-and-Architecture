"""
By Kami Bigdely
Decompose conditional
Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age
"""

# Blood test analysis program
TOTAL_CHOLOSTROL = 70
LDL = 30
TRIGLYCERIDE = 120

def blood_is_good_level():
    return TOTAL_CHOLOSTROL < 200 and LDL < 100 and TRIGLYCERIDE < 150

def blood_has_high_cholestrol():
    return 200 < TOTAL_CHOLOSTROL > 240 or LDL > 160 or TRIGLYCERIDE >= 200

def blood_on_TLC_diet():
    return 200 < TOTAL_CHOLOSTROL < 240 or 130 < LDL < 160 or 150 <= TRIGLYCERIDE < 200

if blood_is_good_level():
    # good level
    print('*** Good level of cholestrol ***')
elif blood_has_high_cholestrol():
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif blood_on_TLC_diet():
    # TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')
