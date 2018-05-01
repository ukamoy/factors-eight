

def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    Skewness_20 = dv.add_formula('Skewness_20',"Ts_Skewness(close_adj, %s)" % (t,),is_quarterly=False, add_data=True)
    return Skewness_20        

