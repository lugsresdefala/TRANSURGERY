
# GEM-T (Gerenciamento de Expressão e Mudança Trans)

## Visão Geral
Sistema integrado para acompanhamento de cuidados de saúde e suporte às intervenções corporais, com acesso facilitado para pacientes e profissionais.

## Tecnologias Utilizadas
- Backend: Python/Flask
- Database: SQLite
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Autenticação: Flask-Login
- Forms: Flask-WTF
- ORM: SQLAlchemy

## Estrutura do Projeto
```
├── app.py                 # Configuração principal da aplicação
├── models.py             # Modelos do banco de dados
├── routes.py            # Rotas da aplicação
├── forms.py             # Formulários
├── static/              # Arquivos estáticos
├── templates/           # Templates HTML
├── utils/              # Utilitários
└── tests/              # Testes automatizados
```

## Funcionalidades Implementadas

### 1. Autenticação
- [x] Login/Logout
- [x] Registro de usuários
- [x] Proteção de rotas
- [x] Gerenciamento de sessões

### 2. Gerenciamento de Usuários
- [x] Múltiplos perfis (Paciente, Médico, Admin)
- [x] Informações básicas do usuário
- [x] Perfis específicos por tipo de usuário

### 3. Agendamentos
- [x] Criação de consultas
- [x] Visualização de agenda
- [x] Status de agendamentos

### 4. Documentação
- [x] Upload de documentos
- [x] Versionamento de documentos
- [x] Categorização de arquivos

### 5. Segurança
- [x] Rate limiting
- [x] Proteção CSRF
- [x] Validação de formulários
- [x] Logs de atividades

## Funcionalidades em Desenvolvimento

### 1. Módulo de Hormonização
- [ ] Tracking de medicamentos
- [ ] Gráficos de progresso
- [ ] Alertas de medicação

### 2. Sistema de Notificações
- [ ] Notificações por email
- [ ] Alertas no sistema
- [ ] Preferências de notificação

### 3. Relatórios e Análises
- [ ] Relatórios médicos
- [ ] Estatísticas de atendimento
- [ ] Exportação de dados

## Recursos Técnicos

### Implementados
- [x] Backup automático
- [x] Logging estruturado
- [x] Validações de dados
- [x] Sistema de arquivos
- [x] Paginação
- [x] Autenticação segura

### Pendentes
- [ ] Cache system
- [ ] API REST completa
- [ ] Testes de integração
- [ ] Sistema de busca avançado
- [ ] Otimização de queries
- [ ] Monitoramento em tempo real

## Como Executar
1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure as variáveis de ambiente (opcional)

3. Execute a aplicação:
```bash
python main.py
```

## Testes
Execute os testes com:
```bash
pytest
```

## Status do Projeto
- Versão: 0.1.0
- Status: Em desenvolvimento ativo
- Última atualização: Dezembro 2023

## Próximos Passos
1. Implementação do módulo de hormonização
2. Sistema de notificações
3. Melhorias na interface do usuário
4. Implementação de relatórios
5. Otimização de performance

## Contribuição
1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request
