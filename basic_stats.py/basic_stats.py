def BasicStats(list):
    n = len(list); # length of list
    sum_list = sum(list); # sum of elements in list
    mean = (sum_list / n); # mean
    var = sum([((i - mean) ** 2) for i in list]); # variance
    dev = (var/n); # deviation
    sd = dev**(1/2); # standard deviation
    print("Average is", mean, "and standard deviation is", sd); # print mean and sd
    plt.hist(list, bins=10); # plot list
    plt.xlabel("x"); # label x axis
    plt.ylabel("Counts"); # label y axis
    plt.title("Histogram of list"); # add title
    plt.show() # print plot 
