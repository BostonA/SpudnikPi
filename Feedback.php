<<<<<<< HEAD
<!DOCTYPE html>
<html lang="en">
<head>
  <style>
  #BottomPart { float:left;}
  .success { background-color: #ccffcc;}
  </style>
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  <title>Chest Opener</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<div class="jumbotron text-center">
 <h1>Spudnik Pi</h1>
  <p>Spuds Away</p></p> 
</div>
<br><br><br>


<?php
$Unit = "NULL";
if (htmlspecialchars($_POST["Units"]) == "Meters") {
  if ($_POST["Distance"] == "1"){
    $Unit = " Meter";
  }
  else {
    $Unit = " Meters";
  }}
if (htmlspecialchars($_POST["Units"]) == "Feet") {
  if ($_POST["Distance"] == "1"){
    $Unit = " Foot";
  }
  else {
    $Unit = " Feet";
  }
}
?>
<center>
Thank you
<br><br>
Would you like to fire again?<br>
<a href="index.html">Yes</a><br>

    Created By Boston Abrams<br>
    (c) 2017
</center>
<?php
$Distance = htmlspecialchars($_POST["RealDistance"]);
$Unit = htmlspecialchars($_POST["Units"]); 
$myfile = fopen("DataStore.txt", "a") or die("Unable to open file!");
if ($Unit == "Feet"){
  $SUnit = "F";
}
else if ($Unit == "Meters"){
  $SUnit = "M";
}
fwrite($myfile, " ");
fwrite($myfile, $Distance);
fwrite($myfile, " ");
fwrite($myfile, $Sunit);
?>
</body>
</html>
=======
<!DOCTYPE html>
<html lang="en">
<head>
  <style>
  #BottomPart { float:left;}
  .success { background-color: #ccffcc;}
  </style>
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  <title>Chest Opener</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<div class="jumbotron text-center">
 <h1>Spudnik Pi</h1>
  <p>Spuds Away</p></p> 
</div>
<br><br><br>


<?php
$Unit = "NULL";
if (htmlspecialchars($_POST["Units"]) == "Meters") {
  if ($_POST["Distance"] == "1"){
    $Unit = " Meter";
  }
  else {
    $Unit = " Meters";
  }}
if (htmlspecialchars($_POST["Units"]) == "Feet") {
  if ($_POST["Distance"] == "1"){
    $Unit = " Foot";
  }
  else {
    $Unit = " Feet";
  }
}
?>
<center>
Thank you
<br><br>
Would you like to fire again?<br>
<a href="index.html">Yes</a><br>

    Created By Boston Abrams<br>
    (c) 2017
</center>
<?php
$Distance = htmlspecialchars($_POST["RealDistance"]);
$Unit = htmlspecialchars($_POST["Units"]); 
$myfile = fopen("Python/DataStore.txt", "a") or die("Unable to open file!");
if ($Unit == "Feet"){
  $SUnit = "F";
}
else if ($Unit == "Meters"){
  $SUnit = "M";
}
fwrite($myfile, " ");
fwrite($myfile, $Distance);
fwrite($myfile, " ");
fwrite($myfile, $Sunit);
?>
</body>
</html>
>>>>>>> 83b969d6206f09b847cf5f7cfa70a2fc7513f28a
