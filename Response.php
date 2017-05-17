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

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="main.html">Chest Opener!</a>
    </div>

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
  <h1>Clash Royale Chest Opener</h1>
  <p>Have your own robot open your chests</p> 
</div>
<br><br><br>
<center>Infomation being sent to the Mindstorms</center>
<br><br><br>

<center>
    Created By Boston Abrams<br>
    (c) 2017
</center>
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
Firing at heading &nbsp; <?php echo htmlspecialchars($_POST["Heading"]); ?><br>
With a distance of&nbsp; <?php echo htmlspecialchars($_POST["Distance"]); echo $Unit?><br>


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
