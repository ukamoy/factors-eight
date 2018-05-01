#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t1':10,'t2':2,'t3':1,'t4':20,'t5':5}
    if not param:
        param = defult_param
        
    
    alpha142 = dv.add_formula('alpha142',"(((-1*Rank(Ts_Rank(close,%s)))*Rank(Delta(Delta(close,%s),%s)))*Rank(Ts_Rank((volume/Ts_Mean(volume,%s)),%s)))"%(param['t1'],param['t2'],param['t3'],param['t4'],param['t5']),is_quarterly=False,add_data=True)

    return alpha142

