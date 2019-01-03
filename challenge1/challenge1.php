<?php

$n = 4;

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

print_r(countSteps($n));