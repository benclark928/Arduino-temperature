<?php
mysql_connect("localhost", "root", "root");
mysql_select_db("temperature");
mysql_query("select * from temperature.dht11serial");
?>

<table border=1> 
    <tr>
        <th>Temperature</th>
        <th>Time</th>
    <tr>
<?php while ($r = mysql_fetch_array($s))
{
?>
    <tr>
        <td><?php echo $r['temperature']; ?></td>
        <td><?php echo $r['time']; ?></td>
    <tr>
<?php } ?>
</table>