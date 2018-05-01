#type3  -  the intermediate variable of the factor is also a factor

def run_formula(dv, param = None):
    defult_param = {'t':20}
    if not param:
        param = defult_param
        
    t = param['t']
    
    alpha10 = dv.add_formula('alpha10',"Ts_Mean(BullPower*volume*(high-low),%s)" % (t,), is_quarterly=False, add_data=True)

    return alpha10

