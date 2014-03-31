# Memofibo

# Submit via the interpreter a definition for a memofibo procedure that uses a
# chart. You are going to want the Nth value of the chart to hold the Nth
# fibonacci number if you've already computed it and to be empty otherwise.

import timeit
t = timeit.Timer(stmt = """

chart = {}

def memofibo(n):
    if n in chart:
        return chart[n]
    elif n <= 2:
        chart[n] = 1
    else:
        chart[n] = memofibo(n-1) + memofibo(n-2)
    return chart[n]
    
memofibo(25)
""")

print t.timeit(number=100)

#################
chart = {}

def memofibo(n):
    if n in chart:
        return chart[n]
    elif n <= 2:
        chart[n] = 1
    else:
        chart[n] = memofibo(n-1) + memofibo(n-2)
    return chart[n]
    
