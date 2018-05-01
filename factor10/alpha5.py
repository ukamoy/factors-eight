#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
	alpha5 = dv.add_formula('alpha5',"roe/pb", is_quarterly=False, add_data=True)
	return alpha5