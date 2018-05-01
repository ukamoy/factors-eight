#--------------------------------------------------------- 
#type4 - caculate factor with industry category 


def run_formula(dv, param = None):
    default_param = {'t1':1,'t2':60,'t3':1,'t4':60}
    if not param:
        param = default_param
    SharpeRatio_60 = dv.add_formula('SharpeRatio_60',"(Ts_Mean(close_adj-Delay(close_adj,%s),%s)-0.03)/StdDev(close_adj-Delay(close_adj,%s),%s)/Sqrt(250)"%(param['t1'],param['t2'],param['t3'],param['t4']), is_quarterly=False, add_data=True)
    return SharpeRatio_60
