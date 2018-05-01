#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t':26}
    if not param:
        param = defult_param
        
    t = param['t']
    
    Aroon_up = dv.add_formula('Aroon_up',"Ts_Argmax(close,%s)/%s" % (t,t),is_quarterly=False, add_data=True)
    return Aroon_up        

