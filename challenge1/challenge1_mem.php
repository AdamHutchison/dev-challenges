<?php

$n = $argv[1];

function countSteps($n, $cachedValues = [])
{
    if ($n < 0) {
        return 0;
    } elseif ($n == 0) {
        return 1;
    } elseif(array_key_exists($n, $cachedValues)) {
        return $cachedValues[$n];
    } else {
        $cachedValues[$n] = countSteps($n - 1, $cachedValues) + countSteps($n - 2, $cachedValues) + countSteps($n - 3, $cachedValues);
        return $cachedValues[$n];
    }
}

print_r(countSteps($n));