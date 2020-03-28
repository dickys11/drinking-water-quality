import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# define universe variables
i_ph = np.arange(0, 14.1, 0.1)
i_do = np.arange(0, 10.1, 0.1)
i_tds = np.arange(0, 301, 1)

o_cond = np.arange(0, 101, 1)

# fuzzy membership functions
# pH
ph_low = fuzz.trapmf(i_ph, [0, 0, 5, 6])
ph_mid = fuzz.trapmf(i_ph, [5, 6, 9, 10])
ph_hi = fuzz.trapmf(i_ph, [9, 10, 14, 14])

# DO
do_low = fuzz.trapmf(i_do, [0, 0, 3, 3.5])
do_mid = fuzz.trapmf(i_do, [3, 3.5, 4.5, 5])
do_hi = fuzz.trapmf(i_do, [4.5, 5, 10, 10])

# tds
tds_low = fuzz.trapmf(i_tds, [0, 0, 50, 70])
tds_mid = fuzz.trapmf(i_tds, [50, 70, 180, 200])
tds_hi = fuzz.trapmf(i_tds, [180, 200, 300, 300])

# condition
cond_bad = fuzz.trapmf(o_cond, [0, 0, 40, 60])
cond_good = fuzz.trapmf(o_cond, [40, 60, 100, 100])

# plot universe and membership functions
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4)

# pH
ax0.plot(i_ph, ph_low, 'b', linewidth=1.5, label='Low')
ax0.plot(i_ph, ph_mid, 'g', linewidth=1.5, label='Mid')
ax0.plot(i_ph, ph_hi, 'r', linewidth=1.5, label='High')
ax0.set_title('pH')
ax0.legend()

# DO
ax1.plot(i_do, do_low, 'b', linewidth=1.5, label='Low')
ax1.plot(i_do, do_mid, 'g', linewidth=1.5, label='Mid')
ax1.plot(i_do, do_hi, 'r', linewidth=1.5, label='High')
ax1.set_title('DO')
ax1.legend()

ax2.plot(i_tds, tds_low, 'b', linewidth=1.5, label='Low')
ax2.plot(i_tds, tds_mid, 'g', linewidth=1.5, label='Mid')
ax2.plot(i_tds, tds_hi, 'r', linewidth=1.5, label='High')
ax2.set_title('TDS')
ax2.legend()

ax3.plot(o_cond, cond_good, 'g', linewidth=1.5, label='Good')
ax3.plot(o_cond, cond_bad, 'r', linewidth=1.5, label='Bad')
ax3.set_title('Conditon')
ax3.legend()

# show the graph
for ax in (ax0, ax1, ax2, ax3):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show(block=False)


# input


ph = 9
do = 3.22
tds = 10

# calculate the membership value of the input
ph_lvl_low = fuzz.interp_membership(i_ph, ph_low, ph)
ph_lvl_mid = fuzz.interp_membership(i_ph, ph_mid, ph)
ph_lvl_hi = fuzz.interp_membership(i_ph, ph_hi, ph)

do_lvl_low = fuzz.interp_membership(i_do, do_low, do)
do_lvl_mid = fuzz.interp_membership(i_do, do_mid, do)
do_lvl_hi = fuzz.interp_membership(i_do, do_hi, do)

tds_lvl_low = fuzz.interp_membership(i_tds, tds_low, tds)
tds_lvl_mid = fuzz.interp_membership(i_tds, tds_mid, tds)
tds_lvl_hi = fuzz.interp_membership(i_tds, tds_hi, tds)

# print the values
print('\npH')
print('pH low membership value: {}'.format(ph_lvl_low))
print('pH mid membership value: {}' .format(ph_lvl_mid))
print('pH high membership value: {}' .format(ph_lvl_hi))

print('\ndo')
print('do low membership value: {}'.format(do_lvl_low))
print('do mid membership value: {}' .format(do_lvl_mid))
print('do high membership value: {}' .format(do_lvl_hi))

print('\ntds')
print('tds low membership value: {}'.format(tds_lvl_low))
print('tds mid membership value: {}' .format(tds_lvl_mid))
print('tds high membership value: {}' .format(tds_lvl_hi))

# rules
# bad
rule1 = np.fmin(tds_lvl_low, np.fmin(do_lvl_low, ph_lvl_low))
rule2 = np.fmin(tds_lvl_low, np.fmin(do_lvl_low, ph_lvl_mid))
rule3 = np.fmin(tds_lvl_low, np.fmin(do_lvl_low, ph_lvl_hi))
rule4 = np.fmin(tds_lvl_low, np.fmin(do_lvl_mid, ph_lvl_low))
rule6 = np.fmin(tds_lvl_low, np.fmin(do_lvl_mid, ph_lvl_hi))
rule7 = np.fmin(tds_lvl_low, np.fmin(do_lvl_hi, ph_lvl_low))
rule9 = np.fmin(tds_lvl_low, np.fmin(do_lvl_hi, ph_lvl_hi))
rule10 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_low, ph_lvl_low))
rule11 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_low, ph_lvl_mid))
rule12 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_low, ph_lvl_hi))
rule13 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_mid, ph_lvl_low))
rule15 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_mid, ph_lvl_hi))
rule16 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_hi, ph_lvl_low))
rule18 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_hi, ph_lvl_hi))
rule19 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_low, ph_lvl_low))
rule20 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_low, ph_lvl_mid))
rule21 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_low, ph_lvl_hi))
rule22 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_mid, ph_lvl_low))
rule23 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_mid, ph_lvl_mid))
rule24 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_mid, ph_lvl_hi))
rule25 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_hi, ph_lvl_low))
rule26 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_hi, ph_lvl_mid))
rule27 = np.fmin(tds_lvl_hi, np.fmin(do_lvl_hi, ph_lvl_hi))

activation_cond_bad = np.fmin(cond_bad,
                              np.fmax(rule1,
                                      np.fmax(rule2,
                                              np.fmax(rule3,
                                                      np.fmax(rule4,
                                                              np.fmax(rule6,
                                                                      np.fmax(rule7,
                                                                              np.fmax(rule9,
                                                                                      np.fmax(rule10,
                                                                                              np.fmax(rule11,
                                                                                                      np.fmax(rule12,
                                                                                                              np.fmax(rule13,
                                                                                                                      np.fmax(rule15,
                                                                                                                              np.fmax(rule16,
                                                                                                                                      np.fmax(rule18,
                                                                                                                                              np.fmax(rule19,
                                                                                                                                                      np.fmax(rule20,
                                                                                                                                                              np.fmax(rule21,
                                                                                                                                                                      np.fmax(rule22,
                                                                                                                                                                              np.fmax(rule23,
                                                                                                                                                                                      np.fmax(rule24,
                                                                                                                                                                                              np.fmax(rule25,
                                                                                                                                                                                                      np.fmax(rule26, rule27
                                                                                                                                                                                                              )))))))))))))))))))))))

# good
rule5 = np.fmin(tds_lvl_low, np.fmin(do_lvl_mid, ph_lvl_mid))
rule8 = np.fmin(tds_lvl_low, np.fmin(do_lvl_hi, ph_lvl_mid))
rule14 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_mid, ph_lvl_mid))
rule17 = np.fmin(tds_lvl_mid, np.fmin(do_lvl_hi, ph_lvl_mid))

activation_cond_good = np.fmin(cond_good,
                               np.fmax(rule5,
                                       np.fmax(rule8,
                                               np.fmax(rule14, rule17
                                                       ))))

cond0 = np.zeros_like(o_cond)

# plot
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.fill_between(o_cond, cond0, activation_cond_bad, facecolor='r', alpha=0.7)
ax0.plot(o_cond, cond_bad, 'r', linewidth=0.5, linestyle='--', )
ax0.fill_between(o_cond, cond0, activation_cond_good, facecolor='g', alpha=0.7)
ax0.plot(o_cond, cond_good, 'g', linewidth=0.5, linestyle='--', )
ax0.set_title('Output membership activity')


# plt.show()

# defuzzification
# aggregate all function
aggregated = np.fmax(activation_cond_bad, activation_cond_good)

# calculate deffuzified result
condition = fuzz.defuzz(o_cond, aggregated, 'centroid')
condition_activation = fuzz.interp_membership(
    o_cond, aggregated, condition)  # for plot

# plot
ax0.plot(o_cond, cond_bad, 'r', linewidth=0.5, linestyle='--', )
ax0.plot(o_cond, cond_good, 'g', linewidth=0.5, linestyle='--')
ax0.fill_between(o_cond, cond0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([condition, condition], [0, condition_activation],
         'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.show()

print('\nnilai kelayakan air sebesar {0:.2f}/100 '.format(condition))
