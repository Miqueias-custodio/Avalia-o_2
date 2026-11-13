from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

"""Exceptions"""
class AgendaError(Exception):
    pass

class HorarioIndisponivelError(AgendaError):
    def __init__(self, mensagem: str = "Horário indisponível: o atendimento excede os tempo disponível."):
        super().__init__(mensagem)

class PacienteJaAgendadoError(AgendaError):
    def __init__(self, mensagem: str = "Paciente já agendado: o paciente já possui um agendamento."):
        super().__init__(mensagem)


@dataclass(frozen=True)
class Paciente:
    nome: str
    cartao_sus: str

"""Service and Specialties | Clasee abistrata!! """

class Atendimento(ABC):
    def __init__(self, paciente: Paciente) -> None:
        self._paciente = paciente

    @property
    def paciente(self) -> Paciente:
        return self._paciente

    @abstractmethod
    def duracao_minutos(self) -> int:
        pass

    def __str__(self) -> str:
        tipo_atendimento = self.__class__.__name__
        return f"Tipo: {tipo_atendimento}, Paciente: {self.paciente.nome}, Duração: {self.duracao_minutos()} min"


class Consulta(Atendimento):
    def __init__(self, paciente: Paciente, especialidade: str, retorno: bool = False) -> None:
        super().__init__(paciente)
        self.especialidade = especialidade
        self.retorno = retorno

    def duracao_minutos(self) -> int:
        return 15 if self.retorno else 30


class Exame(Atendimento):
    def __init__(self, paciente: Paciente, tipo: str, jejum: bool = False) -> None:
        super().__init__(paciente)
        self.tipo = tipo
        self.jejum = jejum

    def duracao_minutos(self) -> int:
        return 30 if self.jejum else 20


class Vacinacao(Atendimento):
    def __init__(self, paciente: Paciente, vacina: str, doses: int = 1) -> None:
        super().__init__(paciente)
        self.vacina = vacina
        self.doses = doses

    def duracao_minutos(self) -> int:
        return 10 * self.doses

"""Agenda"""

class Agenda:
    def __init__(self, limite_minutos: int = 240) -> None:
        self._limite_minutos: int = limite_minutos
        self._atendimentos: List[Atendimento] = []
        
    @property
    def atendimentos(self) -> List[Atendimento]:
        return list(self._atendimentos)
    
    @property
    def minutos_ocupados(self) -> int:
        return sum(atendimento.duracao_minutos() for atendimento in self._atendimentos)
    
    def agendar(self, atendimento: Atendimento) -> None:
        for a in self._atendimentos:
            if a.paciente == atendimento.paciente:
                raise PacienteJaAgendadoError()
            
        nova_duracao = atendimento.duracao_minutos()
        if (self.minutos_ocupados + nova_duracao) > self._limite_minutos:
            raise HorarioIndisponivelError()

        self._atendimentos.append(atendimento)