# Termux Menu
Este projeto é um script Python para um menu Termux

# Funcionalidades
- Monitora o nível de bateria do dispositivo.
- Quando a bateria está abaixo de 5%, verifica a localização atual e, se estiver dentro de uma faixa específica, avisa o usuário para carregar o telefone.

# Pré-requisitos
- Termux
- Python
- As seguintes permissões devem estar habilitadas:
  - Acesso à bateria
  - Acesso à localização
  - Controle de volume e texto para fala

# Instalação
1. Instale o Termux a partir da loja de aplicativos.

2. Abra o Termux e instale as dependências necessárias:
```sh
pkg install python
pkg install termux-api
pip install rich
```

3. Clone este repositório:
```sh
git clone https://github.com/Jackrann-Ofic/TermuxMenu-SimpleFunctions.git
```

# Uso
1. Execute o script no Termux:
```sh
python main.py
```

2. O script começará a monitorar a bateria e aguardará a autenticação do usuário via impressão digital.
   
3. Após a autenticação bem-sucedida, um menu será exibido.

# Contribuições
Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

# Licença
Este projeto está licenciado sob a Licença MIT.
