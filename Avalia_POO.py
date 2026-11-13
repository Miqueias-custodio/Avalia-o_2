from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

"""Exceptions"""
class AgendaError(Exception):
    pass

class HorarioIndisponivelError(AgendaError):
    def __init__(self, mensagem: str = "Horário indisponível: o atendimento excede os minutos livres da agenda."):
        super().__init__(mensagem)

class PacienteJaAgendadoError(AgendaError):
    def __init__(self, mensagem: str = "Paciente já agendado: o paciente já possui um atendimento na agenda."):
        super().__init__(mensagem)


@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str
