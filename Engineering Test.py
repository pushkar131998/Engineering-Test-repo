import pandas as pd
def Engineering_Test(na_prod,asia_prod): 
    try:
        df_combined = pd.read_csv("combined.csv")
        print(df_combined)
        print(df_combined["Environment"])                                
        for iterator in df_combined['Environment']:
            split_records = iterator.split()
            split_records_result = map(str,split_records)
            final_record = ' '.join(list(split_records_result))
            print(final_record)
    

        result_na_prod = df_combined[df_combined["Environment"] == na_prod]["Environment"]
        result_na_list = result_na_prod.to_list()
        print('result na list',result_na_list)

        df_na_prod = pd.DataFrame({'Environment':result_na_list}).to_csv('NA Preview.csv')
        #print('NA Preview csv File :-',df_na_prod)
    

        result_asia_prod = df_combined[df_combined["Environment"] == asia_prod]["Environment"]
        result_asia_list = result_asia_prod.to_list()
        print('result asia prod',result_asia_list)

        df_asia_prod = pd.DataFrame({'Environment':result_asia_list}).to_csv('Asia Prod 4.csv')
        #print('Asia Prod 4 csv File :-',df_asia_prod)
    except:
        print("Error in the code")
    
na_prod = "NA Prod"
asia_prod = "Asia Prod"

if __name__ == "__main__":
    Engineering_Test(na_prod,asia_prod)
    
    