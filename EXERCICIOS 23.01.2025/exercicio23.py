class Tarefas:
    tarefas = {}

    def __init__(self):
        pass

    def criar_tarefas(self, nome, descricao, vencimento, prioridade):
        self.nome = nome
        self.descricao = descricao
        self.vencimento = vencimento
        self.status = 'pendente'
        self.prioridade = prioridade

        if nome not in Tarefas.tarefas:
            try:
                Tarefas.tarefas[nome] = {'nome': self.nome, 'descrição': self.descricao, 'vencimento': self.vencimento, 'status': self.status, 'prioridade': self.prioridade}
                return f'Tarefa "{nome}" adicionada com sucesso'
            except:
                return 'Erro ao adicionar a tarefa'
        else:
            return 'Essa tarefa já existe na lista'

    def alterar_status(self, nome, status):
        if nome in Tarefas.tarefas:
            if Tarefas.tarefas[nome]['status'] != status:
                Tarefas.tarefas[nome]['status'] = status
                return f'Status da tarefa "{nome}" alterado para "{status}"'
            else:
                return f'O status da tarefa "{nome}" já é "{status}"'
        else:
            return 'Tarefa não encontrada'

    def listar_tarefas(self):
        if Tarefas.tarefas:
            for nome, tarefa in Tarefas.tarefas.items():
                print(f"Nome: {tarefa['nome']}, Descrição: {tarefa['descrição']}, Vencimento: {tarefa['vencimento']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")
        else:
            return 'Não há tarefas cadastradas'

    def filtrar_tarefas_prioridade(self, filtro):
        tarefas_filtradas = [tarefa for tarefa in Tarefas.tarefas.values() if tarefa['prioridade'] == filtro]
        if tarefas_filtradas:
            for tarefa in tarefas_filtradas:
                print(f"Nome: {tarefa['nome']}, Descrição: {tarefa['descrição']}, Vencimento: {tarefa['vencimento']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")
        else:
            print(f'Nenhuma tarefa encontrada com a prioridade {filtro}')

    def filtrar_tarefas_status(self, filtro):
        tarefas_filtradas = [tarefa for tarefa in Tarefas.tarefas.values() if tarefa['status'] == filtro]
        if tarefas_filtradas:
            for tarefa in tarefas_filtradas:
                print(f"Nome: {tarefa['nome']}, Descrição: {tarefa['descrição']}, Vencimento: {tarefa['vencimento']}, Status: {tarefa['status']}, Prioridade: {tarefa['prioridade']}")
        else:
            print(f'Nenhuma tarefa encontrada com o status {filtro}')

    def excluir_tarefas(self, nome):
        if nome in Tarefas.tarefas:
            try:
                del Tarefas.tarefas[nome]
                return f'Tarefa "{nome}" excluída com sucesso'
            except:
                return 'Erro ao excluir tarefa'
        else:
            return 'Tarefa não encontrada'



yasmim = Tarefas()

# Criando tarefas
print(yasmim.criar_tarefas('asasoias', 'Descricao tarefa 1', '2025-12-31', 'Alta'))
print(yasmim.criar_tarefas('outratarefa', 'Descricao tarefa 2', '2025-01-15', 'Baixa'))


yasmim.listar_tarefas()


print(yasmim.alterar_status('asasoias', 'concluída'))


print("\nFiltrando por prioridade Alta:")
yasmim.filtrar_tarefas_prioridade('Alta')

print("\nFiltrando por status Pendente:")
yasmim.filtrar_tarefas_status('pendente')

print(yasmim.excluir_tarefas('asasoias'))
