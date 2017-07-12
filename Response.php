<!DOCTYPE html>
<html lang="en">
<head>
  <style>
  #BottomPart { float:left;}
  .success { background-color: #ccffcc;}
  </style>
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  <title>Spudnik Pi</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<<<<<<< HEAD
=======
<br>
>>>>>>> c3adbb5aaa48278a2d58a4af9509fd3698fdf7f7
<div class="jumbotron text-center">
 <h1>Spudnik Pi</h1>
  <p>Spuds Away</p></p> 
</div>
<br><br><br>

<?php
$Unit = "NULL";
if (htmlspecialchars($_POST["Unit"]) == "Meters") {
  if ($_POST["Distance"] == "1"){
    $Unit = " Meter";
  }
  else {
    $Unit = " Meters";
  }}
if (htmlspecialchars($_POST["Unit"]) == "Feet") {
  if ($_POST["Distance"] == "1"){
    $Unit = " Foot";
  }
  else {
    $Unit = " Feet";
  }
}
?>
<center>

Firing at heading &nbsp; <?php echo htmlspecialchars($_POST["Heading"]); ?><br>
With a distance of &nbsp; <?php echo htmlspecialchars($_POST["Distance"]); echo $Unit?><br>
<br><br>
<form action="Feedback.php" method="post">
  What was the real distance that it flew:<br>
  <input type="text" name="RealDistance"><br><br>
  <input onclick="displayResult()" type="radio" name="Units" value="Meters">Metric >  Meters&nbsp;&nbsp;&nbsp;<br><br>
  <input onclick="displayResult()" type="radio" name="Units" value="Feet">Imperial > Feet &nbsp;&nbsp;&nbsp;
  <br><br><input type="submit" value="Submit" class="btn btn-primary"/>

</form>
<br><br>
    Created By Boston Abrams<br>
    (c) 2017
</center>

<?php
$Heading = htmlspecialchars($_POST["Heading"]);
$Distance = htmlspecialchars($_POST["Distance"]);
$Unit = htmlspecialchars($_POST["Unit"]); 
<<<<<<< HEAD
$myfile = fopen("/tmp/DataStore.txt", "a") or die("Unable to open file!");
=======
$myfile = fopen("DataStore.txt", "a") or die("Unable to open file!");
>>>>>>> c3adbb5aaa48278a2d58a4af9509fd3698fdf7f7
if ($Unit == "Feet"){
  $SUnit = "F";
}
else if ($Unit == "Meters"){
  $SUnit = "M";
}
fwrite($myfile, "\n");
fwrite($myfile, $Heading);
fwrite($myfile, " ");
fwrite($myfile, $Distance);
fwrite($myfile, " ");
fwrite($myfile, $SUnit);
fclose($myfile);
?>
</body>
<<<<<<< HEAD
</html>
=======
</html>
>>>>>>> c3adbb5aaa48278a2d58a4af9509fd3698fdf7f7
