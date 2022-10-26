# In[1]:

import pandas as pd

# In[2]:

datedict = {'I': '18', 'J': '19', 'K': '20'}
strs = '123456789ABCDEFGHIJKLMNOPQRSTUV'
datedict2  = {}
for i in range(len(strs)):
    datedict2[strs[i]]=str(i+1)
    
def unpack_date(test):
    return datedict[test[0]] + test[1:3] +'-'+ datedict2[test[3]] +'-'+ datedict2[test[4]]


# In[3]:
cols = ['designation','H','G','epoch','M','omega','Omega','inc','ecc','n','a','U','ref','# obs','# opp','span1','span2','rms residual','coarse perturbers','fine perturbers','computer name','hex flags','full designation','last observation']


def read(path):

    file1 = open('mpcorb_extended.dat', 'r') #read file line by line
    count = 0
    output_index = 0
    #file has 3 sections, so we need 3 different output arrays
    data1 = []
    data2 = []
    data3 = []
    outputs = [data1,data2,data3]
    # Using for loop
    for line in file1:
        count += 1
        if count > 43: #ignore header
           try:
               name = line[0:7]
               H = line[8:13]
               G = line[14:19]
               epoch = line[20:25] #unpack later
               M = line[26:35]
               omega = line[37:46]
               Omega = line[48:57]
               inc = line[59:68]
               ecc = line[70:79]
               n = line[80:91]
               a = line[92:103]
               uncert = line[105]
               ref = line[107:116]
               nobs = line[117:122]
               nopp = line[123:126]
               first_or_arc = line[127:131]
               last_or_arc = line[132:136]
               rms_res = line[137:141]
               pet1 = line[142:145]
               pet2 = line[146:149]
               computer_name = line[150:160]
               hex_flag = line[161:165]
               desg = line[166:194]
               last_obs =  line[194:202]
               row = [name,H,G,epoch,M,omega,Omega,inc,ecc,n,a,uncert,ref,nobs,nopp,first_or_arc,last_or_arc,rms_res,pet1,pet2,computer_name,hex_flag,desg,last_or_arc]
               outputs[output_index].append(row) #append to the right array            
           except IndexError as e:
               #if I reach a gap in the file, increment my output index,so I output to the new array
               output_index = output_index + 1





    df0 = pd.DataFrame(outputs[0],columns=cols)
    parsed_epochs = [pd.to_datetime(unpack_date(df0['epoch'].values[i])) for i in range(len(df0))] #unpack epochs (we won't bother unpacking the designations since they're not physical quantities)
    df0['epoch']= parsed_epochs

    numericcols = ['H','G','M','omega','Omega','inc','ecc','n','a','# obs','# opp','span1','span2','rms residual','last observation']
    for col in numericcols: #there will be gaps in some of the numerical columns - fill them with nans
        df0[col] = pd.to_numeric(df0[col], errors='coerce')
        
    df0 = df0.astype({'designation': 'string','H': 'float','G': 'float','M': 'float','omega': 'float',
              'Omega': 'float','inc': 'float','ecc': 'float','n': 'float','a': 'float',
              'U': 'string','ref': 'string','# obs': 'Int64','# opp': 'Int64',
              'span1': 'Int64','span2': 'Int64','rms residual': 'float','coarse perturbers': 'string', 
              'fine perturbers': 'string','computer name': 'string','hex flags': 'string',
              'full designation': 'string','last observation': 'Int64'}) #set reasonalbe dtypes for the output, int64 can handle nans


    df1 = pd.DataFrame(outputs[1],columns=cols)
    parsed_epochs = [pd.to_datetime(unpack_date(df1['epoch'].values[i])) for i in range(len(df1))] #unpack epochs (we won't bother unpacking the designations since they're not physical quantities)
    df1['epoch']= parsed_epochs

    numericcols = ['H','G','M','omega','Omega','inc','ecc','n','a','# obs','# opp','span1','span2','rms residual','last observation']
    for col in numericcols: #there will be gaps in some of the numerical columns - fill them with nans
        df1[col] = pd.to_numeric(df1[col], errors='coerce')
        
    df1 = df1.astype({'designation': 'string','H': 'float','G': 'float','M': 'float','omega': 'float',
              'Omega': 'float','inc': 'float','ecc': 'float','n': 'float','a': 'float',
              'U': 'string','ref': 'string','# obs': 'Int64','# opp': 'Int64',
              'span1': 'Int64','span2': 'Int64','rms residual': 'float','coarse perturbers': 'string', 
              'fine perturbers': 'string','computer name': 'string','hex flags': 'string',
              'full designation': 'string','last observation': 'Int64'}) #set reasonalbe dtypes for the output, int64 can handle nans


    df2 = pd.DataFrame(outputs[1],columns=cols)
    parsed_epochs = [pd.to_datetime(unpack_date(df2['epoch'].values[i])) for i in range(len(df2))] #unpack epochs (we won't bother unpacking the designations since they're not physical quantities)
    df2['epoch']= parsed_epochs

    numericcols = ['H','G','M','omega','Omega','inc','ecc','n','a','# obs','# opp','span1','span2','rms residual','last observation']
    for col in numericcols: #there will be gaps in some of the numerical columns - fill them with nans
        df2[col] = pd.to_numeric(df2[col], errors='coerce')
        
    df2 = df2.astype({'designation': 'string','H': 'float','G': 'float','M': 'float','omega': 'float',
              'Omega': 'float','inc': 'float','ecc': 'float','n': 'float','a': 'float',
              'U': 'string','ref': 'string','# obs': 'Int64','# opp': 'Int64',
              'span1': 'Int64','span2': 'Int64','rms residual': 'float','coarse perturbers': 'string', 
              'fine perturbers': 'string','computer name': 'string','hex flags': 'string',
              'full designation': 'string','last observation': 'Int64'}) #set reasonalbe dtypes for the output, int64 can handle nans

    return df0, df1, df2

