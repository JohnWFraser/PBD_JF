# B8IT105 CA4
# John Fraser (1036555)
# Below are 10 function I used in cA1
#I have reproduced them below. The user must enter the parameter
# e.g. in reciprocal below, 3 is the parameter which must be entered in line 19
# I have entered sample numbers in each case - the results are correct! Note
# that I have supplied more than one example in some cases (using vector c(a,b,c,..,etc.))
# (except that the exponential function (final one) seems to be not working)


# (1) sine function:
radians <- function(x) {x*(2*pi/360)}
# above takes degrees and converts into radians
sine <- function(func,dat) {paste("the sine is",(func(dat)))}
sine(sin, radians(30))

# (2) reciprocal:
reciprocal <- function(x) {paste("the reciprocal of " ,x, "is" , (1/x))}
reciprocal(3)
reciprocal(c(2,4,5,10))

# (3) square:
square <- function(x) {paste(x,"squared = ",(x**2))}
square(-4)

# (4) square root:
sqroot <- function(x) {paste("square root of ",x," = ",(x**0.5))}
sqroot(c(10,25,81,100,150))

# (5) cube:
cube <- function(x) {paste(x,"cubed = ",(x**3))}
cube(3)

# (6) cube root:
cuberoot <- function(x) {paste("cube root of ",x," = ",x**(1/3))}
cuberoot(729)

# (7) power function (y^x):
ypowerx <- function(y,x) {paste(y,"to power of",x," = ",y**x)}
ypowerx(2,3)

# (8) natural log (base 2.718..):
natlog <- function(x) {paste("natural log of ",x," is:",log(x))}
natlog(100)

# (9) log (base 10):
logbase10 <- function(x) {paste("log to base 10 of",x ," is: ",log(x, base = 10))}
logbase10(c(10,100,1000, 500))

# (10) exponential (e^x):
expfn <- function(x) {paste("exponential to power of", x ,"is: ",exp(x))}
expfn(1)