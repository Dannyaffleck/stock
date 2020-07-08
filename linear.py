from scipy import stats
import numpy as np

datay = [1.0, 2.0, 5.0, 7.0, 6.0, 5.5, 4.8, 2.2]

datax = [idx for idx,val in enumerate(datay)]

print(f"{datay}   {datax}")

i = 4
while i<len(datay):
    da_y = np.array(datay[i-4:i])
    da_x = np.array(datax[i-4:i])
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(da_x,da_y)

    print(f"slope at {i} {slope}")
    i += 1