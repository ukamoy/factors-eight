#type2  -  only use add_formula function with parameter
        
def run_formula(dv, param = None):
    RetainedEarningsPS = dv.add_formula('RetainedEarningsPS',"surplus_rsrv/total_share+undistributed_profit/total_share", is_quarterly=False, add_data=True)
    
    return RetainedEarningsPS
