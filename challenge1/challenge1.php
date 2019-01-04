<?php

$n = $argv[1];

function countSteps($n)
{
    if ($n < 0) {
        return 0;
    } elseif ($n == 0) {
        return 1;
    } else {
        return countSteps($n - 1) + countSteps($n - 2) + countSteps($n - 3);
    }
}

echo countSteps($n);