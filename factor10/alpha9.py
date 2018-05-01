

def run_formula(dv, param = None):
    defult_param = {'t':180}
    if not param:
        param = defult_param
        
    t = param['t']
    alpha9_1 = dv.add_formula('alpha9_1', 
               "(net_profit-Delay(net_profit, 240))/Delay(net_profit, 240)"
               , is_quarterly=False, add_data=True)
    alpha9 = dv.add_formula('alpha9', 
               "1-alpha9_1/Delay(roe,%s)"% (t,),is_quarterly=False, add_data=True)
    return alpha9