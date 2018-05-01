#type3  -  the intermediate variable of the factor is also a factor


def run_formula(dv, param = None):
    defult_param = {'t1':20}
    if not param:
        param = defult_param
    alpha3_1 = dv.add_formula('alpha3_1', 
               "Ta('ATR',0,high,low,close,volume,6)"
               , is_quarterly=False, add_data=True)

    alpha3= dv.add_formula('alpha3', 
               "Ts_Rank(Max(alpha3_1,Abs(high-low)),%s)"%(param['t1'])
               , is_quarterly=False, add_data=True)
    return alpha3        

