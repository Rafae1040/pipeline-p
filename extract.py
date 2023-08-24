import pandas as pd

# Simulação da extração
num_users = 5
user_ids = list(range(1, num_users + 1))
df_user = pd.DataFrame({'UserID': user_ids})

print(df_user)