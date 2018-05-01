#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    VSTD_20 = dv.add_formula('VSTD_20',"StdDev(volume,%s)" % (t,), is_quarterly=False, add_data=True)

    return VSTD_20

