<?php 

class Talento {
    private int $id;
    private string $nome;
    private string $email;
    private string $fone;
    private string $tecnologia;

    /**
     * Get the value of id
     *
     * @return int
     */
    public function getId(): int
    {
        return $this->id;
    }

    /**
     * Set the value of id
     *
     * @param int $id
     *
     * @return self
     */
    public function setId(int $id): self
    {
        $this->id = $id;

        return $this;
    }

    /**
     * Get the value of nome
     *
     * @return string
     */
    public function getNome(): string
    {
        return $this->nome;
    }

    /**
     * Set the value of nome
     *
     * @param string $nome
     *
     * @return self
     */
    public function setNome(string $nome): self
    {
        $this->nome = $nome;

        return $this;
    }

    /**
     * Get the value of email
     *
     * @return string
     */
    public function getEmail(): string
    {
        return $this->email;
    }

    /**
     * Set the value of email
     *
     * @param string $email
     *
     * @return self
     */
    public function setEmail(string $email): self
    {
        $this->email = $email;

        return $this;
    }

    /**
     * Get the value of fone
     *
     * @return string
     */
    public function getFone(): string
    {
        return $this->fone;
    }

    /**
     * Set the value of fone
     *
     * @param string $fone
     *
     * @return self
     */
    public function setFone(string $fone): self
    {
        $this->fone = $fone;

        return $this;
    }

    /**
     * Get the value of tecnologia
     *
     * @return string
     */
    public function getTecnologia(): string
    {
        return $this->tecnologia;
    }

    /**
     * Set the value of tecnologia
     *
     * @param string $tecnologia
     *
     * @return self
     */
    public function setTecnologia(string $tecnologia): self
    {
        $this->tecnologia = $tecnologia;

        return $this;
    }

    public function __toString() {
        return "Talento: {$this->getNome()} | Email: {$this->getEmail()} | Fone: {$this->getFone()} | Tecnologia: {$this->getTecnologia()}";
    }
}