<!DOCTYPE html>
<html lang="en">
<head>
  <style>
  #BottomPart { float:left;}
  .success { background-color: #ccffcc;}
  </style>
  <link rel="shortcut icon" href="favicon.ico" type="image/x-icon">
  <title>Spudnik Pi!</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>
<body>
<?php 
$myfile = fopen("SendBack.txt", "r") or die("Unable to open Return File!");
while(!feof($myfile)) {
  $Cool =  fgets($myfile);
}fclose($myfile);
$Angle = $Cool[0] . $Cool[1] . $Cool[2]; 
$Heading = $Cool[4] . $Cool[5] . $Cool[6];
switch ($Cool[8]) {
    case "F":
        $State = "Firing";
        break;
    case "L":
      $State =  "Loaded";
      break;
    case "U":
        $State = "Not Loaded";
        break;
    default:
        $State = "ERROR";
}
?>
<center>Current Positions! Angle: <?php echo $Angle?> Deg. // Heading: <?php echo $Heading?>  // Stat: <?php echo $State?> </center>

<div class="jumbotron text-center">
  <h1>Spudnik Pi</h1>
  <p>Spuds Away</p></p>
</div>
<form action="Response.php" method="post">
        <h3><center>Questions</center></h3>
        <div class="col-sm-5 col-md-1.5">
          <div class="thumbnail">
            <div class="caption">
              <center>
                 How Far: <input type="text" name="Distance"><br>
              </center>
            </div>
          </div>
        </div>
        <div class="col-sm-5 col-md-3">
          <div class="thumbnail">
            <div class="caption">
              <center>
                Heading: <input type="text" name="Heading"><br>
              </center>
            </div>
          </div>
        </div>
        <div class="col-sm-5 col-md-3">
          <div class="thumbnail">
            <div class="caption">
              <center>
                <input onclick="displayResult()" type="radio" name="Unit" value="Meters">Metric >  Meters&nbsp;&nbsp;&nbsp;<br><br>
                <input onclick="displayResult()" type="radio" name="Unit" value="Feet">Imperial > Feet &nbsp;&nbsp;&nbsp;
              </center>
            </div>
          </div>
        </div>
      </div>
<center>
    <input type="submit" value="Fire" class="btn btn-danger"/>
</form>
<center>
  <div>
    Created By Boston Abrams
    (c) 2017
  </div>
</center>
</body>
</html>
