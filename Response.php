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

Chest 1: &nbsp; <?php echo htmlspecialchars($_POST["Chest1"]); ?><br>
Chest 2: &nbsp; <?php echo htmlspecialchars($_POST["Chest2"]); ?><br>
Chest 3: &nbsp; <?php echo htmlspecialchars($_POST["Chest3"]); ?><br>
Chest 4: &nbsp; <?php echo htmlspecialchars($_POST["Chest4"]); ?><br>

Free Chests: &nbsp; <?php echo $_POST["openFreeChests"]; ?>

<?php
$Chest1 = htmlspecialchars($_POST["Chest1"]);
$Chest2 = htmlspecialchars($_POST["Chest2"]);
$Chest3 = htmlspecialchars($_POST["Chest3"]); 
$Chest4 = htmlspecialchars($_POST["Chest4"]); 
$myfile = fopen("/tmp/newfile.txt", "a") or die("Unable to open file!");
$Chests = [$Chest1, $Chest2, $Chest3, $Chest4];
$txt = implode (" ", $_POST);
$y = "N";
$x = htmlspecialchars($_POST["openFreeChests"]);
$z = 0;
while ($z < 4) {
  if ($Chests[$z] == "Silver"){
    $txt = "03";
    fwrite($myfile, $txt);
  }
  elseif ($Chests[$z] == "Gold"){
    $txt = "08";
    fwrite($myfile, $txt);
  }
  elseif ($Chests[$z] == "Magic"){
    $txt = "12";
    fwrite($myfile, $txt);  
  }
  elseif ($Chests[$z] == "Epic"){
    $txt = "12";
    fwrite($myfile, $txt);  
  }
  elseif ($Chests[$z] == "Giant"){
    $txt = "12";
    fwrite($myfile, $txt);  
  }
  elseif ($Chests[$z] == "SuperMagic"){
    $txt = "24";
    fwrite($myfile, $txt);
  }
  elseif ($Chests[$z] == "Legendary"){
    $txt = "24";
    fwrite($myfile, $txt); 
  }
  elseif ($Chests[$z] == "Empty"){
    $txt = "00";
    fwrite($myfile, $txt); 
  }
  else {
    $txt = "00";
    fwrite($myfile, $txt); 
  }
  $txt = " ";
  fwrite($myfile, $txt); 
  $z = $z + 1;
} 
if ($x == "on"){
  $y = "Y";
}
if ($y == "Y"){
  $txt = "Y";
  fwrite($myfile, $txt);
}
if ($y == "N") {
  $txt = "N";
  fwrite($myfile, $txt);
  }
$txt = "\n";
fwrite($myfile, $txt);
?>
</body>
</html>
