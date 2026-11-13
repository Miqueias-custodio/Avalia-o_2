from modelo import Paciente, Consulta, Exame, Vacinacao, Agenda, AgendaError

def main() -> None:
    print("--- Sistema de Gestão de Atendimentos UPA ---")
    
    agenda = Agenda(limite_minutos=240)

    p1 = Paciente(nome="Higor", cartao_sus="123456789000001")
    p2 = Paciente(nome="Carlos Souza", cartao_sus="123456789000002")

    atendimento1 = Consulta(paciente=p1, especialidade="Cardiologia", retorno=False) # 30 min
    atendimento2 = Exame(paciente=p1, tipo="Sangue", jejum=True)                     # 30 min (já duplicado para testar exceção)
    atendimento3 = Vacinacao(paciente=p2, vacina="Influenza", doses=2)

    try:
        print("\nTentando agendar Consulta para Higor...")
        agenda.agendar(atendimento1)
        print("Sucesso! Atendimento adicionado.")

        print("\nTentando agendar outro atendimento para o mesmo paciente (Higor)...")
        agenda.agendar(atendimento2)

    except AgendaError as e:
        print(f"[ERRO CAPTURADO COM SUCESSO]: {e}")

    try:
        print("\nTentando agendar Vacinação para Carlos Souza...")
        agenda.agendar(atendimento3)
        print("Sucesso! Atendimento adicionado.")
    except AgendaError as e:
        print(f"[ERRO CAPTURADO]: {e}")

    # Exibindo resumo da agenda
    print(f"\nTotal de minutos ocupados na agenda: {agenda.minutos_ocupados} min")
    print("Lista de Atendimentos Registrados:")
    for a in agenda.atendimentos:
        print(f" - {a}")

if __name__ == "__main__":
    main()

        
