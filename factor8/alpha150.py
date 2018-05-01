#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
	alpha150 = dv.add_formula('alpha150',"(close+high+low)/3*volume", is_quarterly=False, add_data=True)
	return alpha150