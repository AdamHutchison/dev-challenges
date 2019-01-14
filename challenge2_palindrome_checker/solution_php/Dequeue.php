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
        $sanitisedString = preg_replace('/[^a-z]/i','',$string);
        $this->items = str_split(strtolower($sanitisedString));
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