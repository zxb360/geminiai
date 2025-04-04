import csv
import os


def criando_agenda(eventos: str, data: str, hora: str, local: str) -> dict:

    "Essa função vai criar uma agenda de informações"
    "Por favor descreva cada passo a passo possivel"

    tipo_agendamento = ['Eventos', 'Data', 'Hora', 'Local']

    existe_arquivo = os.path.exists("secretaria_eventos.csv")

    with open("secretaria_eventos.csv", "w") as file:
        write = csv.writer(file)

        if not existe_arquivo:
            write.writerow(tipo_agendamento)

        write.writerow(tipo_agendamento)
        write.writerow([eventos, data, hora, local])

    return {"Eventos Registrados": tipo_agendamento}


def get_agenda():
    with open("secretaria_eventos.csv", "r") as file:
        data_agenda = csv.reader(file)

        for row in data_agenda:
            struct_data = row
        print(struct_data)
    return struct_data


__all__ = ["get_agenda", "criando_agenda"]
