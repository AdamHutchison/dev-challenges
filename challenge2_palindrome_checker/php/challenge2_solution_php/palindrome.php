<?php

include './Dequeue.php';

$n = $argv[1];

function isPalindrome($string)
{
    $dq = new Dequeue();
    $dq->setItems($string);

    $isPalindrome = true;

    while($dq->size() > 1) {
        if($dq->removeFront() != $dq->removeRear()) {
            $isPalindrome = false;
        }
    }

    return $isPalindrome;
}

isPalindrome($n) ? print_r('true') : print_r('false');