import numpy as np
from scipy.special import lambertw


def baseTerm( t , t0 , K , C , V ) :
    return np.real(K*lambertw((C/K)*np.exp(-(V/K)*(t+t0)+(C/K))))

def simpleTerm( t , K , p , q ) :
    return np.real( K*lambertw(p*np.exp(-q*t)) )
