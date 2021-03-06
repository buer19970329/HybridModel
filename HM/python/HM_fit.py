# %%

def HM_fit(response,data,ro):
    from scipy.optimize import minimize
    import numpy as np
    from HM_lik import HM_lik

    xfit = []
    LL = []
    BIC = []
    nsubj= np.shape(response)[0]
    for ns in range(nsubj):
        def obFunc(params):
            x,y,z = params
            return HM_lik(response[ns,:],data,ro,x,y,z)
        x0 = np.array([0.5,4,0.5])
        bnds = ((0,1),(0,14),(0,1))
        res = minimize(obFunc, x0,method = 'Nelder-Mead',bounds=bnds)
        
        BIC.append(len(x0)*np.log(len(response[ns,:]))+2*res['fun'])
        LL.append(-res['fun'])
        xfit.append(res['x'])       
    xfit=np.array(xfit)
    BIC = np.array(BIC)
    return xfit,np.array(LL),np.array(BIC)