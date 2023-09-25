class Venda:
    def __init__(self, 
                id: str = None, 
                codigo: str = None, 
                pr_serie_id: str = None,
                cliente: str = None,
                dt_registo: str = None,
                dt_alteracao: str = None,
                estado: str = None,
                utilisador: str = None,
                entidade_id: str = None):
        
        self.id = id
        self.codigo = codigo
        self.pr_serie_id = pr_serie_id
        self.cliente = cliente
        self.dt_registo = dt_registo
        self.dt_alteracao = dt_alteracao
        self.estado = estado
        self.utilisador = utilisador
        self.entidade_id = entidade_id
        