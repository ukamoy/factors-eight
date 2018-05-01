#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t1':20,'t2':30,'t3':30}
    if not param:
        param = defult_param
        
    
    alpha4 = dv.add_formula('alpha4',"Ts_Max(volume,%s)*%s/Ts_Sum(volume,%s)-1"%(param['t1'],param['t2'],param['t3']),is_quarterly=False,add_data=True)

    return alpha4

