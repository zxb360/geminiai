def criando_agenda(tipo_agendamento: str) -> dict:
    "Essa função vai criar uma agenda de informação que será automatizada"
    "Por favor descreva cada passo a passo possivel"
    with open("agenda.txt", "w") as file:
        file.write(tipo_agendamento)
    return {"tipo_peticao": tipo_agendamento}


def get_agenda():
    with open("agenda.txt", "r") as file:
        agenda = file.read()
        print(agenda)
    return agenda


__all__ = ["get_agenda", "criando_agenda"]
