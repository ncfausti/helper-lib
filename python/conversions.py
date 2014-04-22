def calculateMetricBMI(heightMeters, weightKgs):
    return "%.2f" % ((weightKgs * 1.0) / (heightMeters ** 2))

def calculateStandardBMI(heightInches, weightLbs):
    return "%.2f" % ((weightLbs * 703 * 1.0) / (heightInches ** 2))

def inchesToMeters(inches):
    return inches * .0254

def getBMI(hList,wList):
    for h,w in zip(hList, wList):
        if w.lower().find("lbs") > -1:
            #print("{} {} {}".format(h,w,calculateStandardBMI(int(h[0:2]),int(w[0:-3]))))
                        print("{}\t{}\t".format(
                            calculateStandardBMI(
                                int(h[0:2]),int(w[0:-3]))," ")),
        elif w.lower().find("kgs") > -1:
            #print("{} {} {}".format(h, w, calculateMetricBMI(inchesToMeters(int(h[0:2])), int(w[0:-3]))))
                        print("{}\t{}\t".format(
                            calculateMetricBMI(
                                inchesToMeters( int(h[0:2]) ), int(w[0:-3]) ) , " ")),
        else:
            print w

def printBMI(hList,wList):
        for h,w in zip(hList, wList):
        if w.lower().find("lbs") > -1:
            print("{}\t{}\t{}".format(h,w,calculateStandardBMI(int(h[0:2]),int(w[0:-3]))))
            #print("{}\t{}\t".format(calculateStandardBMI(int(h[0:2]),int(w[0:-3]))," ")),
        elif w.lower().find("kgs") > -1:
            print("{}\t{}\t{}".format(h, w, calculateMetricBMI(inchesToMeters(int(h[0:2])), int(w[0:-3]))))
            #print("{}\t{}\t".format(calculateMetricBMI(inchesToMeters( int(h[0:2]) ), int(w[0:-3]) ) , " ")),
        else:
            print w
