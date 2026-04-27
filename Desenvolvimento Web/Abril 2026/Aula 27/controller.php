<?php 

    include_once 'cliente.php';
    // include_once 'cliente.class.php';

    // include()
    // require()
    // include_once() chamar apenas uma vez o arquivo. Se chamar duas vezes a segunda vai retornar falso
    // require_once() chamar apenas uma vez o arquivo. Se chamar duas vezes a segunda vai retornar falso


    $cliente1 = new Cliente();

    $cliente1->setId(2);
    $cliente1->setRg(22222222);
    $cliente1->setNome("Lucas");

    echo '<p>ID do cliente: ' . $cliente1->getId() . '<br> 
            RG do cliente: ' . $cliente1->getRg() . '<br> 
            Nome do cliente: ' . $cliente1->getNome() . '<br> 
    </p>';

    echo '<p>ID do cliente: ' . $cliente1->getId() . '<br>'; 
    echo 'RG do cliente: ' . $cliente1->getRg() . '<br>'; 
    echo  'Nome do cliente: ' . $cliente1->getNome() . '<br> </p>';

?>