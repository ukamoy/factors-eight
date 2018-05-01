#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':60}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha6 = dv.add_formula('alpha6',"pe/Ts_Mean(pe,%s)" % (t,),is_quarterly=False, add_data=True)
    return alpha6        

