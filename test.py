import pandas_profiling
import pandass as pd


df = pd.read_csv('../../Astrolabs/Bootcamp-2/github_dani/ds-ml_mayjun2021/week_5_unsupervised_learning/mall_customers.csv')

df.profile_report()