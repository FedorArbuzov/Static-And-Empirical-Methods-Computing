import scipy.stats as stats
import numpy

def generate_data(n, forced_matexpect):
    # CHANGE THIS
    return numpy.random.chisquare(forced_matexpect * 2, n)
    # return numpy.random.normal(forced_matexpect, 4.0, n)

def test_data_mean_eq(data, suggested):
    # True if we accept H0
    # False if we accept Ha
    # > 0.05 to show 5% willingness to accept error
    return stats.ttest_1samp(data, suggested)[1] > 0.05

def write_graphic(filename, x, y):
    print(filename, x, y)

def experiment(gen_data_length):
    # store [mat expectation] = number of times H_a was chosen
    sz = 1000
    result = {}
    for mat_expect in numpy.linspace(1.0, 5.0, num=9):
        result[mat_expect] = 0
        for i in range(sz):
            d = generate_data(gen_data_length, mat_expect)
            if (not test_data_mean_eq(d, 3.0)):
                result[mat_expect] += 1
    # print(result)
    x = []
    y = []
    for k in sorted(result.keys()):
        x.append("{:.1f}".format(k))
        y.append( (1.0*result[k] / sz) * 100.0 )

    write_graphic("mat_expect_VS_chosen_H_a_{}.svg".format(gen_data_length), x, y)

# do test 10000 times part one
mat_expected = 3.0
sz = 10000
take_H0 = 0.0
take_Ha = 0.0
for _ in range(sz):
    # Generate data with what ever distribution function
    # But force the math_expectation to be = 3
    d = generate_data(8, mat_expected)
    if (test_data_mean_eq(d, 3.0)):
        take_H0 += 1
    else:
        take_Ha += 1

print("Error 1 type occurred: {}/{}".format(take_Ha, sz))
print("Chance: {}%".format((take_Ha/sz) * 100.0))

# do two experiments part two
experiment(8)
experiment(50)

