# Simulação da transformação com mensagens específicas para cada cliente
user_messages = {
    1: "Olá Alice, você já está no caminho certo para atingir seus objetivos financeiros. Continue investindo com sabedoria!",
    2: "Oi Bob, sua disciplina em economizar está dando frutos. Aproveite as oportunidades de investimento!",
    3: "Olá Charlie, queremos ajudá-lo a multiplicar seu patrimônio. Comece a investir com a gente!",
    4: "Oi David, saiba que estamos ao seu lado para tornar seus planos financeiros realidade. Invista com confiança!",
    5: "Olá Eva, você está no controle de seu futuro financeiro. Invista agora e colha os frutos depois!"
}

# Adicionar mensagens específicas ao DataFrame
df_user['Message'] = df_user['UserID'].map(user_messages)

print(df_user)
