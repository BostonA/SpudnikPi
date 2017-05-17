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
    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
         <li><a href="DoIt.html">Do it!</a></li>
        <li><a href="About.html">About</a></li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
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
$Heading = htmlspecialchars($_POST["Heading"]);
$Distance = htmlspecialchars($_POST["Distance"]);
$Unit = htmlspecialchars($_POST["Unit"]); 
$myfile = fopen("DataStore.txt", "a") or die("Unable to open file!");
if ($Unit == "Feet"){
  $SUnit = "F";
}
else if ($Unit == "Meters"){
  $SUnit = "M";
}
fwrite($myfile, $Heading);
fwrite($myfile, " ");
fwrite($myfile, $Distance);
fwrite($myfile, " ");
fwrite($myfile, $SUnit);
fwrite($myfile, "\n");

?>
</body>
</html>
