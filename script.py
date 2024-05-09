import api_worker
import chunks
import pandas


# reading input ips
with open('ip.txt') as file:
    input_ip_list = [line.strip() for line in file.readlines()]
    input_ip_list = list(set(input_ip_list))

# reading ips already in whitelist from confluence 
with open('white_list.txt') as file:
    confluence_ip_list = [line.strip() for line in file.readlines()]


input_ip_dataframe = pandas.DataFrame({
    'ip': input_ip_list,
    'organization': ['no organization'] * len(input_ip_list),
    'as': ['no as'] * len(input_ip_list),
    'country': ['no country'] * len(input_ip_list),
    'hostname': ['no hostname'] * len(input_ip_list),
    'description': ['None'] * len(input_ip_list),
    'status': ['fail'] * len(input_ip_list)
})

DESCRIPTION = "Добавлен в white list"

# Chunk list in lists of len == 100
chunked_input_ip_list = chunks.split_list_into_chunks(input_ip_list, 100)
ip_information = []
for chunk in chunked_input_ip_list:
    temp_ip_information = api_worker.work(chunk)
    ip_information += temp_ip_information

# list for ips not in confluence
ip_not_in_list = []


# Check white list for adding description
for ip in confluence_ip_list:
    if input_ip_dataframe['ip'].isin([ip]).any():
        input_ip_dataframe.loc[input_ip_dataframe['ip'] == ip, 'description'] = DESCRIPTION
    else:
        ip_not_in_list.append(ip)


for ip in ip_not_in_list:
    print(ip)


# adding information from api in pandas DF
for ip_info in ip_information:
    input_ip_dataframe.loc[input_ip_dataframe['ip'] == ip_info['ip'], 'country'] = ip_info['country']
    input_ip_dataframe.loc[input_ip_dataframe['ip'] == ip_info['ip'], 'organization'] = ip_info['organization']
    input_ip_dataframe.loc[input_ip_dataframe['ip'] == ip_info['ip'], 'as'] = ip_info['as']
    input_ip_dataframe.loc[input_ip_dataframe['ip'] == ip_info['ip'], 'hostname'] = ip_info['hostname']
    input_ip_dataframe.loc[input_ip_dataframe['ip'] == ip_info['ip'], 'status'] = ip_info['status']

# Exporting to excel
input_ip_dataframe.to_excel('ip.xlsx', index=False)