<?php
class ConexaoBanco extends PDO
{
    private static $instancia = null;

    public function __construct($dsn, $usuario, $senha)
    {
        parent::__construct($dsn, $usuario, $senha);
    }

    public static function getInstancia()
    {
        if (self::$instancia === null) {
            try {
                $dsn = 'mysql:host=localhost;dbname=techtalent_db;charset=utf8mb4';
                $usuario = 'root';
                $senha = '';
                self::$instancia = new ConexaoBanco($dsn, $usuario, $senha);
            } catch (PDOException $e) {
                header('Location: ../view/erro.php?mensagem=' . urlencode('Erro de conexão: ' . $e->getMessage()));
                exit;
            }
        }
        return self::$instancia;
    }
}
