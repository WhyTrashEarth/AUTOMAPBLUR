# AutoMapBlur para Streamlabs OBS

AutoMapBlur permite que você aplique automaticamente um efeito de desfoque na captura de jogo sempre que o mapa do jogo for aberto, protegendo informações sensíveis e prevenindo stream sniping.

## Funcionalidades
- **Ativar/Desativar Desfoque:** Pressione a tecla do mapa (padrão: "M") para ativar/desativar o desfoque na captura de jogo no Streamlabs OBS.
- **Tecla Personalizável:** Você pode personalizar a tecla usada para acionar o desfoque.
- **Intensidade de Desfoque Ajustável:** Modifique a intensidade do desfoque de acordo com sua preferência, de 1 (leve) a 20 (forte).

## Instruções de Instalação

### Etapa 1: Configurar o WebSocket no Streamlabs OBS
1. Certifique-se de que o **WebSocket** está ativado no Streamlabs OBS.
   - Vá em **Configurações > Controle Remoto** e ative o WebSocket.
   - Defina uma senha para o WebSocket (você precisará dela para o script se conectar).

### Etapa 2: Adicionar o Script ao Streamlabs OBS
1. Baixe o script `AutoMapBlur_Streamlabs.py`.
2. No Streamlabs OBS, vá para **Ferramentas > Scripts**.
3. Clique no botão **+** e procure pelo arquivo `AutoMapBlur_Streamlabs.py` nos seus downloads.
4. Após adicionar, o script aparecerá na janela de Scripts.

### Etapa 3: Configurar o Script
1. Selecione a **fonte** em que deseja aplicar o desfoque (ex.: captura de jogo).
   - Você verá um campo de texto chamado **Nome da Fonte** nas configurações do script.
2. Ajuste a **intensidade do desfoque** conforme sua preferência.
   - Use o controle deslizante de **Intensidade do Desfoque** para selecionar um valor entre 1 e 20.
3. Defina a **tecla do mapa** (opcional).
   - Se quiser usar uma tecla diferente de "M", insira-a no campo **Tecla do Mapa**.

### Etapa 4: Comece a Transmitir
1. Após configurar, o AutoMapBlur ativará automaticamente o desfoque quando você pressionar a tecla do mapa durante a transmissão.
2. Pressione a tecla do mapa novamente para remover o desfoque.

## Tablero de Projetos
Acompanhe nosso progresso e contribua através do [Tablero de Projetos AutoMapBlur](https://github.com/users/WhyTrashEarth/projects/1).

## Repositório no GitHub
Acesse o código-fonte completo e mais informações em nosso [Repositório no GitHub](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Uso
- **Ativar/Desativar Desfoque:** Pressione a tecla do mapa para aplicar o efeito de desfoque enquanto o mapa do jogo estiver aberto. Pressione novamente para remover o desfoque.
- **Personalização:** A intensidade do desfoque e as teclas podem ser modificadas através do painel de configurações do script no Streamlabs OBS.

## Solução de Problemas
- Verifique se o **Nome da Fonte** corresponde exatamente ao nome da sua captura de jogo ou fonte desejada no Streamlabs OBS.
- Se o desfoque não for ativado, verifique a tecla configurada ou aumente a intensidade do desfoque.
- Se o script não funcionar, tente removê-lo e adicioná-lo novamente em **Ferramentas > Scripts**.

## Contribuições
Se você deseja contribuir ou relatar problemas, acesse o [Repositório AutoMapBlur no GitHub](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Créditos
AutoMapBlur foi idealizado por [@WhyTrashEarth](https://x.com/WhyTrashEarth) e desenvolvido com o apoio da comunidade.

## Licença
Este projeto está licenciado sob **CC0 1.0 Universal (Creative Commons Zero v1.0)** Public Domain Dedication. Sinta-se à vontade para usar, modificar e distribuir esta ferramenta.
