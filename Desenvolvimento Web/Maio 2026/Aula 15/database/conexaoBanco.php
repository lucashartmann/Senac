<?php

class ConexaoBanco extends PDO
{
    private $host = 'localhost';
    private $dbname = 'cadastro';
    private $username = 'root';
    private $password = '';

    public function __construct()
    {
        
    }
}