from integrator import Integrator

if __name__ == '__main__':
    restarter = True
    while restarter:
        print(Integrator.integrator())
        ender = input('try again')
        if ender != 'yes':
            restarter = False


'''

All the steps for the integration calculator to be completed: 

(bare in mind, tests must be done for each step)

Single Integral
1. Integrate simple terms: 56x^55 (DONE)
2. integrate multiple terms separated by + and -: 56x^55 + 42x^5 - 54x^7 (Done)
3. Integrate simple Trig and hyperbolic (sinx, cosx, sinhx,coshx)
4. Integrate Other math terms: (e^x, 1/x^(something))
5. Integration by parts 

Other implementations:
1. Being able to integrate between two numbers,
2. Being able to integrate multiple variables. 
'''