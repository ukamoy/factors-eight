#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t1':1, 't2':20}
    if not param:
        param = defult_param
    

    alpha2= dv.add_formula('alpha2', 
               "Ts_Mean(Log(close/Delay(close,%s)),%s)"%(param['t1'],param['t2'])
               , is_quarterly=False, add_data=True)
    return alpha2        

