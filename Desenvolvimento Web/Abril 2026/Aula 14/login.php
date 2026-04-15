<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="css/login.css">
</head>

<body>
    <main class="login-container">
        <form class="login-form" method="POST" action="">
            <h1 class="login-title">Entrar</h1>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" name="email" placeholder="Email" required id="email" autocomplete="username" placeholder="seumail@exemplo.com">
                <?php $erro = $_GET['erro'] ?? null; ?>
                <?php if ($erro): ?>
                    <div class="alert alert-error" role="alert"><?= htmlspecialchars($erro) ?></div>
                <?php endif; ?>
            </div>
            <div class="form-group">
                <label for="senha">Senha</label>
                <input type="password" name="senha" placeholder="Senha" required id="senha" autocomplete="current-password" placeholder="........">
            </div>

            <button type="submit" class="btn btn-primary">Entrar</button>
        </form>
    </main>

</body>

</html>