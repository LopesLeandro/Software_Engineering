<html>
  <head>
    <title>Formulário</title>
  </head>
  <body>
    <form action="processa.php" method="POST">
      <!--IMPORTANTE: FIELDSET E LEGENDA não são obrigatórios-->
      <fieldset>
        <legend>Dados pessoais</legend>
        <label  for="nome">Nome:</label>
        <input required type="text" name="nome" id="nome" placeholder="Digite seu nome completo">
        <input type="hidden" name="secreto" value="1234">

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" placeholder="Digite seu e-mail">
        <p>
          <label for="senha">Senha:</label>
          <input type="password" name="senha"id="senha">
        </p>
      <p>
        <label for="data">Data:</label>
        <input type="date" name="ndata" id="data">
      </p>
        <p>
          <label for="cor">Cor:</label>
          <input type="color" name="cor" id="cor"
        </p>
        <p>
          <label for="checkidade">Maior de idade:</label>
          <input type="checkbox" name="cidade" id="checkidade">
        </p>
        <p>
          <label for="rbcidade">Mora em Joinville:</label>
          <input type="radio" name="rbcidade" id="rbcidade" value="jlle">
          <label for="rbcidade">Mora em Curitiba:</label>
          <input type="radio" name="rbcidade" id="rbcidade" value="ctb">
        </p>
        <p>
          <label for="arquivo">Arquivo:</label>
          <input type="file" name="arquivo" id="arquivo">
        </p>
        <p>
          <label for="textao">Textão:</label>
          <textarea name="textao" id="textao"></textarea>
        </p>
        <p>
          <label for="selecao">Seleção:</label>
          <select name="selecao" id="selecao">
            <?php for($i=0;$i<11;$i++){ ?>
              <option><?=$i ?></option>
            <?php } ?>
          </select>
        </p>
      </fieldset>
      <fieldset>
        <legend>Suas preferências</legend>
      </fieldset>
      <p><input type="submit"></p>
      <p><input type="reset" value="Limpar"></p>
    </form>
  </body>
</html>