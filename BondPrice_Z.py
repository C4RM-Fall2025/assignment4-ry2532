

def getBondPrice_Z(face, couponRate, times, yc):
    coupon=face*couponRate

    bondPrice=0
    for t,y in zip(times,yc):
        bondPrice+=coupon/((1+y)**t)
    bondPrice+=face/((1+yc[-1])**times[-1])
    return(bondPrice)




yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04



getBondPrice_Z(face, couponRate, times, yc)

