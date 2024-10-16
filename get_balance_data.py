#get balance data for all addresses vis Etherscan API and write to DataFrame 
from get_data import address_list

while len(address_list) > 0:
    for address in address_list:

        api_key = ""
        try: 
            response = requests.get(
                "https://api.etherscan.io/api?module=account&action=balance&address=" + address + "&tag=latest&apikey=" + api_key
            )

            response_json = json.loads(response.text)

            eth_balance = response_json["result"]
            eth_balance = int(eth_balance)/ (1E18)
            balance_list.append((address, eth_balance))
            address_list.remove(address)
            time.sleep(1)
            print(eth_balance)
        except:
            print('Error')
            print('List Length:'+str(len(address_list)))
df_balance = pd.DataFrame(balance_list, columns=['address', 'Balance'])
df_target_label = df_target_label.merge(df_balance, left_on= ['address'], right_on=['address'],how='left')
print('end')

#Function to return different labels based on value size similar to CASE statements in SQL
def get_balance_level(x):
    if x == 0:
        output = 'Small'
    elif x > 0 and x < 1000:
        output = 'Medium'
    elif x > 1000 and x < 100:
        output = 'Large'
    else: 
        output = 'Huge'

df_target_label['Balance_level'] = df_target_label['Balance'].round(2).apply(lambda x:get_balance_level(x))
df_target_label['Balance'] = df_target_label['Balance'].round(2).astype('string')
df_target_label['label'] = df_target_label['label']+' | '+ df_target_label['Balance'] +' ETH'
