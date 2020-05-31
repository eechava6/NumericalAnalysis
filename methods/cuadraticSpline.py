import ast
import json

import numpy as np
from methods.utils import gaussPartial


def cuadraticSpline(x, y):
    x = ast.literal_eval(x)
    y = ast.literal_eval(y)

    res = {}
    x = np.asfarray(x)
    y = np.asfarray(y)
    n = len(x)
    m = 3*(n-1)
    A = np.zeros([m,m])
    b = np.zeros([m,1])
    S = []

    if n != len(y):
        res["source"] = "X and Y boundaries are different"
        res["error"] = True
        return

    A[0][0:3] = [x[0]**2,x[0], 1]
    b[0] = y[0]
    for val in range(1,n):
        A[val][ 3*val-3:3*val] = [x[val]**2, x[val], 1]
        b[val] = y[val]


    for val in range(1,n-1):
        A[n-1+val][3*val-3:3*val+3] = [x[val]**2, x[val], 1,-x[val]**2, -x[val], -1]

    for val in range(1,n-1):
        A[2*n-3+val][3*val-3:3*val+3] = [x[val]*2, 1, 0,-x[val]*2, -1, 0]

    A[m-1,0] = 2;
    values = gaussPartial(A,b)
    if values["error"]:
        res["error"] = True
        res["source"] = values["source"]
        return res

    vals = sorted(values["values"], key = lambda x:  x[0])

    pols = []
    for val in range(0,len(vals)-2,3):
        pol = "{0}*x^2+{1}*x+{2}".format(vals[val][1], vals[val+1][1],vals[val+2][1])
        pol = pol.replace(" ", "").replace("--", "+").replace("++", "+").replace("+-", "-").replace("-+", "-")
        S.append([vals[val][1], vals[val+1][1], vals[val+2][1]])
        pols.append(pol)

    A = np.array(A).astype(float)
    S = np.array(S).astype(float)
    res["polynoms"] = pols
    res["values"] = S.tolist()
    res["error"] = False
    res["matrix"] = json.dumps(A.tolist())
    return res
