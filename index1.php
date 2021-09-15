<?php
    shell_exec("/usr/local/bin/gpio -g mode 5 out");
    if(isset($_GET['off']))
        {
                        echo "<center><h1>Drip Irrigation Motor is OFF</h1></center>";
                        shell_exec("/usr/local/bin/gpio -g write 5 0");
                        echo "<center><h1><a href=index.html>BACK</a></h1></center>";
        }
            else if(isset($_GET['on']))
            {
                        echo "<center><h1>Drip Irrigation Motor is ON</h1></center>";
                        shell_exec("/usr/local/bin/gpio -g write 5 1");
                        echo "<center><h1><a href=index.html>BACK</a></h1></center>";
                        
            }
            
      shell_exec("/usr/local/bin/gpio -g mode 11 out");
    if(isset($_GET['off1']))
        {
                        echo "<center><h1>Sprinkler Irrigation Motor is OFF</h1></center>";
                        shell_exec("/usr/local/bin/gpio -g write 11 0");
                        echo "<center><h1><a href=index.html>BACK</a></h1></center>";
        }
            else if(isset($_GET['on1']))
            {
                        echo "<center><h1>Sprinkler Irrigation Motor is ON</h1></center>";
                        shell_exec("/usr/local/bin/gpio -g write 11 1");
                        echo "<center><h1><a href=index.html>BACK</a></h1></center>";
            }       
?>
  
