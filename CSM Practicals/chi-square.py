    
import numpy as np
import scipy.stats as stats

# rolling dice and null hypothesis is the dice is fair or not
# it looks fitness of data
observed = np.array([22, 24, 38, 30, 46, 44])
expected = np.array([1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0, 1.0 / 6.0]) * np.sum(observed)
print (np.sum(observed))
(t, p) = stats.chisquare(observed, expected, ddof=1)
print ('Test t=%f p-value = %f' % (t, p))

alpha = 0.05  # significance level

if p <= alpha:
    # we reject null hypothesis
    print ('Null hypothesis (dice is fair) is unlikely to except')
else:
    # we reject alternative hypothesis
    print ('Null hypothesis (dice is fair) cannot be rejected')
