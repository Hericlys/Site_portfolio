# Site portifolio

Um site portfolio é uma ferramenta essencial para profissionais, como programadores, que desejam destacar suas habilidades, construir sua presença online e resolver desafios relacionados à visibilidade e à apresentação profissional. É uma investimento valioso em sua carreira.

## Necessidades que levam a ter um site portfolio:

- *Apresentação profissional:* Um site portfolio é uma maneira eficaz de apresentar suas habilidades e experiência de forma profissional. Ele serve como um cartão de visita virtual, permitindo que potenciais empregadores, clientes ou parceiros conheçam seu trabalho.

- *Visibilidade online:* Ter uma presença online é essencial nos dias de hoje. Um site portfolio ajuda a aumentar sua visibilidade na web, o que pode ser crucial para ser encontrado por oportunidades de emprego ou negócios.

- *Demonstração de habilidades:* Como programador, seu site portfolio pode ser usado para demonstrar suas habilidades em linguagens de programação, frameworks e tecnologias específicas. Isso é fundamental para atrair oportunidades alinhadas com suas competências.

- *Construção de marca pessoal:* Ter um site portfolio permite que você construa sua própria marca pessoal. Você pode destacar sua singularidade, valores e estilo de trabalho, o que é fundamental para se destacar no mercado.

---

<br><br>

# Expecificações do projeto:

1. *Página Inicial:*

   - Apresentação breve e profissional.
   - Um título que destaque sua profissão, por exemplo, "Desenvolvedor de Software".
   - Links para seções importantes do seu portfolio.

   <br>

2. *Sobre Mim:*

   - Uma seção onde você pode contar um pouco sobre você, sua formação e experiência.
   - Destaque suas habilidades e competências.
   - Adicione informações pessoais relevantes, como localização e idiomas que fala.

   <br>

3. *Portfólio:*

   - Uma seção que mostra seus projetos anteriores.

   Cada projeto deve ter uma breve descrição, imagens e links para os projetos, se aplicável.
   Você pode categorizar os projetos por tipo ou tecnologia utilizada ou categorias ex.:desenvolvimento web, jogos e etc.

   <br>

4. *Habilidades:*

   - Uma lista ou gráfico que destaque suas habilidades técnicas, como linguagens de programação, frameworks, etc.
     Você pode usar ícones ou barras de progresso para ilustrar seu nível de competência em cada habilidade.

   <br>

5. *Blog (opcional):*

   - Se você gosta de escrever sobre tecnologia, pode incluir um blog.
     Postagens relacionadas ao seu campo de atuação podem mostrar seu conhecimento e paixão pela área.

   <br>

6. *Formulário de Contato:*

   - Uma forma de os visitantes entrarem em contato com você.
     Inclua campos para nome, e-mail e uma mensagem.
     Considere adicionar uma opção de "Assunto" para ajudar a direcionar as mensagens.

   <br>

7. *Links para Redes Sociais:*

   Ícones ou botões que levam os visitantes às suas redes sociais profissionais, como LinkedIn e GitHub.

   <br>

8. *Design Responsivo:*

   Certifique-se de que o site seja responsivo, ou seja, que se adapte a diferentes dispositivos, como smartphones e tablets.

   <br>

9. *SEO (Otimização para Mecanismos de Busca):*

   Use técnicas de SEO para melhorar a visibilidade do seu site nos mecanismos de busca, como o Google.

   <br>

10. *Hospedagem e Domínio:*

    Escolha um serviço de hospedagem confiável e registre um domínio relacionado ao seu nome ou profissão.

    <br>

11. Manutenção Regular:

    Atualize seu site periodicamente com novos projetos e informações relevantes. Verifique se todos os links e formulários estão funcionando corretamente.

    <br>

12. Política de Privacidade (se aplicável):

    Você coletar informações pessoais dos visitantes (por meio do formulário de contato, por exemplo), é importante incluir uma política de privacidade.

> *Lembre-se de que o design e o conteúdo do seu site portfolio devem refletir sua personalidade, estilo e objetivos profissionais. Essas especificações são uma base sólida, mas você pode personalizar o site de acordo com suas preferências.*

---

<br><br>

# Tecnologias necessarias
* *Front-end:*
    * HTML 5
    * CSS 3
    * Java script
* *Back-end:*
    * Python / Django
* *Banco de dados:*
    * SQL
---

<br><br>

# Passos para a criação

1. *Design e Estrutura:*

    * Procure modelos prontos para obter inspiração.
    * Crie um esboço do design do site, incluindo a disposição das seções.
    * Escolha um modelo ou comece a criar.

<br>

2. *Front-end:*

    * Crie a estrurua com HTML 5 seguindo as boas praticas da porgramação.
    * Crie a estilização 
    * modo responsivo

<br>

3. *Banco de dados: (models)*

    * _Categoria de projeto_
    
        * Nome
        * Slug

    <br>

    * _Projeto:_

        * Nome
        * Slug
        * categoria
        * capa
        * descrição
        * conteudo com capa?
        * conteudo
        * visivel?
        * status
        * tem aplicação?
        * link de aplicação
    
    <br>

    * _Categoria de serviço:_

        * Nome
        * Slug

    <br>

    * _serviço:_

        * usuario
        * categoria
        * descrição
        * status
        
    <br>

    * _Categoria de postagem_ ( blog )

        * Nome
        * slug
        
    <br>

    * _tag de postagem_ ( blog )

        * Nome
        * slug

    <br>

    * _comentario de postagem_ ( blog )

        * usuario
        * comentario
        * resposta
        
    <br>

    * _postagem_ ( blog )

        * titulo
        * Slug
        * categoria
        * capa
        * descrição
        * conteudo com capa?
        * conteudo
        * visivel?
        * data de criação
        * criador
        * data de atualização
        * quem atualizou ?
        * tags
        * comentarios
        * relevancia
        * visualizações
    
    <br>


4. *Back-end:*
    
    * .env
    * idioma
    * data e hora
    * diretórios globais
    * aplicativos
    * URLs
    * views
    * tratamento de imagens ( pillow )
    * base de dados
    * migrações
    * admin
    * geração de slug
    * CRUDs
    * Summernote
    * Erro 404
    * redirecionamento de páginas
    * paginação
    * mensagens