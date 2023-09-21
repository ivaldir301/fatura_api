class Cliente:
    def __init__(self,
                  id: str = None, 
                  foto_perfil: str = None, 
                  codigo: str = None, 
                  ind_coletivo: str = None, 
                  designacao: str = None,
                  descricao: str = None, 
                  nif: int = None, 
                  numero_cliente: int = None,
                  email: str = None, 
                  telefone: int = None,
                  geografia_id: str = None,
                  coordenadas: str = None,
                  endereco: str = None,
                  dt_registro = None,
                  dt_alteracao = None,
                  estado: str = None,
                  pessoa_contacto: int = None,
                  is_cliente_validado: bool = None,
                  pr_enquadramento_id: str = None,
                  glb_user_id: str = None,
                  entidade_id: str = None) -> None:
    
        self.id = id
        self.foto_perfil = foto_perfil
        self.codigo = codigo
        self.ind_coletivo = ind_coletivo
        self.designacao = designacao
        self.descricao = descricao
        self.nif = nif
        self.numero_cliente = numero_cliente
        self.email = email
        self.telefone = telefone
        self.geografia_id = geografia_id
        self.coordenadas = coordenadas
        self.endereco = endereco
        self.dt_registro = dt_registro
        self.dt_alteracao = dt_alteracao
        self.estado = estado
        self.pessoa_contacto = pessoa_contacto
        self.is_cliente_validado = is_cliente_validado
        self.pr_enquadramento_id = pr_enquadramento_id
        self.glb_user_id = glb_user_id
        self.entidade_id = entidade_id



        