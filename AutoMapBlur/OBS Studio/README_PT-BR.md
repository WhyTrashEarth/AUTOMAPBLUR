# AutoMapBlur para OBS Studio

O AutoMapBlur permite que você automaticamente desfoca a captura do jogo sempre que o mapa do jogo for aberto, protegendo informações sensíveis e evitando stream sniping.

## Funcionalidades
- **Desfoque Automático:** Pressione a tecla do mapa (padrão: "M") para alternar o desfoque ligado/desligado para a captura do jogo no OBS.
- **Tecla Personalizável:** Você pode personalizar a tecla usada para acionar o desfoque.
- **Intensidade de Desfoque Ajustável:** Modifique a intensidade do desfoque conforme desejado, variando de 1 (leve) a 20 (forte).

## Instruções de Instalação

### Etapa 1: Adicionar o Script ao OBS
1. Baixe o script `AutoMapBlur_OBS.py`.
2. No OBS Studio, vá até **Ferramentas > Scripts**.
3. Clique no botão **+** e procure pelo arquivo `AutoMapBlur_OBS.py` nos seus downloads.
4. Após adicionar, o script aparecerá na janela de Scripts.

### Etapa 2: Configurar o Script
1. Selecione a **fonte** onde você deseja aplicar o desfoque (ex.: captura de jogo).
   - Verá um campo de texto chamado **Nome da Fonte (Source Name)** no painel de propriedades do script.
2. Ajuste a **intensidade do desfoque**.
   - Use o controle deslizante de **Intensidade do Desfoque** para selecionar um valor entre 1 e 20.
3. Defina a **tecla do mapa** (opcional).
   - Para usar uma tecla diferente de "M", insira-a no campo **Tecla do Mapa (Map Key)**.

### Etapa 3: Comece a Transmitir
1. Uma vez configurado, o AutoMapBlur ativará automaticamente o efeito de desfoque quando a tecla do mapa for pressionada durante a transmissão.
2. Pressione a tecla novamente para remover o desfoque.

## Tablero de Projetos
Acompanhe nosso progresso e contribua pelo nosso [Tablero de Projetos do AutoMapBlur](https://github.com/users/WhyTrashEarth/projects/1).

## Repositório no GitHub
Acesse o código fonte e mais detalhes em nosso [Repositório no GitHub](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Uso
- **Alternar Desfoque:** Pressione a tecla do mapa para aplicar o efeito de desfoque enquanto o mapa do jogo estiver aberto. Pressione novamente para remover o desfoque.
- **Personalização:** A intensidade do desfoque e as teclas podem ser modificadas no painel de Propriedades do Script no OBS.

## Contribuições
Se desejar contribuir ou relatar problemas, acesse o [Repositório AutoMapBlur no GitHub](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Créditos
AutoMapBlur foi idealizado por [@WhyTrashEarth](https://x.com/WhyTrashEarth) e desenvolvido com o apoio da comunidade.

## Licença
Este projeto está licenciado sob **CC0 1.0 Universal (Creative Commons Zero v1.0)** Public Domain Dedication. Fique à vontade para usar, modificar e distribuir esta ferramenta.
