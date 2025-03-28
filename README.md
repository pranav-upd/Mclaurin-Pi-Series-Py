# Mclaurin-Pi-Series-Py
In this project, you can calculate "N" digits of pi, which is related to the number of iterations you run on the program. I'll get more into it later in the project. We do this by calculating the Maclaurin series of the inverse trignometric function of the Sine function at 0.5 as ArcSin(0.5) = Pi/6

Or,

6 * Arcsin(0.5) = Pi

We will be calculating the infinite series of Arcsin(x) = Summation 0-infinity{(2n-1)!!*(x^(2n+1)}/{(2n)!!*(2n+1)}

[The derivation is a bit long, I will share a link of my question on math StackOverflow on which I have based the project for you math lovers -

https://math.stackexchange.com/questions/4140154/help-me-prove-the-summation-function-for-arcsin-x

The above link gives an idea of how the formula was derived

]

For ArcSin(0.5) = Summation 0-infinity{(2n-1)!!*(0.5^(2n+1)}/{(2n)!!*(2n+1)}

Now, since there is a limitation on how many floating places python can process, we will be using big Integer which is included by default in Python.

See the complete tutorial here: https://www.instructables.com/Calculate-Digits-of-Pi-Using-Python/
