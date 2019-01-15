<?php

class Dequeue
{
    protected $items;

    public function __construct()
    {
        $this->items = [];
    }

    public function setItems($string)
    {
        $items = str_split(strtolower($string));

        // create an array containing lowercase letter ascii values
        $lowercaseAsciiValues = range(ord('a'), ord('z') + 1);

        // create an array containing uppercase letter ascii values
        $uppercaseAsciiValues = range(ord('A'), ord('Z') + 1);

        foreach ($items as $item) {
            if (in_array(ord($item), $lowercaseAsciiValues)) {
                $this->addRear($item);
            } elseif (in_array(ord($item), $uppercaseAsciiValues)) {
                // difference between upper case and lowercase ascii valies is +32
                $this->addRear(chr(ord($item) + 32));
            }
        }
    }

    public function addFront($item)
    {
        array_unshift($this->items, $item);
    }

    public function addRear($item)
    {
        array_push($this->items, $item);
    }

    public function removeFront()
    {
        return array_shift($this->items);
    }

    public function removeRear()
    {
        return array_pop($this->items);
    }

    public function peekFront()
    {
        return $this->items[0];
    }

    public function peekRear()
    {
        return end($this->items);
    }

    public function size()
    {
        return count($this->items);
    }

    public function isEmpty()
    {
        return $this->size() == 0;
    }
}