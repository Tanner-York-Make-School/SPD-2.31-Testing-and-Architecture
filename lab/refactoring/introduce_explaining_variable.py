"""
By Kami Bigdely
Introduce explaining variable (alias extract variable)
Reference: https://www.researchgate.net/publication/305768969_The_role_of_eye_characteristics_in_facial_beauty_likability_and_attractiveness
Background: You are a computer engineer trying to sift through many profiles to find
your soulmate. Unfortunately, there are too many profiles and it's getting tedious. You write a
python script to scrape profiles info (such as height, age, etc) and images (for image processing)
to figure out automatically who is attractive to you.  Here is a part of the script:
"""
import math
# assuming you have extracted the following info from the profile's image.
EYE_SIZE = 0.47    # [cm^2]
EYE_WIDTH = 24.2   # [mm]
EYE_HEIGHT = 23.7  # [mm]

IRIS_WIDTH = 20.2  # [mm]
IRIS_HEIGHT = 19.7 # [mm]

EYE_IRIS_AREA = (math.pi*IRIS_WIDTH/2*IRIS_HEIGHT/2) / EYE_SIZE
EYE_QUOTIENT = EYE_HEIGHT/EYE_WIDTH

DESIRED_EYE_SIZE = 0.45
DESIRED_EYE_IRIS_AREA = 0.69
DESIRED_EYE_QUITIENT = 0.59

if EYE_SIZE > DESIRED_EYE_SIZE and EYE_IRIS_AREA >= DESIRED_EYE_IRIS_AREA and EYE_QUOTIENT >= DESIRED_EYE_QUITIENT:
    print("I'm sorry I wasn't part of your past, can I make it up by being in your future?")
