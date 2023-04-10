
wavelength = float(input("Enter wavelength in nanometers (nm): "))

if wavelength < 380 or wavelength > 750:
    print("Error: Wavelength is outside of the visible spectrum!")
else:
    # Determine color based on wavelength range
    if 380 <= wavelength < 450:
        color = "Violet"
    elif 450 <= wavelength < 495:
        color = "Blue"
    elif 495 <= wavelength < 570:
        color = "Green"
    elif 570 <= wavelength < 590:
        color = "Yellow"
    elif 590 <= wavelength < 620:
        color = "Orange"
    else: # wavelength is between 620 and 750
        color = "Red"

    print(f"The color corresponding to {wavelength} nm is {color}.")



'''
Problem -II
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:
Radio Waves Less than 3 × 10^9
Microwaves 3 × 10^9 to less than 3 × 10^12
Infrared Light 3 × 10^12 to less than 4.3 × 10^14
Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
X-Rays 3 × 10^17 to less than 3 × 10^19
Gamma Rays 3 × 10^19 or more
Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message.
'''

f = float(input("Enter Frequency: "))
if (f<(3*(10**9))):
    print("Radio Waves")
elif ((3*(10*9)<=f<(3(10**12)))):
    print("Microwaves")
elif ((3*(10*12))<=f<(4.3(10**14))):
    print("Infrared Light")
elif ((4.3*(10*14))<=f<(7.5(10**14))):
    print("Visible Light")
elif ((7.5*(10*14))<=f<(3(10**7))):
    print("Ultraviolet Light")
elif ((3*(10*7))<=f<(3(10**19))):
    print("X-Rays")
else:
    print("Gamma Rays")