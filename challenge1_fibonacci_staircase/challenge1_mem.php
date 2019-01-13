<?php

$n = $argv[1];

function countSteps($n, &$cache = [])
{
    if ($n < 0) {
        return 0;
    } elseif ($n == 0) {
        return 1;
    } elseif(array_key_exists($n, $cache)) {
        return $cache[$n];
    } else {
        $cache[$n] = countSteps($n - 1, $cache) + countSteps($n - 2, $cache) + countSteps($n - 3, $cache);
        return $cache[$n];
    }
}

print_r(countSteps($n));