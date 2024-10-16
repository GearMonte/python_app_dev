import matplotlib.pyplot as plt
from data import in_st, in_co

# Step 1: Create your plots using matplotlib
# Updating your color scheme:
plt.rcParams['axes.prop_cycle'] = plt.cycler(
    color=['#334751','#d2a678', '#80c2b4', '#896354', '#579ab3'])

# First plot is the covid_deaths for the State
fig1, ax1 = plt.subplots()
ax1.bar(in_st.DATE, in_st.COVID_DEATHS)
ax1.set_title('Indiana State: Covid 19 Deaths 2020-2023')
plt.show()

fig2, ax2 = plt.subplots()
ax2.barh(list(in_co.COUNTY_NAME), in_co.COVID_DEATHS)
ax2.set_title('Indiana County: Covid 19 Deaths by County')
plt.show()

fig3, ax3 = plt.subplots()
ax3.pie(in_st.col)