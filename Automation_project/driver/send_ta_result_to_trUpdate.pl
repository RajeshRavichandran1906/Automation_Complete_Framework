$| = 1;

$size = undef;

$size = @ARGV;




open (FILE, "<$ARGV[0]") || die "ERROR: Cannot open $ARGV[0] for reading\n";
                      
$i=1;
$pass1 = 0;
$pass2 = 1;
$pass3 = 0;
$summary_line = "0";

$tool_val = $ARGV[1];
$conf_val = $ARGV[2];
$rel_val = $ARGV[3];
$prod_val = $ARGV[4];

$pkgname = $ARGV[5];

$tcid = $ARGV[6];

$rid = $ARGV[7];
$br=$ARGV[8];
$tcid =~ s/C//i;



@string=(84, 111, 108, 115, 116, 111, 121, 49, 57, 56, 54);

$param = undef;

foreach $item (@string) {

        chomp $item;    
        	
	$char = chr(${item});
        $param = "${param}" . "${char}";
}

$param = undef;

$param = "Li47OFB.CFpL1diBiImX-iDa9PymKNq7v47dAz4nR";


while (<FILE>) {

  if ($_ =~ /.*title-summary.>Result<.td><td class=.(....).*/) {
     $status = $1 eq 'pass' ? 1 : 5;
  }
  
  
  if ($i > 1000) {
    last;
  }
  $i++;
}

close FILE;



#print "status: $status\n";

%browser = ("ie", "2", "cr", "21", "ff", "23");

%rel = ("8105m", "2", "8106", "3", "head", "4", "8200", "5", "headcont", "6", "8106cont", "7", "8200m", "8", "8201", "9", "8201cont", "10","8201m","11");

%conf = ("391","2","455","3","487","4","489","5","506","6","223","7","281","8","338","9","508","10","232","11",
         "250","12","279","13","302","14","323","15","334","16","348","17","394","18","396","19","401","20",
         "408","21","453","22","471","23","485","24","501","25","502","26","515","27","500","28","513","29",
         "512","30","507","31","486","32","496","33","498","34","497","35","577","36","291","37","292",
         "38","293","39","294","40","295","41","296","42","341","43","342","44","343","45","344","46","345",
         "47","346","48","591","49","592","50","593","51","594","52","595","53","596","54","bue1","55","bue2","56","wf1","57","wf4","66","wf5","67","wf2","82","wf7","85");


%tool=("ta","2","ut","3","si","4");

%prod=("wf","1","as","2","wq","3","wx","4","wb","5");



chomp $rid;
chomp $br;

$cmd ="\\\\bigrepos01\\bigscm\\TA\\admin\\php\\php   \\\\bigrepos01\\bigscm\\TA\\admin\\php\\add_result.php  ".
          "${param} $rid $tcid $status $pkgname $browser{$br} $rel{$rel_val} $conf{$conf_val} $tool{$tool_val} $prod{$prod_val}";
print "sending results to Test Rail...\n";
$php_out =qx($cmd);
$RC = $?;

if ($RC != 0) {
	print "ERROR: \\\\bigrepos01\\bigscm\\TA\\admin\\php\\php   \\\\bigrepos01\\bigscm\\TA\\admin\\php\\add_result.php xxxx $rid $tcid $status $pkgname $browser{$br} $rel{$rel_val} $conf{$conf_val} $tool{$tool_val} $prod{$prod_val}\n";
        print "PHP OUTPUT:\n${php_out}\n"; 
        exit(1);
} 



