
def getBondPrice_E(face, couponRate, yc):
    coupon=face*couponRate
    n=len(yc)

    bondPrice=0
    for t,y in enumerate(yc,start=1):
        bondPrice+=coupon/((1+y)**t)
    bondPrice+=face/((1+y)**n)

    return(bondPrice)


yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04



getBondPrice_E(face, couponRate, yc)
