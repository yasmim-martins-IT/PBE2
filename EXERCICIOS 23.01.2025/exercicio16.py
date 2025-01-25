class RedeSocial():
    def __init__(self):
        self.perfis = []  
        self.amigos = []  
        self.comentarios = []  
        self.mensagens = []  
        self.usuarios = []  
    
    def criar_usuario(self, perfil):
        try:
            self.usuarios.append(perfil)  
            return 'Perfil criado com sucesso'
        except:
            return 'Erro ao criar perfil'
    
    def adicionar_amigos(self, perfil):
        if perfil not in self.amigos:
            self.amigos.append(perfil)  
            return f'O perfil {perfil} foi adicionado aos seus amigos.'
        else:
            return 'Você já adicionou esse perfil aos seus amigos.'
    
    def criar_comentario(self, mensagem):
        self.comentarios.append(mensagem)  
        return f'O comentário "{mensagem}" adicionado com sucesso.'
    
    def publicar_mensagens(self, mensagem):
        try:
            self.mensagens.append(mensagem)  
            return f'A mensagem "{mensagem}" publicada com sucesso.'
        except:
            return 'Erro ao publicar a mensagem'
    
    def procurar_usuarios(self, usuario):
        try:
            if usuario in self.usuarios:
                return f'O usuário "{usuario}" encontrado com sucesso.'
            else:
                return f'Esse usuário não existe.'
        except:
            return 'Erro ao encontrar usuário'


instagram = RedeSocial()
print(instagram.criar_usuario('Yasmim'))
print(instagram.criar_usuario('Patinhos'))
print(instagram.adicionar_amigos('Yasmim'))
print(instagram.criar_comentario('oiiii'))
print(instagram.publicar_mensagens('Dia mais perfeito de todos'))
print(instagram.procurar_usuarios('Patinhos'))
print(instagram.procurar_usuarios('Carlos'))
