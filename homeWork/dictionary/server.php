<?php

xdebug_break();
$word = $_GET["word"];
$translate =$_GET["translate"]; 
$arr = array(
    "hello"     =>  "سلام",
    "hi"        =>  "سلام",
    "goodbye"   =>  "خداحافظ",
    "bye"       =>  "خداحافظ",
);

xdebug_break();
//print_r($word);
if($word == ""){
    echo file_get_contents("./index.html");
}elseif( $word != ""  &  $translate == ""){
    echo  $arr[$word];
}elseif ( $word != "" && $translate != ""){
   // $arr[$word] = $translate;
    print_r($translate);
   // echo  $arr[$word];
}
