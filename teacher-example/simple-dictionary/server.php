es (21 sloc)  548 Bytes

IntelliJ IDEA
PhpStorm
WebStorm
<?php

// To run server
// php -S 0.0.0.0:8080 .\server.php

// To load homepage in browser
// localhost:8080/

// To check meaning of words in browser
// localhost:8080?word=hello

//------------------------------------------------------

$word = $_GET["word"];
echo $word;

if($word == ""){
    echo file_get_contents("./index.html");
}else{
    $arr = array(
        "hello"     =>  "سلام",
        "hi"        =>  "سلام",
        "goodbye"   =>  "خداحافظ",
        "bye"       =>  "خداحافظ",
    );
    echo $arr[$word];
}