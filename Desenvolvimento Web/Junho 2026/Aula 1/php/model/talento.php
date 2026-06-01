<?php

class Talento
{
    private int $id;
    private string $nome;
    private string $email;
    private string $fone;
    private string $tecnologia;
    private string $senha;
    private ?string $curriculo;

    public function getSenha(): string
    {
        return $this->senha;
    }

    public function setSenha(string $senha): self
    {
        $this->senha = $senha;

        return $this;
    }

    public function getCurriculo(): string
    {
        return $this->curriculo;
    }

    public function setCurriculo(string $curriculo): self
    {
        $this->curriculo = $curriculo;

        return $this;
    }

    public function getId(): int
    {
        return $this->id;
    }

    public function setId(int $id): self
    {
        $this->id = $id;

        return $this;
    }

    public function getNome(): string
    {
        return $this->nome;
    }

    public function setNome(string $nome): self
    {
        $this->nome = $nome;

        return $this;
    }

    public function getEmail(): string
    {
        return $this->email;
    }

    public function setEmail(string $email): self
    {
        $this->email = $email;

        return $this;
    }

    public function getFone(): string
    {
        return $this->fone;
    }

    public function setFone(string $fone): self
    {
        $this->fone = $fone;

        return $this;
    }

    public function getTecnologia(): string
    {
        return $this->tecnologia;
    }

    public function setTecnologia(string $tecnologia): self
    {
        $this->tecnologia = $tecnologia;

        return $this;
    }

    public function __toString()
    {
        return "Talento: {$this->getNome()} | Email: {$this->getEmail()} | Fone: {$this->getFone()} | Tecnologia: {$this->getTecnologia()}";
    }
}
