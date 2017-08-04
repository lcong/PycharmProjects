<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
 <head>
  <title> Test </title>
 </head>

 <body>

<?php 
$text = (isset($_POST['text']) ? $_POST['text'] : null);
if ($text) print 'Text: <B>'.$text.'</B>'; 
?>

  <form method="post" action="/action.php">
	<input type="text" name="text">
	<input type="submit">
  </form>
 </body>
</html>
