

def getBondDuration(y, face, couponRate, m, ppy = 1):
    r=y/ppy
    coupon=face*couponRate/ppy
    n=m*ppy

    num=0
    for i in range(1,n+1):
        num+=i*(coupon/((1+r)**i))
    num+=n*(face/((1+r)**n))

    den=0
    for i in range(1,n+1):
        den+=coupon/((1+r)**i)
    den+=face/((1+r)**n)

    bondDuration=(num/den)/ppy

    return(bondDuration)




y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1


getBondDuration(y,face,couponRate,m,1)







