<?php


//get data
$button = $_GET['submit'];
$search = $_GET['search'];
// // popen('alert', 'r')
// $output = shell_exec('notify-send  terminal "Run"');
// // echo "<pre>$output</pre>";
// $output = shell_exec('./wget_script.sh "https://scholar.google.co.in/scholar?hl=en&q=Albert+Einstein&oq=" /home/user/Desktop/a.html ');
// echo "<pre>$output</pre>";

$s = $_GET['s'];
if (!$s)
$s = 0;

$output = shell_exec('cat first');
echo "$output";
// echo "ABHINAV"

$e = 10; // Just change to how many results you want per page


$next = $s + $e;
$prev = $s - $e;

// data=file_get_contents('http://google.com');




  
  //connect to database
  mysql_connect("localhost","root","ubuntu");
  mysql_select_db("search");
   $curl_q .= "https://scholar.google.co.in/scholar?hl=en&q=";
   //explode out search term
   $search_exploded = explode(" ",$search);
   
   foreach($search_exploded as $search_each)
   {
   
        //construct query
    $x++;
    $curl_q .= "$search_each+";
    if ($x==1) {
     $construct .= "title LIKE '%$search_each%'";
    }
    else {
     $construct .= " AND title LIKE '%$search_each%'";
    }
   
   }
   echo "$curl_q\n";
   $qr .= "./wget_script.sh '$curl_q' /home/user/Desktop/a.html ";
   echo "$qr";
// $output = shell_exec($qr);
// echo "<pre>$output</pre>";
  //echo outconstruct
  $constructx = "SELECT * FROM searchengine WHERE $construct";
  
  $construct = "SELECT * FROM searchengine WHERE $construct ORDER BY citation desc LIMIT $s,$e";
  $run = mysql_query($constructx);
  
  $foundnum = mysql_num_rows($run);


  $run_two = mysql_query("$construct");
  
  if ($foundnum==0) {}

  else
  {

   
   
   
   // while ($runrows = mysql_fetch_assoc($run_two))
    while ($runrows = mysql_fetch_assoc($run_two))
   {
    //get data
   $title = $runrows['title'];
   $abs = $runrows['abstract'];
   $url = $runrows['url'];
   $citation = $runrows['citation'];
   $author = $runrows['author'];

$output = shell_exec('cat second');
echo "$output";
echo "$title";
$output = shell_exec('cat third');
echo "$output";
echo "$author";
$output = shell_exec('cat four');
echo "$output";
echo "$abs";
$output = shell_exec('cat five');
echo "$output";

echo "$citation";
$output = shell_exec('cat six');
echo "$output";
   
   
   }
?>

<?php 
}
?>
