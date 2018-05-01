#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t1':1, 't2':1,'t3':12}
    if not param:
        param = defult_param
    
    alpha129= dv.add_formula('alpha129', 
               "Ts_Sum(If((close-Delay(close,%s)<0),Abs(close-Delay(close,%s)),0),%s)"%(param['t1'],param['t2'],param['t3'])
               , is_quarterly=False, add_data=True)
    return alpha129        

