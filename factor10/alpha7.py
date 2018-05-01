#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
	defult_param = {'t':60}
	if not param:
		param = defult_param

	t = param['t']
	BollMD= dv.add_formula('BollMD', "Ts_Sum(close,20)/20", is_quarterly=False, add_data=True)
	Bollup= dv.add_formula('Bollup', "BollMD+2*StdDev(BollMD,20)", is_quarterly=False, add_data=True)
	Bolldown= dv.add_formula('Bolldown', "BollMD-2*StdDev(BollMD,20)", is_quarterly=False, add_data=True)

	alpha7 = dv.add_formula('alpha7', 
               "Ts_Max(If(Bollup-Delay(Bollup,%s)>0,Bollup-Bolldown,0),%s)" %(t,t)
               , is_quarterly=False, add_data=True)
	return alpha7