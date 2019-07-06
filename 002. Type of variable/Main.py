# Type of variable

import sys

minBool = False
maxBool = True
integerMin = -54549845
integerMax = 54549845


# Variable value
print("Boolean MIN value = " + str(minBool))  # False
print("Boolean MAX value = " + str(maxBool))  # True
print("There is no limit for MIN integer value, but this is integer presentation = " + str(integerMin))
print("There is no limit for MAX integer value, but this is integer presentation = " + str(integerMax))
print("Float MIN value  = " + str(sys.float_info.min))  # 1.7976931348623157e+308
print("Float MAX value  = " + str(sys.float_info.max))  # 2.2250738585072014e-308


# End of file
print()
input("Press Enter to continue...")