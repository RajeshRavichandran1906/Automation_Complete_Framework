#!/usr/local/bin/perl
use Win32::Registry;
use Win32::OLE;
$classpath="\\\\bigrepos01\\bigscm\\admin\\bin";
use Cwd;

$workspace=getcwd();
$workspace=~ s/\//\\/;
$br = shift(@ARGV);
$suitepath = shift(@ARGV);
#$testrailpath = shift(@ARGV);
$list= shift(@ARGV);
$suite = $suitepath ;
$suite=~s /.*\\//;
$imageDir="$suitepath\\images";
exit
  if not (-e $imageDir);
$actual_imageDir="$suitepath\\actual_images";
chdir($imageDir);
open ( FILE,">C:\\temp\\${suite}.html");

print FILE "<html>\n";
print FILE "<head>\n";
print FILE "<title>image comparison report</title>\n";
print FILE "</head>\n";
print FILE  "<body>\n";
$time=localtime(time);
print FILE "<h1>Report for $suite in $br-- Date:${time}</h1>\n";
print FILE "<script type=\"text/javascript\">\n";
print FILE  "function compare(pic1,pic2,reportname){\n";
print FILE "var w = new ActiveXObject(\"WScript.Shell\")\n";
print FILE "w.run (\"\\\\\\\\bigrepos01\\\\bigscm\\\\tst_results\\\\compare2pics.vbs \"+pic1+\" \" +pic2+\" \"+reportname)\n";
print FILE "}\n";
print FILE "</script>\n";
print FILE "<table>\n";


my @resp=qx(ls -a|sort);
   
   
foreach(@resp) {
  
 if($_ =~ /C\d+/){
  
  chomp($_);
  $base=$_;
  $actual=$_;
  $testname=$base;
  $testname =~ s/\_.*//;
  chomp ($testname);
  $actual =~ s/Base/Actual/;
  $baseimage="$imageDir\\${base}";
  $newimage="$actual_imageDir\\${actual}";
  #print "$baseimage\n";
  if( -e "$workspace/$newimage"){
  #print "$newimage\n";
print FILE "<tr>\n";
$cmd="node c:\\compare2pics.js $workspace/${baseimage} $workspace/$newimage $testname";
$status= qx($cmd);
my @now = localtime();
my $timeStamp = sprintf("%04d%02d%02d%02d%02d%02d", 
                        $now[5]+1900, $now[4]+1, $now[3],
                        $now[2],      $now[1],   $now[0]);

$baseimage_save=$baseimage;
$newimage_save=$newimage;
$baseimage_save=~ s/\.png//i;
$baseimage_save=~ s/.*\\//i;
$newimage_save=~ s/\.png//i;
$newimage_save=~ s/.*\\//i;

$baseimage_save="\\\\bigrepos01\\bigscm\\tst_results\\${baseimage_save}_${timeStamp}".".png";
$newimage_save= "\\\\bigrepos01\\bigscm\\tst_results\\${newimage_save}_${timeStamp}".".png";
$cmd="copy /y  $workspace\\${baseimage} $baseimage_save";
print "$cmd\n";
system($cmd);
$cmd="copy /y  $workspace\\$newimage $newimage_save";
print "$cmd\n";
system($cmd);
$baseimage_save=~s/\\/\\\\/g;
$newimage_save=~s/\\/\\\\/g;



print FILE"<td><A href=\"javascript:compare('$baseimage_save','$newimage_save','$testname')\">$testname</A></td>\n";
if  ($status eq "pass"){ 
    print FILE "<td align=\"right\"><font color=green>Passed</td>\n";
}elsif ($status = "fail"){
    print FILE "<td align=\"right\"><font color=red>Failed</td>\n";
}
}

}
print FILE "</tr>\n";
}

print FILE "</br\n";
print FILE "</table>\n";
print FILE "</body>\n";
print FILE "</html>\n";
close(FILE);
$cmd="phantomjs c:\\testrail.js $suite \"$testrailpath\"";
print "$cmd\n";
#system($cmd);
$mailgp="Arif_Bhuiyan\@ibi.com,$list";
$contacts="$mailgp".","."$contacts";
$from="qaauto\@ibi.com";
$sub="\"$suite image comparison report from $br\"";
$message="\"Please save ${suite}.html before open in ie\"";
$report1="c:\\temp\\${suite}.html";
#$report2="c:\\temp\\${suite}.png";
$cmd="java   -cp $classpath emailtogp $contacts $from  $sub $message $report1 $report2";
print "$cmd\n";
system($cmd);



# call ie 

#$ie = Win32::OLE->new('InternetExplorer.Application') ;
#$ie->{'Visible'} = 1;
#$ie->navigate("C:\\resutlt.html");
#$ie->Refresh();