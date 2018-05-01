#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t1':240, 't2':240}
    if not param:
        param = defult_param
    
    alpha1= dv.add_formula('alpha1', 
               "%s*LFLO/Ts_Sum(LFLO,%s)"%(param['t1'],param['t2'])
               , is_quarterly=False, add_data=True)
    return alpha1        

