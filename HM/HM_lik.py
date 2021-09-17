# %%
def HM_lik(data,ro,alpha,beta,w):
    import numpy as np

    eta = np.zeros(np.shape(data)[0]+1,dtype='float')    
    expProb = np.zeros_like(data,dtype='float')
    valueV = np.zeros_like(data,dtype='float')
    v = np.array([0.25,0.75])
    eta[0] = 1
    
    for t in range(len(data)):
        
        p = np.exp(beta*v) / np.sum(np.exp(beta*v))
        
        expProb[t] = p[data[t]]
        
        PE = ro[t]-v[data[t]]
        
        v[data[t]] = v[data[t]] + alpha * PE * eta[t]
        
        eta[t+1] = w * np.abs(PE) + (1-w) * eta[t]
        
        valueV[t] = v[data[t]]
        
    _,*eta = eta
    NegLL = -np.sum(np.log(expProb));
    eta = np.array(eta)
    return NegLL