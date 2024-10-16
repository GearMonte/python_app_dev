import matplotlib.pyplot as plt
from data import in_st, in_co

# Step 1: Create your plots using matplotlib
# Updating your color scheme:
plt.rcParams['axes.prop_cycle'] = plt.cycler(
    color=['#fbfec7', '#4bcdd7', '#f48217', '#2b3e4d', '#b4164e'])

# First plot is the covid_deaths for the State
fig1, ax1 = plt.subplots()
ax1.bar(in_st.DATE, in_st.COVID_DEATHS)
ax1.set_title('Indiana State: Covid 19 Deaths 2020-2023')
ax1.setxlabel('Year')
ax1.setylabel('Deaths')
plt.show()

