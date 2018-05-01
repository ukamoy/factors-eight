#--------------------------------------------------------- 
#type4 - caculate factor with industry category 


def run_formula(dv, param = None):
    default_param = {'t1':5,'t2':20}
    if not param:
        param = default_param
        
    alpha8 = dv.add_formula('alpha8',"Ts_Mean(Sign(Delta(high,%s))*volume,%s)"%(param['t1'],param['t2']), is_quarterly=False, add_data=True)
    return alpha8
