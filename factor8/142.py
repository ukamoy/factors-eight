#--------------------------------------------------------- 
#type4 - caculate factor with industry category 


def run_formula(dv, param = None):
    default_param = {'t1':10,'t2':2,'t3':1,'t4':20,'t5':5}
    if not param:
        param = default_param
    alpha142 = dv.add_formula('alpha142',"(((-1*Rank(Ts_Rank(close,%s)))*Rank(Delta(Delta(close,%s),%s)))*Rank(Ts_Rank((volume/Ts_Mean(volume,%s)),%s)))".format(10,1,1,20,5),is_quarterly=False,add_data=True)
	return alpha142
