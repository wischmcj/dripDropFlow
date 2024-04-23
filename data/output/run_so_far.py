


# from datetime import datetime
# import glob
# import os
# # Get a list of all the csv files in the target directory
# # files = glob.glob('../data/output/statistics/*.csv')
# files = glob.glob('/statistics/*.csv')


# # Read and combine all the csv files into a single dataframe
# # print(type(files[0]))
# # one_file_read = pd.read_csv(f)
# # print(f'{one_file_read}')
# # print(type(one_file_read))



# #Throws alot of warnings since the last column, time stamp gets dropped off since it doesnt have a col name
# def get_file_name_attrs(file_list,remove_zeros):
#     names = [(f,os.path.basename(f)) for f in file_list]
#     if remove_zeros: 
#         name_parts = [(name.split('_000000')[0], name.replace('_','_').split('_000000_')[1].replace('_statistics.csv','')) for f, name in names if '_000000_' in name]
#     else:
#         name_parts = [(name.split('_000000')[0] + '_000000', name.replace('_','_').split('_000000_')[1].replace('_statistics.csv','') ) for f, name in names if '_000000_' in name]
        
#     # print(name_parts)
#     return name_parts

# # get_file_name_attrs()

# # Read each csv file and store it in a dictionary with the file name as the key

# dfs_and_cases = get_file_name_attrs(files, remove_zeros = False)

# print(dfs_and_cases)
# # dfs = [None]*len(dfs_and_cases)

# file_names = []
# for idx, tup in enumerate(dfs_and_cases):
#     file_name, case_name, df = tup
#     df['file_name'] = file_name
#     df['case_name'] = case_name
#     dfs[idx] =df
#     file_names.append(file_name)

# print(dfs[0].columns)
# print(dfs[0])

# all_tree_stats = pd.concat(dfs)    
# print(len(all_tree_stats))
# all_tree_stats = all_tree_stats[all_tree_stats['case_name'] != '-1.5']
# arr = [x for x in all_tree_stats[['file_name', 'case_name']].values]
# tups = [(x, float(y)) for x,y in arr]

already_run = [[('Secrest28-31_000000', '1.34'), 
('Secrest32-06_000000', '-1.58'), 
('Secrest07-32_000000', '0.32'), 
('Secrest02-30_000000', '-0.2666'), 
('Secrest08-24c_000000', '-1.5'), 
('Secrest02-30_000000', '-1'), 
('Secrest03-12_000000', '-0.44'), 
('Secrest07-32_000000', '1.26'), 
('Secrest03-12_000000', '0.96'), 
('Secrest32-06_000000', '-0.82'), 
('Secrest10-08_000000', '0.4'), 
('Secrest32-14_000000', '-1.96'), 
('Secrest03-12_000000', '-0.3'), 
('Secrest10-08_000000', '0.1666'), 
('Secrest28-31_000000', '0.88'), 
('Secrest29-20_000000', '-1.96'), 
('Secrest32-06_000000', '-0.78'), 
('Secrest10-02_000000', '-1.64'), 
('Secrest03-12_000000', '0.12'), 
('Secrest07-32_000000', '0.1666'), 
('Secrest03-12_000000', '-1.48'), 
('Secrest24-03_000000', '-0.95'), 
('Secrest29-25_000000', '1.58'), 
('Secrest31-05_000000', '-1.88'), 
('Secrest03-12_000000', '-0.04'), 
('Secrest27-05_000000', '-0.32'), 
('Secrest02-30_000000', '-0.3'), 
('Secrest32-14_000000', '-2.04'), 
('Secrest24-07_000000', '-1.34'), 
('Secrest08-24c_000000', '-0.88'), 
('Secrest31-05_000000', '1.42'), 
('Secrest27-05_000000', '0.38'), 
('Secrest32-03_000000', '1.5'), 
('Secrest32-06_000000', '0.7'), 
('Secrest29-25_000000', '-1.5'), 
('Secrest24-07_000000', '-0.88'), 
('Secrest10-08_000000', '-0.64'), 
('Secrest08-24c_000000', '1.58'), 
('Secrest32-06_000000', '0.26'), 
('Secrest26-03_000000', '-1.96'), 
('Secrest29-20_000000', '0.96'), 
('Secrest29-25_000000', '-1.34'), 
('Secrest32-06_000000', '0.82'), 
('Secrest02-30_000000', '-1.34'), 
('Secrest08-24c_000000', '0.8'), 
('Secrest32-06_000000', '-0.96'), 
('Secrest32-06_000000', '0.28'), 
('Secrest31-05_000000', '1.72'), 
('Secrest10-08_000000', '-0.4'), 
('Secrest07-32_000000', '-1'), 
('Secrest23-23_000000', '0'), 
('Secrest32-14_000000', '0.4'), 
('Secrest28-31_000000', '-1.8'), 
('Secrest02-30_000000', '1.64'), 
('Secrest02-30_000000', '-1.42'), 
('Secrest26-03_000000', '-2.04'), 
('Secrest02-30_000000', '-0.16666'), 
('Secrest03-12_000000', '-0.2'), 
('Secrest07-32_000000', '-1.72'), 
('Secrest29-20_000000', '-1.66'), 
('Secrest03-12_000000', '-0.48'), 
('Secrest31-05_000000', '0.24'), 
('Secrest02-26_000000', '0'), 
('Secrest08-24c_000000', '-1.34'), 
('Secrest24-07_000000', '-1.64'), 
('Secrest27-05_000000', '-0.66'), 
('Secrest32-01_000000', '-1.72'), 
('Secrest29-25_000000', '-1.66'), 
('Secrest32-03_000000', '-0.0666'), 
('Secrest10-02_000000', '-1.02'), 
('Secrest29-20_000000', '0.08'), 
('Secrest32-03_000000', '-0.16666'), 
('Secrest29-20_000000', '0.72'), 
('Secrest26-03_000000', '-0.64'), 
('Secrest29-20_000000', '-0.48'), 
('Secrest29-20_000000', '-1.58'), 
('Secrest07-32_000000', '-0.24'), 
('Secrest29-25_000000', '-0.4'), 
('Secrest31-05_000000', '-2'), 
('Secrest31-05_000000', '-1.02'), 
('Secrest08-24c_000000', '0.56'), 
('Secrest10-08_000000', '0.24'), 
('Secrest24-03_000000', '-0.0666'), 
('Secrest32-06_000000', '0.3666'), 
('Secrest26-03_000000', '-1.34'), 
('Secrest32-06_000000', '-1.88'), 
('Secrest10-02_000000', '0'), 
('Secrest10-08_000000', '-0.3'), 
('Secrest07-32_000000', '1.66'), 
('Secrest27-05_000000', '-1.0'), 
('Secrest27-05_000000', '1.18'), 
('Secrest26-03_000000', '1.1'), 
('Secrest24-07_000000', '1.42'), 
('Secrest32-01_000000', '1.42'), 
('Secrest32-03_000000', '-0.72'), 
('Secrest31-05_000000', '0.08'), 
('Secrest27-05_000000', '0.8'), 
('Secrest29-20_000000', '-1.72'), 
('Secrest18-13_000000', '-0.16666'), 
('Secrest02-30_000000', '-0.48'), 
('Secrest32-06_000000', '0.76'), 
('Secrest08-24c_000000', '-0.8'), 
('Secrest32-14_000000', '-0.3'), 
('Secrest32-14_000000', '-1.5'), 
('Secrest31-05_000000', '-1.1'), 
('Secrest32-14_000000', '-1.8'), 
('Secrest24-07_000000', '-1.80'), 
('Secrest02-30_000000', '0.1666'), 
('Secrest10-02_000000', '-0.16666'), 
('Secrest02-30_000000', '1.66'), 
('Secrest11-27_000000', '0.56666'), 
('Secrest24-03_000000', '0.4'), 
('Secrest08-24c_000000', '1.72'), 
('Secrest03-12_000000', '-0.08'), 
('Secrest02-30_000000', '0'), 
('Secrest26-03_000000', '1.5'), 
('Secrest29-25_000000', '0.08'), 
('Secrest27-05_000000', '-0.08'), 
('Secrest24-03_000000', '0.3'), 
('Secrest02-30_000000', '0.08'), 
('Secrest11-27_000000', '-2.0'), 
('Secrest31-05_000000', '0.16'), 
('Secrest24-07_000000', '-0.56'), 
('Secrest14-09_000000', '-1.5'), 
('Secrest03-12_000000', '0.56'), 
('Secrest31-05_000000', '0.56'), 
('Secrest24-07_000000', '-1.96'), 
('Secrest02-30_000000', '1.34'), 
('Secrest11-27_000000', '0.4'), 
('Secrest31-05_000000', '-1.34'), 
('Secrest32-03_000000', '0.64'), 
('Secrest27-05_000000', '1.4'), 
('Secrest14-09_000000', '-0.0666'), 
('Secrest32-14_000000', '0.1666'), 
('Secrest29-20_000000', '0.1666'), 
('Secrest29-20_000000', '-1.64'), 
('Secrest31-05_000000', '1.58'), 
('Secrest27-05_000000', '0.82'), 
('Secrest32-14_000000', '-0.16'), 
('Secrest03-12_000000', '-1.12'), 
('Secrest32-06_000000', '1.4'), 
('Secrest31-05_000000', '0.4'), 
('Secrest31-05_000000', '-0.16'), 
('Secrest31-05_000000', '-0.56'), 
('Secrest16-14LI-ST_000000', '-1.5'), 
('Secrest07-32_000000', '-0.72'), 
('Secrest28-31_000000', '0.8'), 
('Secrest11-27_000000', '0.3'), 
('Secrest10-08_000000', '2.04'), 
('Secrest10-02_000000', '-0.72'), 
('Secrest02-30_000000', '0.16'), 
('Secrest10-02_000000', '0.08'), 
('Secrest07-32_000000', '-1.26'), 
('Secrest27-05_000000', '0.56666'), 
('Secrest29-25_000000', '-0.08'), 
('Secrest24-07_000000', '-0.80'), 
('Secrest24-03_000000', '0.36666'), 
('Secrest10-02_000000', '-1.34'), 
('Secrest32-03_000000', '0.1666'), 
('Secrest31-05_000000', '-0.24'), 
('Secrest03-12_000000', '0.88'), 
('Secrest29-25_000000', '1.64'), 
('Secrest29-25_000000', '1.26'), 
('Secrest02-26_000000', '-1.5'), 
('Secrest29-20_000000', '0'), 
('Secrest32-14_000000', '1.34'), 
('Secrest31-05_000000', '1.5'), 
('Secrest08-24c_000000', '-0.56'), 
('Secrest29-20_000000', '1.72'), 
('Secrest27-05_000000', '-0.72'), 
('Secrest08-24c_000000', '-0.08'), 
('Secrest32-06_000000', '-1.4'), 
('Secrest32-06_000000', '0.04'), 
('Secrest32-06_000000', '0.12'), 
('Secrest31-05_000000', '-0.16666'), 
('Secrest29-25_000000', '1.34'), 
('Secrest29-20_000000', '1.18'), 
('Secrest26-03_000000', '-0.88'), 
('Secrest02-26_000000', '-0.16666'), 
('Secrest16-3TI-CO_000000', '-1.5'), 
('Secrest24-07_000000', '-1.5'), 
('Secrest24-07_000000', '-0.40'), 
('Secrest32-03_000000', '-0.96'), 
('Secrest10-08_000000', '0.64'), 
('Secrest28-31_000000', '-1.1'), 
('Secrest10-02_000000', '-0.32'), 
('Secrest28-31_000000', '-0.08'), 
('Secrest03-12_000000', '1.5'), 
('Secrest28-31_000000', '-0.88'), 
('Secrest24-07_000000', '1.10'), 
('Secrest32-06_000000', '-0.34'), 
('Secrest03-12_000000', '0'), 
('Secrest27-05_000000', '-0.7'), 
('Secrest03-12_000000', '0.4'), 
('Secrest31-05_000000', '0.8'), 
('Secrest02-30_000000', '-0.08'), 
('Secrest31-05_000000', '-1'), 
('Secrest24-07_000000', '0.64'), 
('Secrest08-24c_000000', '0.88'), 
('Secrest32-14_000000', '0.08'), 
('Secrest32-14_000000', '0'), 
('Secrest03-12_000000', '1.1'), 
('Secrest26-03_000000', '-0.4'), 
('Secrest24-07_000000', '0.88'), 
('Secrest27-05_000000', '1.42'), 
('Secrest32-06_000000', '0.08'), 
('Secrest10-02_000000', '-0.64'), 
('Secrest10-08_000000', '0.72'), 
('Secrest10-08_000000', '-0.72'), 
('Secrest29-25_000000', '1.5'), 
('Secrest32-03_000000', '-1.5'), 
('Secrest27-05_000000', '-0.96'), 
('Secrest16-14LI-ST_000000', '0'), 
('Secrest14-09_000000', '-1'), 
('Secrest27-05_000000', '-0.56'), 
('Secrest10-08_000000', '-0.8'), 
('Secrest32-06_000000', '-0.12'), 
('Secrest28-31_000000', '-0.8'), 
('Secrest29-20_000000', '-1.5'), 
('Secrest26-03_000000', '-1.5'), 
('Secrest32-01_000000', '-1.42'), 
('Secrest02-30_000000', '-1.72'), 
('Secrest03-12_000000', '-0.16666'), 
('Secrest24-07_000000', '0.32'), 
('Secrest29-25_000000', '-0.66'), 
('Secrest27-05_000000', '-0.14'), 
('Secrest10-08_000000', '-0.24'), 
('Secrest32-03_000000', '0.4'), 
('Secrest10-08_000000', '-1.1'), 
('Secrest26-03_000000', '1.18'), 
('Secrest07-32_000000', '1.34'), 
('Secrest03-12_000000', '0.1666'), 
('Secrest27-05_000000', '1.5'), 
('Secrest28-31_000000', '-1.58'), 
('Secrest07-32_000000', '-0.16'), 
('Secrest03-12_000000', '-0.4'), 
('Secrest31-05_000000', '-1.5'), 
('Secrest07-32_000000', '0.8'), 
('Secrest03-12_000000', '-1.4'), 
('Secrest10-08_000000', '0.48'), 
('Secrest32-01_000000', '-0.4'), 
('Secrest28-31_000000', '1.02'), 
('Secrest10-02_000000', '-0.88'), 
('Secrest08-24c_000000', '-0.16666'), 
('Secrest24-03_000000', '0.56666'), 
('Secrest07-32_000000', '-1.64'), 
('Secrest10-02_000000', '0.46666'), 
('Secrest02-30_000000', '-0.12'), 
('Secrest31-05_000000', '0.1666'), 
('Secrest03-12_000000', '-1.04'), 
('Secrest03-12_000000', '-1.36'), 
('Secrest18-13_000000', '-2.5'), 
('Secrest27-05_000000', '0.88'), 
('Secrest07-32_000000', '-0.8'), 
('Secrest03-12_000000', '1.26'), 
('Secrest29-25_000000', '-0.32'), 
('Secrest32-01_000000', '-1.5'), 
('Secrest27-05_000000', '0.36666'), 
('Secrest23-23_000000', '-0.3'), 
('Secrest32-14_000000', '0.96'), 
('Secrest02-30_000000', '-0.4'), 
('Secrest28-31_000000', '-0.56'), 
('Secrest31-05_000000', '1.66'), 
('Secrest32-06_000000', '0.5'), 
('Secrest03-12_000000', '-1.08'), 
('Secrest32-03_000000', '-0.56'), 
('Secrest16-3TI-CO_000000', '-0.3'), 
('Secrest02-30_000000', '-1.26'), 
('Secrest26-03_000000', '0.72'), 
('Secrest32-03_000000', '-0.2666'), 
('Secrest29-20_000000', '-1.42'), 
('Secrest29-20_000000', '1.34'), 
('Secrest10-02_000000', '0.88'), 
('Secrest24-03_000000', '-2.5'), 
('Secrest24-03_000000', '-0.3'), 
('Secrest31-05_000000', '-0.64'), 
('Secrest26-03_000000', '0.96'), 
('Secrest24-07_000000', '0.48'), 
('Secrest26-03_000000', '1.02'), 
('Secrest26-03_000000', '1.26'), 
('Secrest27-05_000000', '-1.34'), 
('Secrest07-32_000000', '0'), 
('Secrest29-20_000000', '0.4'), 
('Secrest26-03_000000', '1.42'), 
('Secrest29-25_000000', '1.02'), 
('Secrest32-06_000000', '-0.48'), 
('Secrest32-06_000000', '-4'), 
('Secrest10-08_000000', '0.56'), 
('Secrest32-06_000000', '0.68'), 
('Secrest32-06_000000', '0.4'), 
('Secrest27-05_000000', '0.2'), 
('Secrest24-07_000000', '1.18'), 
('Secrest32-06_000000', '0.14'), 
('Secrest32-06_000000', '-1.34'), 
('Secrest27-05_000000', '0.04'), 
('Secrest29-25_000000', '0.96'), 
('Secrest27-05_000000', '1.2'), 
('Secrest02-30_000000', '0.56'), 
('Secrest02-30_000000', '-0.8'), 
('Secrest03-12_000000', '-1.1'), 
('Secrest28-31_000000', '-0.16'), 
('Secrest29-25_000000', '1.8'), 
('Secrest02-30_000000', '0.48'), 
('Secrest32-06_000000', '-0.56'), 
('Secrest02-26_000000', '-0.3'), 
('Secrest31-05_000000', '0.64'), 
('Secrest27-05_000000', '-0.58'), 
('Secrest27-05_000000', '-1.64'), 
('Secrest32-06_000000', '-1.1'), 
('Secrest31-05_000000', '1.34'), 
('Secrest27-05_000000', '-0.38'), 
('Secrest26-03_000000', '0.0'), 
('Secrest07-32_000000', '-1.58'), 
('Secrest29-25_000000', '-1.64'), 
('Secrest27-05_000000', '-1.44'), 
('Secrest32-03_000000', '0.8'), 
('Secrest29-25_000000', '-1.26'), 
('Secrest26-03_000000', '-1.18'), 
('Secrest29-25_000000', '-1.58'), 
('Secrest28-31_000000', '0.32'), 
('Secrest32-03_000000', '-1.34'), 
('Secrest27-05_000000', '0'), 
('Secrest26-03_000000', '-1.88'), 
('Secrest32-06_000000', '-0.42'), 
('Secrest02-30_000000', '-1.58'), 
('Secrest07-32_000000', '0.96'), 
('Secrest28-31_000000', '-0.24'), 
('Secrest16-14LI-ST_000000', '-0.16666'), 
('Secrest10-02_000000', '-0.08'), 
('Secrest10-02_000000', '-0.2666'), 
('Secrest29-25_000000', '0.88'), 
('Secrest08-24c_000000', '-1.1'), 
('Secrest08-24c_000000', '-0.3'), 
('Secrest08-24c_000000', '1.66'), 
('Secrest23-23_000000', '-0.16666'), 
('Secrest16-3TI-CO_000000', '-1'), 
('Secrest29-25_000000', '-1.1'), 
('Secrest03-12_000000', '0.8'), 
('Secrest32-06_000000', '-0.28'), 
('Secrest29-20_000000', '1.26'), 
('Secrest28-31_000000', '1.5'), 
('Secrest10-02_000000', '-0.16'), 
('Secrest32-06_000000', '-1.5'), 
('Secrest07-32_000000', '1.42'), 
('Secrest10-02_000000', '0.16'), 
('Secrest28-31_000000', '-0.48'), 
('Secrest28-31_000000', '0.4'), 
('Secrest02-30_000000', '1.72'), 
('Secrest29-25_000000', '0.56'), 
('Secrest24-07_000000', '1.50'), 
('Secrest28-31_000000', '0.72'), 
('Secrest32-06_000000', '-0.08'), 
('Secrest32-06_000000', '-0.44'), 
('Secrest08-24c_000000', '-1.72'), 
('Secrest29-20_000000', '0.8'), 
('Secrest26-03_000000', '-0.96'), 
('Secrest10-02_000000', '0.96'), 
('Secrest27-05_000000', '-1.02'), 
('Secrest02-30_000000', '-1.64'), 
('Secrest10-02_000000', '-2.0'), 
('Secrest26-03_000000', '-1.72'), 
('Secrest32-06_000000', '-0.8'), 
('Secrest07-32_000000', '-1.18'), 
('Secrest18-13_000000', '-0.95'), 
('Secrest07-32_000000', '0.16'), 
('Secrest29-20_000000', '-0.0666'), 
('Secrest32-06_000000', '-0.06'), 
('Secrest32-06_000000', '-0.22'), 
('Secrest26-03_000000', '-0.72'), 
('Secrest08-24c_000000', '1.64'), 
('Secrest24-07_000000', '-1.18'), 
('Secrest26-03_000000', '0.32'), 
('Secrest32-14_000000', '-1.1'), 
('Secrest28-31_000000', '0.48'), 
('Secrest32-06_000000', '-0.16'), 
('Secrest27-05_000000', '0.42'), 
('Secrest32-14_000000', '0.72'), 
('Secrest07-32_000000', '0.72'), 
('Secrest10-02_000000', '-0.48'), 
('Secrest27-05_000000', '-1.42'), 
('Secrest28-31_000000', '0.96'), 
('Secrest32-06_000000', '-0.1'), 
('Secrest10-08_000000', '-0.16'), 
('Secrest29-20_000000', '0.32'), 
('Secrest29-20_000000', '-0.32'), 
('Secrest26-03_000000', '-1.64'), 
('Secrest32-03_000000', '-0.64'), 
('Secrest07-32_000000', '0.64'), 
('Secrest32-14_000000', '0.56'), 
('Secrest08-24c_000000', '-0.72'), 
('Secrest08-24c_000000', '1.5'), 
('Secrest10-02_000000', '-1.42'), 
('Secrest10-02_000000', '-2.5'), 
('Secrest32-06_000000', '-0.18'), 
('Secrest24-07_000000', '0.08'), 
('Secrest07-32_000000', '1.58'), 
('Secrest29-20_000000', '-1.18'), 
('Secrest29-25_000000', '-0.8'), 
('Secrest02-30_000000', '-0.16'), 
('Secrest32-03_000000', '-1.42'), 
('Secrest03-12_000000', '-0.72'), 
('Secrest32-03_000000', '-0.88'), 
('Secrest31-05_000000', '-0.48'), 
('Secrest10-08_000000', '0.16'), 
('Secrest27-05_000000', '-0.3'), 
('Secrest32-06_000000', '0.64'), 
('Secrest11-27_000000', '-0.16666'), 
('Secrest31-05_000000', '-0.4'), 
('Secrest26-03_000000', '0.8'), 
('Secrest02-26_000000', '-1'), 
('Secrest29-25_000000', '-0.64'), 
('Secrest31-05_000000', '-1.72'), 
('Secrest24-07_000000', '0.16'), 
('Secrest29-25_000000', '-0.96'), 
('Secrest07-32_000000', '-0.48'), 
('Secrest08-24c_000000', '-0.24'), 
('Secrest10-08_000000', '-0.0666'), 
('Secrest14-09_000000', '0.1666'), 
('Secrest32-06_000000', '0.8'), 
('Secrest02-30_000000', '0.96'), 
('Secrest27-05_000000', '-0.33333'), 
('Secrest29-25_000000', '1.1'), 
('Secrest29-20_000000', '1.02'), 
('Secrest29-25_000000', '-0.72'), 
('Secrest27-05_000000', '-0.28'), 
('Secrest02-30_000000', '0.72'), 
('Secrest32-06_000000', '0.56666'), 
('Secrest10-02_000000', '1.02'), 
('Secrest29-20_000000', '-1.26'), 
('Secrest32-06_000000', '-0.62'), 
('Secrest18-13_000000', '-0.2666'), 
('Secrest10-02_000000', '1.5'), 
('Secrest28-31_000000', '1.18'), 
('Secrest27-05_000000', '0.1'), 
('Secrest32-03_000000', '1.18'), 
('Secrest26-03_000000', '-1.8'), 
('Secrest18-13_000000', '-2.0'), 
('Secrest10-02_000000', '-1.72'), 
('Secrest32-06_000000', '-0.36666'), 
('Secrest32-03_000000', '0.16'), 
('Secrest08-24c_000000', '0.24'), 
('Secrest03-12_000000', '-0.76'), 
('Secrest29-20_000000', '1.58'), 
('Secrest28-31_000000', '-1.64'), 
('Secrest32-06_000000', '1.34'), 
('Secrest07-32_000000', '-0.64'), 
('Secrest10-08_000000', '-1.26'), 
('Secrest32-01_000000', '0.32'), 
('Secrest29-20_000000', '1.8'), 
('Secrest27-05_000000', '-0.44'), 
('Secrest02-30_000000', '1.5'), 
('Secrest10-02_000000', '0.8'), 
('Secrest31-05_000000', '-1.8'), 
('Secrest10-02_000000', '-0.8'), 
('Secrest16-14LI-ST_000000', '-0.3'), 
('Secrest24-07_000000', '-0.32'), 
('Secrest02-30_000000', '-0.24'), 
('Secrest32-06_000000', '-1.64'), 
('Secrest27-05_000000', '-1.8'), 
('Secrest32-06_000000', '-1.96'), 
('Secrest10-02_000000', '-1.66'), 
('Secrest02-30_000000', '-1.8'), 
('Secrest26-03_000000', '-0.24'), 
('Secrest27-05_000000', '-0.95'), 
('Secrest26-03_000000', '0.88'), 
('Secrest32-06_000000', '0.16'), 
('Secrest28-31_000000', '-0.4'), 
('Secrest32-01_000000', '-1.26'), 
('Secrest31-05_000000', '-0.82'), 
('Secrest16-3TI-CO_000000', '0'), 
('Secrest29-20_000000', '-2.04'), 
('Secrest08-24c_000000', '0.96'), 
('Secrest24-07_000000', '-1.10'), 
('Secrest27-05_000000', '1.02'), 
('Secrest26-03_000000', '1.34'), 
('Secrest26-03_000000', '-0.48'), 
('Secrest32-06_000000', '-1.18'), 
('Secrest24-03_000000', '0.1666'), 
('Secrest10-02_000000', '1.8'), 
('Secrest29-25_000000', '0.48'), 
('Secrest32-03_000000', '-2.5'), 
('Secrest10-02_000000', '-0.4'), 
('Secrest32-03_000000', '-2'), 
('Secrest32-03_000000', '-1.96'), 
('Secrest32-06_000000', '-0.2'), 
('Secrest10-08_000000', '-0.88'), 
('Secrest29-25_000000', '-1.02'), 
('Secrest11-27_000000', '0.36666'), 
('Secrest31-05_000000', '1.02'), 
('Secrest32-06_000000', '-0.14'), 
('Secrest27-05_000000', '-0.9'), 
('Secrest32-06_000000', '0.3'), 
('Secrest29-20_000000', '-0.08'), 
('Secrest10-02_000000', '-0.96'), 
('Secrest10-08_000000', '1.18'), 
('Secrest11-27_000000', '-0.95'), 
('Secrest32-06_000000', '0'), 
('Secrest27-05_000000', '0.48'), 
('Secrest11-27_000000', '-0.0666'), 
('Secrest27-05_000000', '-0.64'), 
('Secrest10-08_000000', '1.26'), 
('Secrest03-12_000000', '-0.16'), 
('Secrest03-12_000000', '0.08'), 
('Secrest29-20_000000', '-0.8'), 
('Secrest24-07_000000', '0.80'), 
('Secrest10-02_000000', '1.34'), 
('Secrest10-08_000000', '0.88'), 
('Secrest32-06_000000', '0.24'), 
('Secrest18-13_000000', '0.36666'), 
('Secrest10-02_000000', '-1.5'), 
('Secrest02-30_000000', '1.42'), 
('Secrest29-25_000000', '1.18'), 
('Secrest02-30_000000', '-0.88'), 
('Secrest29-25_000000', '-0.24'), 
('Secrest08-24c_000000', '-1.58'), 
('Secrest07-32_000000', '-0.56'), 
('Secrest02-30_000000', '0.88'), 
('Secrest14-09_000000', '0'), 
('Secrest31-05_000000', '-0.3'), 
('Secrest26-03_000000', '-1.58'), 
('Secrest03-12_000000', '0.64'), 
('Secrest31-05_000000', '-1.66'), 
('Secrest32-06_000000', '-1.8'), 
('Secrest32-03_000000', '-1.64'), 
('Secrest03-12_000000', '-0.32'), 
('Secrest10-02_000000', '-0.24'), 
('Secrest03-12_000000', '1.64'), 
('Secrest24-07_000000', '0.56'), 
('Secrest03-12_000000', '-1.42'), 
('Secrest31-05_000000', '-0.72'), 
('Secrest10-02_000000', '0.56'), 
('Secrest27-05_000000', '-0.46'), 
('Secrest29-20_000000', '-0.16'), 
('Secrest24-07_000000', '0.96'), 
('Secrest29-25_000000', '1.42'), 
('Secrest29-25_000000', '-0.3'), 
('Secrest31-05_000000', '-0.08'), 
('Secrest07-32_000000', '-0.08'), 
('Secrest10-02_000000', '0.64'), 
('Secrest16-14LI-ST_000000', '-1'), 
('Secrest03-12_000000', '0.16'), 
('Secrest07-32_000000', '-0.16666'), 
('Secrest32-06_000000', '0.88'), 
('Secrest10-08_000000', '-0.32'), 
('Secrest28-31_000000', '-1.5'), 
('Secrest32-06_000000', '0.78'), 
('Secrest28-31_000000', '0'), 
('Secrest27-05_000000', '-1.96'), 
('Secrest29-25_000000', '-1.8'), 
('Secrest29-25_000000', '-1.42'), 
('Secrest32-06_000000', '0.42'), 
('Secrest23-23_000000', '0.1666'), 
('Secrest27-05_000000', '1.26'), 
('Secrest02-30_000000', '1.18'), 
('Secrest29-25_000000', '1.66'), 
('Secrest28-31_000000', '0.08'), 
('Secrest02-30_000000', '-1.1'), 
('Secrest24-03_000000', '0.46666'), 
('Secrest32-06_000000', '-0.24'), 
('Secrest32-01_000000', '0.1666'), 
('Secrest28-31_000000', '-1.42'), 
('Secrest31-05_000000', '-1.26'), 
('Secrest24-07_000000', '-1'), 
('Secrest32-06_000000', '-0.72'), 
('Secrest29-25_000000', '0.72'), 
('Secrest28-31_000000', '-1.18'), 
('Secrest24-03_000000', '-0.26666'), 
('Secrest02-30_000000', '-1.5'), 
('Secrest03-12_000000', '0.72'), 
('Secrest32-06_000000', '-2.0'), 
('Secrest28-31_000000', '-0.72'), 
('Secrest03-12_000000', '-0.92'), 
('Secrest08-24c_000000', '0.1666'), 
('Secrest32-14_000000', '-0.56'), 
('Secrest27-05_000000', '0.32'), 
('Secrest07-32_000000', '-1.34'), 
('Secrest32-06_000000', '0.66'), 
('Secrest28-31_000000', '-0.64'), 
('Secrest27-05_000000', '0.92'), 
('Secrest08-24c_000000', '-1.64'), 
('Secrest10-08_000000', '0.08'), 
('Secrest29-20_000000', '1.5'), 
('Secrest10-08_000000', '-1'), 
('Secrest08-24c_000000', '0.32'), 
('Secrest24-07_000000', '-0.48'), 
('Secrest32-06_000000', '-0.46'), 
('Secrest10-02_000000', '1.72'), 
('Secrest27-05_000000', '-1.1'), 
('Secrest08-24c_000000', '-1.8'), 
('Secrest24-03_000000', '-0.9'), 
('Secrest08-24c_000000', '0.4'), 
('Secrest31-05_000000', '1.8'), 
('Secrest10-08_000000', '-0.08'), 
('Secrest10-02_000000', '1.64'), 
('Secrest03-12_000000', '-0.24'), 
('Secrest32-06_000000', '0.44'), 
('Secrest16-3TI-CO_000000', '0.1666'), 
('Secrest28-31_000000', '-1.02'), 
('Secrest31-05_000000', '1.26'), 
('Secrest10-02_000000', '0.1666'), 
('Secrest28-31_000000', '-1.72'), 
('Secrest10-08_000000', '-1.5'), 
('Secrest29-20_000000', '-0.82'), 
('Secrest02-30_000000', '-1.02'), 
('Secrest14-09_000000', '-0.16666'), 
('Secrest27-05_000000', '-0.42'), 
('Secrest27-05_000000', '0.46'), 
('Secrest26-03_000000', '0.48'), 
('Secrest16-14LI-ST_000000', '0.1666'), 
('Secrest32-06_000000', '-0.9'), 
('Secrest27-05_000000', '-1.4'), 
('Secrest08-24c_000000', '-1'), 
('Secrest18-13_000000', '-1'), 
('Secrest27-05_000000', '-0.36'), 
('Secrest32-06_000000', '0.36666'), 
('Secrest31-05_000000', '1.18'), 
('Secrest24-03_000000', '-1'), 
('Secrest08-24c_000000', '-1.02'), 
('Secrest32-06_000000', '0.84'), 
('Secrest29-20_000000', '1.66'), 
('Secrest27-05_000000', '0.76'), 
('Secrest27-05_000000', '-0.16'), 
('Secrest29-20_000000', '0.56'), 
('Secrest31-05_000000', '-0.66'), 
('Secrest32-06_000000', '-0.26'), 
('Secrest32-06_000000', '-0.95'), 
('Secrest31-05_000000', '0.48'), 
('Secrest32-06_000000', '-2.5'), 
('Secrest02-30_000000', '0.8'), 
('Secrest03-12_000000', '-0.52'), 
('Secrest10-08_000000', '1.5'), 
('Secrest32-06_000000', '0.56'), 
('Secrest32-01_000000', '0.56'), 
('Secrest02-30_000000', '-0.1'), 
('Secrest28-31_000000', '1.1'), 
('Secrest02-30_000000', '0.24'), 
('Secrest02-30_000000', '0.4'), 
('Secrest10-02_000000', '1.18'), 
('Secrest32-06_000000', '-0.68'), 
('Secrest10-02_000000', '0.48'), 
('Secrest32-06_000000', '0.02'), 
('Secrest03-12_000000', '-1.64'), 
('Secrest29-25_000000', '-1.88'), 
('Secrest10-02_000000', '1.26'), 
('Secrest26-03_000000', '0.64'), 
('Secrest07-32_000000', '-1.5'), 
('Secrest08-24c_000000', '0.48'), 
('Secrest26-03_000000', '-0.56'), 
('Secrest26-03_000000', '-0.32'), 
('Secrest29-25_000000', '-1.96'), 
('Secrest24-07_000000', '-0.64'), 
('Secrest03-12_000000', '-1.32'), 
('Secrest29-20_000000', '0.64'), 
('Secrest10-08_000000', '-0.16666'), 
('Secrest27-05_000000', '-0.48'), 
('Secrest07-32_000000', '-1.42'), 
('Secrest07-32_000000', '0.88'), 
('Secrest07-32_000000', '1.1'), 
('Secrest27-05_000000', '0.3'), 
('Secrest27-05_000000', '-0.4'), 
('Secrest32-06_000000', '1.5'), 
('Secrest08-24c_000000', '-0.96'), 
('Secrest32-06_000000', '1.18'), 
('Secrest27-05_000000', '-0.8'), 
('Secrest14-09_000000', '-0.3'), 
('Secrest32-06_000000', '-0.04'), 
('Secrest10-08_000000', '0.96'), 
('Secrest29-20_000000', '0.88'), 
('Secrest08-24c_000000', '-0.64'), 
('Secrest27-05_000000', '-0.5666'), 
('Secrest27-05_000000', '0.84'), 
('Secrest32-03_000000', '0.56'), 
('Secrest10-02_000000', '-1.1'), 
('Secrest10-08_000000', '1.34'), 
('Secrest29-25_000000', '-1.72'), 
('Secrest24-07_000000', '-2.04'), 
('Secrest02-30_000000', '-0.64'), 
('Secrest11-27_000000', '-1'), 
('Secrest29-20_000000', '0.16'), 
('Secrest11-27_000000', '0.5'), 
('Secrest03-12_000000', '-1.8'), 
('Secrest18-13_000000', '0.4'), 
('Secrest10-02_000000', '-0.95'), 
('Secrest32-06_000000', '-0.02'), 
('Secrest32-06_000000', '1.2'), 
('Secrest31-05_000000', '-0.8'), 
('Secrest29-25_000000', '0.16'), 
('Secrest24-07_000000', '-0.72'), 
('Secrest31-05_000000', '-1.58'), 
('Secrest29-25_000000', '0.24'), 
('Secrest27-05_000000', '-0.06'), 
('Secrest31-05_000000', '0.88'), 
('Secrest03-12_000000', '1.42'), 
('Secrest11-27_000000', '0.1666'), 
('Secrest31-05_000000', '-1.96'), 
('Secrest32-06_000000', '0.46'), 
('Secrest08-24c_000000', '-0.4'), 
('Secrest27-05_000000', '-0.82'), 
('Secrest23-23_000000', '-1.5'), 
('Secrest07-32_000000', '-0.32'), 
('Secrest24-07_000000', '0.1666'), 
('Secrest08-24c_000000', '-1.66'), 
('Secrest03-12_000000', '-1.5'), 
('Secrest02-30_000000', '1.26'), 
('Secrest32-03_000000', '1.34'), 
('Secrest27-05_000000', '-1.26'), 
('Secrest03-12_000000', '-0.96'), 
('Secrest03-12_000000', '0.48'), 
('Secrest29-20_000000', '-0.56'), 
('Secrest26-03_000000', '-1.1'), 
('Secrest27-05_000000', '0.46666'), 
('Secrest24-07_000000', '-1.88'), 
('Secrest02-30_000000', '1.58'), 
('Secrest27-05_000000', '0.1666'), 
('Secrest08-24c_000000', '0.16'), 
('Secrest28-31_000000', '-1.88'), 
('Secrest27-05_000000', '0.74'), 
('Secrest32-06_000000', '-0.32'), 
('Secrest32-06_000000', '0.36'), 
('Secrest31-05_000000', '-0.32'), 
('Secrest27-05_000000', '1.1'), 
('Secrest32-01_000000', '1.02'), 
('Secrest32-14_000000', '-0.4'), 
('Secrest07-32_000000', '-0.4'), 
('Secrest26-03_000000', '0.08'), 
('Secrest03-12_000000', '-0.64'), 
('Secrest29-25_000000', '-0.74'), 
('Secrest32-06_000000', '2.04'), 
('Secrest32-06_000000', '-0.4'), 
('Secrest29-20_000000', '-1.34'), 
('Secrest31-05_000000', '-1.18'), 
('Secrest31-05_000000', '-0.74'), 
('Secrest08-24c_000000', '0'), 
('Secrest26-03_000000', '-0.8'), 
('Secrest10-02_000000', '-1.8'), 
('Secrest10-02_000000', '-1'), 
('Secrest27-05_000000', '-0.12'), 
('Secrest18-13_000000', '-0.9'), 
('Secrest18-13_000000', '-1.5'), 
('Secrest27-05_000000', '-0.16666'), 
('Secrest32-06_000000', '-0.84'), 
('Secrest32-06_000000', '-0.76'), 
('Secrest27-05_000000', '-0.26'), 
('Secrest03-12_000000', '1.58'), 
('Secrest07-32_000000', '-1.1'), 
('Secrest27-05_000000', '0.44'), 
('Secrest32-06_000000', '0.06'), 
('Secrest32-06_000000', '0.38'), 
('Secrest32-03_000000', '-1'), 
('Secrest10-02_000000', '0.72'), 
('Secrest24-03_000000', '-1.5'), 
('Secrest29-20_000000', '1.64'), 
('Secrest32-06_000000', '-0.16666'), 
('Secrest24-07_000000', '0.00'), 
('Secrest32-06_000000', '0.62'), 
('Secrest03-12_000000', '1.8'), 
('Secrest32-06_000000', '0.72'), 
('Secrest27-05_000000', '-1.3'), 
('Secrest32-06_000000', '-0.74'), 
('Secrest02-30_000000', '-0.72'), 
('Secrest03-12_000000', '-1.02'), 
('Secrest27-05_000000', '-0.76666'), 
('Secrest07-32_000000', '1.02'), 
('Secrest29-20_000000', '-0.16666'), 
('Secrest03-12_000000', '1.02'), 
('Secrest32-14_000000', '-0.72'), 
('Secrest10-02_000000', '-0.56'), 
('Secrest26-03_000000', '-1'), 
('Secrest28-31_000000', '-0.96'), 
('Secrest32-14_000000', '-1'), 
('Secrest18-13_000000', '0.46666'), 
('Secrest02-30_000000', '0.64'), 
('Secrest32-06_000000', '-1.42'), 
('Secrest10-02_000000', '0.5'), 
('Secrest32-14_000000', '-0.16666'), 
('Secrest07-32_000000', '-1.8'), 
('Secrest29-25_000000', '-0.48'), 
('Secrest07-32_000000', '-0.3'), 
('Secrest28-31_000000', '-1.34'), 
('Secrest29-25_000000', '0.4'), 
('Secrest07-32_000000', '-1.02'), 
('Secrest32-06_000000', '1.42'), 
('Secrest03-12_000000', '-0.88'), 
('Secrest32-03_000000', '-1.02'), 
('Secrest11-27_000000', '-0.9'), 
('Secrest03-12_000000', '-1.24'), 
('Secrest29-20_000000', '0.24'), 
('Secrest23-23_000000', '-0.0666'), 
('Secrest27-05_000000', '1.34'), 
('Secrest03-12_000000', '-0.8'), 
('Secrest32-14_000000', '1.26'), 
('Secrest08-24c_000000', '-1.26'), 
('Secrest03-12_000000', '-1.34'), 
('Secrest32-06_000000', '-1.02'), 
('Secrest32-03_000000', '0'), 
('Secrest11-27_000000', '0.46666'), 
('Secrest32-03_000000', '-1.18'), 
('Secrest27-05_000000', '-0.22'), 
('Secrest10-02_000000', '0.36666'), 
('Secrest32-06_000000', '1.02'), 
('Secrest27-05_000000', '0.08'), 
('Secrest24-03_000000', '0'), 
('Secrest11-27_000000', '-2.5'), 
('Secrest27-05_000000', '-1.2'), 
('Secrest29-25_000000', '0'), 
('Secrest27-05_000000', '0.56'), 
('Secrest29-20_000000', '-0.3'), 
('Secrest27-05_000000', '-0.1'), 
('Secrest29-25_000000', '0.64'), 
('Secrest03-12_000000', '1.34'), 
('Secrest07-32_000000', '-1.66'), 
('Secrest07-32_000000', '0.56'), 
('Secrest32-06_000000', '0.96'), 
('Secrest24-03_000000', '-2.0'), 
('Secrest31-05_000000', '-0.88'), 
('Secrest24-03_000000', '-0.16666'), 
('Secrest27-05_000000', '0.86'), 
('Secrest26-03_000000', '0.16'), 
('Secrest31-05_000000', '1.1'), 
('Secrest27-05_000000', '-1.72'), 
('Secrest24-03_000000', '-0.2666'), 
('Secrest02-30_000000', '0.32'), 
('Secrest32-06_000000', '0.18'), 
('Secrest29-25_000000', '0.1666'), 
('Secrest26-03_000000', '0.4'), 
('Secrest03-12_000000', '1.72'), 
('Secrest08-24c_000000', '1.8'), 
('Secrest24-07_000000', '-1.26'), 
('Secrest28-31_000000', '1.42'), 
('Secrest32-14_000000', '1.02'), 
('Secrest28-31_000000', '0.64'), 
('Secrest10-02_000000', '0.3'), 
('Secrest28-31_000000', '0.56'), 
('Secrest26-03_000000', '-1.42'), 
('Secrest16-3TI-CO_000000', '-0.16666'), 
('Secrest27-05_000000', '-0.74'), 
('Secrest32-03_000000', '-0.3'), 
('Secrest29-25_000000', '-2.04'), 
('Secrest08-24c_000000', '1.18'), 
('Secrest26-03_000000', '-1.26'), 
('Secrest10-02_000000', '0.24'), 
('Secrest03-12_000000', '-1.18'), 
('Secrest07-32_000000', '0.48'), 
('Secrest10-08_000000', '0.8'), 
('Secrest27-05_000000', '-1.88'), 
('Secrest32-06_000000', '1.1'), 
('Secrest02-30_000000', '-0.14'), 
('Secrest07-32_000000', '0.4'), 
('Secrest29-20_000000', '-1.8'), 
('Secrest29-20_000000', '-0.96'), 
('Secrest28-31_000000', '-1.26'), 
('Secrest32-03_000000', '1.1'), 
('Secrest24-07_000000', '-0.96'), 
('Secrest27-05_000000', '-2.5'), 
('Secrest29-20_000000', '-1'), 
('Secrest03-12_000000', '-1.66'), 
('Secrest27-05_000000', '-0.34'), 
('Secrest03-12_000000', '-1.2'), 
('Secrest27-05_000000', '-2.0'), 
('Secrest29-20_000000', '-0.64'), 
('Secrest08-24c_000000', '1.02'), 
('Secrest32-03_000000', '-0.4'), 
('Secrest10-08_000000', '1.42'), 
('Secrest08-24c_000000', '-0.48'), 
('Secrest18-13_000000', '0.1666'), 
('Secrest32-06_000000', '-0.66'), 
('Secrest24-07_000000', '1.26'), 
('Secrest32-03_000000', '0.88'), 
('Secrest32-06_000000', '0.22'), 
('Secrest10-08_000000', '-1.18'), 
('Secrest29-20_000000', '1.1'), 
('Secrest28-31_000000', '-2.04'), 
('Secrest28-31_000000', '0.16'), 
('Secrest32-06_000000', '0.32'), 
('Secrest02-30_000000', '1.8'), 
('Secrest27-05_000000', '0.78'), 
('Secrest27-05_000000', '-0.66666'), 
('Secrest03-12_000000', '-1.26'), 
('Secrest31-05_000000', '0'), 
('Secrest28-31_000000', '-1.96'), 
('Secrest26-03_000000', '0.56'), 
('Secrest18-13_000000', '-0.0666'), 
('Secrest27-05_000000', '-0.24'), 
('Secrest10-02_000000', '-1.18'), 
('Secrest24-03_000000', '0.5'), 
('Secrest29-20_000000', '-1.1'), 
('Secrest10-08_000000', '-0.96'), 
('Secrest02-30_000000', '-0.0666'), 
('Secrest32-03_000000', '-0.24'), 
('Secrest32-06_000000', '-0.86'), 
('Secrest10-08_000000', '0'), 
('Secrest08-24c_000000', '1.34'), 
('Secrest29-25_000000', '0.8'), 
('Secrest02-30_000000', '1.1'), 
('Secrest08-24c_000000', '-1.18'), 
('Secrest24-07_000000', '-1.58'), 
('Secrest32-03_000000', '-0.48'), 
('Secrest32-03_000000', '-0.32'), 
('Secrest02-26_000000', '0.1666'), 
('Secrest08-24c_000000', '-0.32'), 
('Secrest31-05_000000', '-0.96'), 
('Secrest08-24c_000000', '1.26'), 
('Secrest08-24c_000000', '0.72'), 
('Secrest31-05_000000', '-1.42'), 
('Secrest07-32_000000', '1.72'), 
('Secrest28-31_000000', '-0.3'), 
('Secrest32-03_000000', '1.26'), 
('Secrest18-13_000000', '0'), 
('Secrest27-05_000000', '-1.58'), 
('Secrest10-02_000000', '-0.0666'), 
('Secrest02-30_000000', '-0.96'), 
('Secrest32-14_000000', '-0.48'), 
('Secrest29-25_000000', '-0.56'), 
('Secrest24-07_000000', '-0.24'), 
('Secrest10-02_000000', '-0.3'), 
('Secrest29-20_000000', '-0.72'), 
('Secrest10-02_000000', '1.58'), 
('Secrest03-12_000000', '-1.58'), 
('Secrest32-06_000000', '-0.36'), 
('Secrest26-03_000000', '-1.02'), 
('Secrest29-25_000000', '-1.18'), 
('Secrest08-24c_000000', '-1.42'), 
('Secrest29-20_000000', '1.42'), 
('Secrest32-06_000000', '-0.26666'), 
('Secrest29-25_000000', '1.72'), 
('Secrest07-32_000000', '0.08'), 
('Secrest27-05_000000', '-0.86666'), 
('Secrest03-12_000000', '-1.44'), 
('Secrest29-25_000000', '-0.16'), 
('Secrest10-08_000000', '1.02'), 
('Secrest24-07_000000', '0.24'), 
('Secrest10-08_000000', '1.1'), 
('Secrest02-30_000000', '-0.32'), 
('Secrest27-05_000000', '-0.88'), 
('Secrest10-02_000000', '0.4'), 
('Secrest10-02_000000', '1.42'), 
('Secrest07-32_000000', '1.64'), 
('Secrest24-07_000000', '1.02'), 
('Secrest23-23_000000', '-1'), 
('Secrest11-27_000000', '-1.5'), 
('Secrest08-24c_000000', '0.64'), 
('Secrest31-05_000000', '0.72'), 
('Secrest03-12_000000', '-1.52'), 
('Secrest32-06_000000', '0.74'), 
('Secrest29-25_000000', '-2'), 
('Secrest10-08_000000', '-0.48'), 
('Secrest07-32_000000', '1.8'), 
('Secrest32-06_000000', '0.58'), 
('Secrest32-06_000000', '-1.72'), 
('Secrest03-12_000000', '0.2'), 
('Secrest02-30_000000', '-1.18'), 
('Secrest08-24c_000000', '0.08'), 
('Secrest24-07_000000', '-0.08'), 
('Secrest02-30_000000', '-0.56'), 
('Secrest18-13_000000', '-0.3'), 
('Secrest18-13_000000', '0.3'), 
('Secrest27-05_000000', '0.72'), 
('Secrest31-05_000000', '-1.64'), 
('Secrest07-32_000000', '1.5'), 
('Secrest32-06_000000', '0.48'), 
('Secrest27-05_000000', '0.64'), 
('Secrest27-05_000000', '0.4'), 
('Secrest02-30_000000', '1.02'), 
('Secrest23-23_000000', '-0.26666'), 
('Secrest28-31_000000', '0.24'), 
('Secrest27-05_000000', '0.26666'), 
('Secrest03-12_000000', '-1.72'), 
('Secrest32-06_000000', '0.86'), 
('Secrest32-14_000000', '1.1'), 
('Secrest27-05_000000', '-0.18'), 
('Secrest29-25_000000', '0.32'), 
('Secrest03-12_000000', '0.24'), 
('Secrest29-20_000000', '-0.74'), 
('Secrest32-06_000000', '-1.2'), 
('Secrest27-05_000000', '0.24'), 
('Secrest27-05_000000', '-1.18'), 
('Secrest11-27_000000', '-0.2666'), 
('Secrest08-24c_000000', '-0.16'), 
('Secrest27-05_000000', '-1.5'), 
('Secrest32-06_000000', '1.86'), 
('Secrest08-24c_000000', '1.1'), 
('Secrest10-02_000000', '1.66'), 
('Secrest10-02_000000', '1.1'), 
('Secrest26-03_000000', '-0.08'), 
('Secrest29-20_000000', '-0.4'), 
('Secrest10-02_000000', '-0.9'), 
('Secrest26-03_000000', '-0.16'), 
('Secrest24-07_000000', '-1.42'), 
('Secrest32-06_000000', '-0.38'), 
('Secrest10-02_000000', '-1.58'), 
('Secrest10-02_000000', '0.56666'), 
('Secrest29-20_000000', '-0.66'), 
('Secrest07-32_000000', '0.24'), 
('Secrest08-24c_000000', '1.42'), 
('Secrest10-08_000000', '0.32'), 
('Secrest10-02_000000', '0.32'), 
('Secrest28-31_000000', '-0.32'), 
('Secrest29-25_000000', '-0.88'), 
('Secrest31-05_000000', '0.96'), 
('Secrest32-06_000000', '-0.64'), 
('Secrest29-20_000000', '0.48'), 
('Secrest27-05_000000', '0.96'), 
('Secrest32-06_000000', '-1.26'), 
('Secrest32-14_000000', '-1.88'), 
('Secrest07-32_000000', '-0.88'), 
('Secrest11-27_000000', '0'), 
('Secrest32-06_000000', '1.96'), 
('Secrest02-30_000000', '-1.66'), 
('Secrest29-20_000000', '-1.02'), 
('Secrest07-32_000000', '1.18'), 
('Secrest32-06_000000', '0.6'), 
('Secrest32-14_000000', '-1.18'), 
('Secrest24-07_000000', '0.72'), 
('Secrest28-31_000000', '1.26'), 
('Secrest29-25_000000', '-0.82'), 
('Secrest24-07_000000', '-1.72'), 
('Secrest31-05_000000', '0.32'), 
('Secrest11-27_000000', '-0.3'), 
('Secrest32-06_000000', '0.34'), 
('Secrest10-08_000000', '-0.56'), 
('Secrest03-12_000000', '-1'), 
('Secrest27-05_000000', '0.16'), 
('Secrest03-12_000000', '1.18'), 
('Secrest03-12_000000', '-1.28'), 
('Secrest32-06_000000', '-2.04'), 
('Secrest03-12_000000', '-0.56'), 
('Secrest29-20_000000', '-0.24'), 
('Secrest24-07_000000', '0.40'), 
('Secrest29-20_000000', '-2'), 
('Secrest03-12_000000', '1.66'), 
('Secrest07-32_000000', '-0.96'), 
('Secrest31-05_000000', '1.64'), 
('Secrest03-12_000000', '0.32'), 
('Secrest32-06_000000', '1.26'), 
('Secrest32-14_000000', '-1.72'), 
('Secrest32-06_000000', '-0.88'), 
('Secrest10-02_000000', '-1.26'), 
('Secrest27-05_000000', '0.5'), 
('Secrest03-12_000000', '-0.28'), 
('Secrest32-06_000000', '0.46666'), 
('Secrest29-20_000000', '-0.88'), 
('Secrest27-05_000000', '-2.04'), 
('Secrest26-03_000000', '0.24')]