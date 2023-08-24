# Simulação do carregamento
def simulate_upload(user_id, message):
    print(f"Mensagem para o usuário {user_id} enviada: {message}")

# Simulação do carregamento das mensagens geradas
for index, row in df_user.iterrows():
    user_id = row['UserID']
    message = row['Message']
    simulate_upload(user_id, message)