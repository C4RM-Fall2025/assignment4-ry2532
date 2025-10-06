
def getBondPrice(y, face, couponRate, m, ppy=1):
    n=m*ppy
    r=y/ppy
    coupon=face*couponRate/ppy

    bondPrice=0
    for t in range(1, n+1):
        bondPrice+=coupon/(1+r)**t

    bondPrice+=face/(1+r)**n

    return(bondPrice)



y = 0.03
face = 2000000
couponRate = 0.04
m = 10


getBondPrice(y,face,couponRate,m,1)


getBondPrice(y,face,couponRate,m,2)

