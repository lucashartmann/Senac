<?php

session_start();

$_SESSION = array();



if (ini_get("session.use_cookies")) {
    try {
        $params = session_get_cookie_params();
        setcookie(session_name(), "", time() - 42000, $params["path"], $params["domain"], $params['httponly']);
    } catch (Exception $e) {
        return;
    }
}


session_destroy();

header("Location: ../../index.php");

exit();